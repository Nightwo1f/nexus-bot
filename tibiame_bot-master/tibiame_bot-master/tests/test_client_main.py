import asyncio
import runpy
import struct
from types import SimpleNamespace

import pytest

import main as main_mod
from core.protocol.packet import Packet


def run(coro):
    return asyncio.run(coro)


def test_dummy_client_build_and_api(monkeypatch: pytest.MonkeyPatch) -> None:
    import clients.dummy_client as dummy_mod

    class FakeTransport:
        def __init__(self) -> None:
            self.connected = False

        def is_connected(self) -> bool:
            return self.connected

    class FakePacketStream:
        def __init__(self, transport) -> None:
            self.transport = transport

    class FakeDispatcher:
        pass

    class FakePipeline:
        def __init__(self) -> None:
            self.added = []

        def add(self, middleware) -> None:
            self.added.append(middleware)

    class FakeDebugger:
        def __init__(self, limit: int) -> None:
            self.limit = limit

    class FakeSession:
        def __init__(self, transport, stream, dispatcher, pipeline) -> None:
            self.transport = transport
            self.stream = stream
            self.dispatcher = dispatcher
            self.pipeline = pipeline
            self.calls = []
            self.next_packet = Packet(1, b"x")

        async def connect(self, host: str, port: int) -> None:
            self.calls.append(("connect", host, port))

        async def close(self) -> None:
            self.calls.append(("close",))

        async def send(self, packet: Packet) -> None:
            self.calls.append(("send", packet))

        async def receive(self, timeout=None) -> Packet:
            self.calls.append(("receive", timeout))
            return self.next_packet

    monkeypatch.setattr(dummy_mod, "TcpTransport", FakeTransport)
    monkeypatch.setattr(dummy_mod, "PacketStream", FakePacketStream)
    monkeypatch.setattr(dummy_mod, "Dispatcher", FakeDispatcher)
    monkeypatch.setattr(dummy_mod, "PacketPipeline", FakePipeline)
    monkeypatch.setattr(dummy_mod, "PacketDebugger", FakeDebugger)
    monkeypatch.setattr(dummy_mod, "Session", FakeSession)

    client = dummy_mod.DummyClient()
    assert client.host == ""
    assert client.port == 0
    assert isinstance(client.session, FakeSession)
    assert isinstance(client.dispatcher, FakeDispatcher)
    assert len(client._pipeline.added) == 1
    assert isinstance(client._pipeline.added[0], FakeDebugger)
    assert client._pipeline.added[0].limit == 500

    pkt = Packet(9, b"z")
    run(client.connect("h", 10))
    run(client.send_packet(pkt))
    received = run(client.recv_packet(timeout=0.5))
    run(client.disconnect())

    assert client.host == "h"
    assert client.port == 10
    assert received == Packet(1, b"x")
    assert client.session.calls == [
        ("connect", "h", 10),
        ("send", pkt),
        ("receive", 0.5),
        ("close",),
    ]
    client._transport.connected = True
    assert client.is_connected() is True


def test_load_handlers_imports_only_packages(monkeypatch: pytest.MonkeyPatch) -> None:
    imports = []
    modules = [
        SimpleNamespace(name="pkg_a", ispkg=True),
        SimpleNamespace(name="file_x", ispkg=False),
        SimpleNamespace(name="pkg_b", ispkg=True),
    ]
    monkeypatch.setattr(main_mod.pkgutil, "walk_packages", lambda _: modules)
    monkeypatch.setattr(main_mod.importlib, "import_module", lambda name: imports.append(name))

    main_mod.load_handlers()
    assert imports == ["core.handlers.pkg_a", "core.handlers.pkg_b"]


def test_wait_login_flow_paths(capsys: pytest.CaptureFixture[str]) -> None:
    class FakeClient:
        def __init__(self, responses, first_timeout=False, second_timeout=False) -> None:
            self.responses = list(responses)
            self.first_timeout = first_timeout
            self.second_timeout = second_timeout
            self.calls = 0
            self.disconnected = False

        async def recv_packet(self, timeout=None):
            self.calls += 1
            if self.calls == 1 and self.first_timeout:
                raise asyncio.TimeoutError
            if self.calls == 2 and self.second_timeout:
                raise asyncio.TimeoutError
            return self.responses.pop(0)

        async def disconnect(self) -> None:
            self.disconnected = True

    timed_out = FakeClient([], first_timeout=True)
    assert run(main_mod.wait_login_flow(timed_out, timeout=0.1)) is False
    assert timed_out.disconnected is True
    assert "No login response received in time." in capsys.readouterr().out

    non_13 = FakeClient([Packet(7, b"")])
    assert run(main_mod.wait_login_flow(non_13)) is True
    assert "Login response opcode: 7" in capsys.readouterr().out

    with_follow_up = FakeClient([Packet(13, b""), Packet(99, b"")])
    assert run(main_mod.wait_login_flow(with_follow_up)) is True
    out = capsys.readouterr().out
    assert "Login response opcode: 13" in out
    assert "Follow-up opcode: 99" in out

    follow_up_timeout = FakeClient([Packet(13, b"")], second_timeout=True)
    assert run(main_mod.wait_login_flow(follow_up_timeout)) is True
    assert "No follow-up after ClientReady." in capsys.readouterr().out


