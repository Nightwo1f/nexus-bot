import asyncio
from types import SimpleNamespace

import pytest

from core.dispatcher.dispatcher import Dispatcher
from core.handlers import login as login_pkg
from core.handlers import ui_pack as ui_pack_pkg
from core.handlers.base_handler import PacketHandler
from core.handlers.handler_meta import HandlerMeta
from core.handlers.handler_registry import HandlerRegistry
from core.handlers.login.login_error_handler import LoginErrorHandler
from core.handlers.login.login_success_handler import LoginSuccessHandler
from core.handlers.login.request_login import RequestLogin
from core.handlers.login.ui_info_handler import UiInfoHandler
from core.handlers.ui_pack.receive_pack_list import ReceivePackList
from core.protocol.byte_writer import ByteWriter
from core.protocol.packet import Packet


def run(coro):
    return asyncio.run(coro)


class DummySession:
    def __init__(self) -> None:
        self.sent: list[Packet] = []

    async def send(self, packet: Packet) -> None:
        self.sent.append(packet)


def test_handler_registry_and_packet_handler_base() -> None:
    registry = HandlerRegistry()
    assert registry.get(999) is None

    good_handler = SimpleNamespace(OPCODE=10)
    registry.register(good_handler)
    assert registry.get(10) is good_handler

    with pytest.raises(ValueError):
        registry.register(SimpleNamespace(OPCODE=-1))
    with pytest.raises(ValueError):
        registry.register(SimpleNamespace(OPCODE=10))

    with pytest.raises(NotImplementedError):
        run(PacketHandler.handle(object(), object(), object()))


def test_handler_meta_registers_and_skips(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    calls = []

    class FakeRegistry:
        def register(self, handler) -> None:
            calls.append(handler)

    monkeypatch.setattr(
        "core.handlers.handler_registry.HandlerRegistry.global_registry",
        lambda: FakeRegistry(),
    )

    class AutoHandler(metaclass=HandlerMeta):
        OPCODE = 55

        async def handle(self, session, packet) -> None:
            return None

    out = capsys.readouterr().out
    assert "Registering handler AutoHandler" in out
    assert len(calls) == 1
    assert calls[0].OPCODE == 55
    assert isinstance(calls[0], AutoHandler)

    before = len(calls)

    class SkipHandler(metaclass=HandlerMeta):
        OPCODE = "invalid"

        async def handle(self, session, packet) -> None:
            return None

    assert len(calls) == before
    assert SkipHandler.OPCODE == "invalid"


def test_dispatcher_dispatches_when_handler_exists(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = []

    class FakeHandler:
        async def handle(self, session, packet):
            calls.append((session, packet))

    fake_registry = SimpleNamespace(get=lambda opcode: FakeHandler() if opcode == 1 else None)
    monkeypatch.setattr(
        "core.handlers.handler_registry.HandlerRegistry.global_registry",
        lambda: fake_registry,
    )

    dispatcher = Dispatcher()
    session = object()
    packet = Packet(1, b"")
    run(dispatcher.dispatch(session, packet))
    assert calls == [(session, packet)]

    run(dispatcher.dispatch(session, Packet(2, b"")))
    assert len(calls) == 1


def test_login_error_handler(capsys: pytest.CaptureFixture[str]) -> None:
    handler = LoginErrorHandler()
    assert handler._decode_login_error_text(Packet(11, b"\x00")) == ""
    assert handler._decode_login_error_text(Packet(11, b"\x00\x00\x03abc")) == "abc"

    run(handler.handle(DummySession(), Packet(11, b"\x00\x00\x03abc")))
    out = capsys.readouterr().out
    assert "Login error: abc" in out

    run(handler.handle(DummySession(), Packet(11, b"\x00")))
    out = capsys.readouterr().out
    assert "Login error packet received." in out


def test_login_success_and_request_login_handlers(capsys: pytest.CaptureFixture[str]) -> None:
    session = DummySession()
    run(LoginSuccessHandler().handle(session, Packet(13, b"")))
    assert session.sent and session.sent[0].opcode == 14
    assert "ClientReady sent" in capsys.readouterr().out

    run(RequestLogin().handle(session, Packet(3, b"")))
    assert "Redirect packet (100) received" in capsys.readouterr().out


def test_ui_info_handler(capsys: pytest.CaptureFixture[str]) -> None:
    handler = UiInfoHandler()
    run(handler.handle(DummySession(), Packet(51, b"\x00")))
    assert "payload curto" in capsys.readouterr().out

    writer = ByteWriter("<")
    writer.u16(7).u32(123).string("ui.pack")
    run(handler.handle(DummySession(), Packet(51, writer.build())))
    out = capsys.readouterr().out
    assert "ui pack version: 7" in out
    assert "ui pack total size: 123" in out
    assert "ui pack name: ui.pack" in out
    assert "UiInfo packet received." in out


def test_receive_pack_list_handler(capsys: pytest.CaptureFixture[str]) -> None:
    handler = ReceivePackList()
    writer = ByteWriter("<")
    writer.u8(1)  # group A count
    writer.u8(1).u16(2).u32(3).u8(4)
    writer.u8(1)  # group B count
    writer.u16(5).u32(6).u8(7)
    writer.u8(1)  # group C count
    writer.u16(8).u32(9).string("pt")
    writer.u8(1)  # group D count
    writer.u16(10).u32(11).string("ogg")
    writer.u8(99)  # trailing bytes
    run(handler.handle(DummySession(), Packet(50, writer.build())))
    out = capsys.readouterr().out
    assert "=== PACK LIST ===" in out
    assert "Group A (1 packs)" in out
    assert "Group C (1 language packs)" in out
    assert "opcode 50 com bytes extras no final: 1" in out

    run(handler.handle(DummySession(), Packet(50, b"\x01")))
    out = capsys.readouterr().out
    assert "opcode 50 inv" in out
    assert "payload: 01" in out


def test_handler_package_exports() -> None:
    assert "LoginErrorHandler" in login_pkg.__all__
    assert "ReceivePackList" in ui_pack_pkg.__all__