def test_main_flow_success_and_early_return(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeDummyClient:
        last_instance = None

        def __init__(self) -> None:
            type(self).last_instance = self
            self.connect_calls = []
            self.disconnect_calls = 0
            self.sent = []
            self.responses = [
                Packet(1, b"a"),
                Packet(50, b"b"),
                Packet(3, b"c"),
                Packet(100, b"d"),
            ]

        async def connect(self, host: str, port: int) -> None:
            self.connect_calls.append((host, port))

        async def disconnect(self) -> None:
            self.disconnect_calls += 1

        async def send_packet(self, packet: Packet) -> None:
            self.sent.append(packet)

        async def recv_packet(self, timeout=None) -> Packet:
            return self.responses.pop(0)

    monkeypatch.setattr(main_mod, "DummyClient", FakeDummyClient)
    monkeypatch.setattr(main_mod, "parse_redirect_endpoint", lambda packet: ("world.host", 7171))
    monkeypatch.setattr(main_mod, "parse_pack_entries", lambda packet: [SimpleNamespace(pack_id=1, version=2, priority=3)])
    monkeypatch.setattr(main_mod.LoginServerHelloPacket, "create", classmethod(lambda cls: Packet(3, b"h1")))
    monkeypatch.setattr(main_mod.HandshakeStep2Packet, "create", classmethod(lambda cls: Packet(19, b"h2")))
    monkeypatch.setattr(main_mod.HandshakeStep3Packet, "create", classmethod(lambda cls: Packet(18, b"h3")))
    monkeypatch.setattr(main_mod.SelectWorldPacket, "create", classmethod(lambda cls, wid: Packet(16, struct.pack("<H", wid))))
    monkeypatch.setattr(main_mod.ClientHelloPacket, "create", classmethod(lambda cls: Packet(3, b"hello")))
    monkeypatch.setattr(main_mod.LoginPacket, "create", classmethod(lambda cls, **kwargs: Packet(13, b"login")))
    monkeypatch.setattr(main_mod.ComboLoginPacket, "create", classmethod(lambda cls, **kwargs: Packet(3, b"combo")))
    monkeypatch.setattr(main_mod, "wait_login_flow", lambda client: asyncio.sleep(0, result=True))

    run(main_mod.main())
    instance = FakeDummyClient.last_instance
    assert instance.connect_calls[0] == (main_mod.LOGIN_HOST, main_mod.LOGIN_PORT)
    assert instance.connect_calls[1] == ("world.host", 7171)
    assert instance.disconnect_calls == 1
    assert instance.sent[-1] == Packet(3, b"combo")

    monkeypatch.setattr(main_mod, "wait_login_flow", lambda client: asyncio.sleep(0, result=False))
    run(main_mod.main())


def test_run_calls_load_handlers_and_asyncio(monkeypatch: pytest.MonkeyPatch) -> None:
    called = {"load_handlers": 0, "asyncio_run": 0}

    def fake_load_handlers() -> None:
        called["load_handlers"] += 1

    def fake_asyncio_run(coro) -> None:
        called["asyncio_run"] += 1
        coro.close()

    monkeypatch.setattr(main_mod, "load_handlers", fake_load_handlers)
    monkeypatch.setattr(main_mod.asyncio, "run", fake_asyncio_run)
    main_mod.run()
    assert called == {"load_handlers": 1, "asyncio_run": 1}


def test_main_entrypoint_executes_run(monkeypatch: pytest.MonkeyPatch) -> None:
    called = {"asyncio_run": 0}

    def fake_asyncio_run(coro) -> None:
        called["asyncio_run"] += 1
        coro.close()

    monkeypatch.setattr(asyncio, "run", fake_asyncio_run)
    monkeypatch.setattr(main_mod.pkgutil, "walk_packages", lambda _: [])
    monkeypatch.setattr(main_mod.importlib, "import_module", lambda name: None)

    runpy.run_path("src/main.py", run_name="__main__")
    assert called["asyncio_run"] >= 1
