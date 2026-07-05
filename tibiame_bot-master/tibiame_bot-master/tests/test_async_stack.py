import asyncio
import struct

import pytest

from core.excepts.transport_errors import TransportConnectionError
from core.infrastructure.interface import ITransport
from core.infrastructure.transport.tcp_transport import TcpTransport
from core.network import Session as SessionExport
from core.network.session import Session
from core.pipeline.logger_middleware import PacketDebugger
from core.pipeline.middleware import Middleware
from core.pipeline.packet_pipeline import PacketPipeline
from core.protocol.packet import Packet
from core.stream.packet_stream import PacketStream


def run(coro):
    return asyncio.run(coro)


class DummyTask:
    def __init__(self, coro) -> None:
        self.cancelled = False
        self._coro = coro
        coro.close()

    def cancel(self) -> None:
        self.cancelled = True


class FakeTransport:
    def __init__(self, responses=None) -> None:
        self.responses = list(responses or [])
        self.sent = []
        self.connected = False
        self.closed = False
        self.connect_calls = []
        self.recv_calls = []

    def is_connected(self) -> bool:
        return self.connected

    async def connect(self, host: str, port: int, timeout: float = 10.0) -> None:
        self.connected = True
        self.connect_calls.append((host, port, timeout))

    async def close(self) -> None:
        self.connected = False
        self.closed = True

    async def send(self, data: bytes) -> None:
        self.sent.append(data)

    async def recv_exactly(self, n: int) -> bytes:
        self.recv_calls.append(n)
        return self.responses.pop(0)

    async def receive(self, count: int) -> bytes:
        return await self.recv_exactly(count)


class FakeStream:
    def __init__(self) -> None:
        self.sent = []
        self.to_read = []

    async def send(self, packet: Packet) -> None:
        self.sent.append(packet)

    async def read(self) -> Packet:
        value = self.to_read.pop(0)
        if isinstance(value, Exception):
            raise value
        return value


class FakePipeline:
    def __init__(self, values=None) -> None:
        self.values = list(values or [])

    async def process(self, session, packet):
        if self.values:
            value = self.values.pop(0)
            if callable(value):
                return value(session, packet)
            return value
        return packet


class FakeDispatcher:
    def __init__(self) -> None:
        self.calls = []

    async def dispatch(self, session, packet) -> None:
        self.calls.append((session, packet))


def test_middleware_base_and_pipeline() -> None:
    with pytest.raises(NotImplementedError):
        run(Middleware.process(object(), object(), object()))

    class AddOne:
        async def process(self, session, packet):
            return Packet(packet.opcode + 1, packet.payload + b"x")

    class Drop:
        async def process(self, session, packet):
            return None

    pipeline = PacketPipeline()
    pipeline.add(AddOne())
    pipeline.add(AddOne())
    out = run(pipeline.process(object(), Packet(1, b"a")))
    assert out == Packet(3, b"axx")

    pipeline = PacketPipeline()
    pipeline.add(Drop())
    pipeline.add(AddOne())
    out = run(pipeline.process(object(), Packet(1, b"a")))
    assert out is None


def test_packet_debugger(capsys: pytest.CaptureFixture[str]) -> None:
    debugger = PacketDebugger(preview_limit=2)
    pkt_empty = Packet(1, b"")
    assert run(debugger.process(object(), pkt_empty)) == pkt_empty
    out = capsys.readouterr().out
    assert "payload: <empty>" in out

    pkt = Packet(2, b"\x01\x02ab")
    assert run(debugger.process(object(), pkt)) == pkt
    out = capsys.readouterr().out
    assert "opcode: 2" in out
    assert "u8 preview:" in out
    assert "u16 preview:" in out
    assert "ascii preview:" in out


def test_packet_stream_read_send_and_validations() -> None:
    header = struct.pack("<H", 3)
    body = b"\x05ab"
    transport = FakeTransport([header, body])
    stream = PacketStream(transport, endian="<", max_body_len=10)

    pkt = run(stream.read())
    assert pkt == Packet(5, b"ab")
    assert transport.recv_calls == [2, 3]

    run(stream.send(pkt))
    run(stream.send(7, b"zz"))
    assert len(transport.sent) == 2

    transport.responses = [header]
    assert run(stream._read_header()) == header
    assert stream._parse_body_len(header) == 3
    transport.responses = [b"abc"]
    assert run(stream._read_body(3)) == b"abc"

    with pytest.raises(ValueError):
        stream._validate_body_len(0)
    with pytest.raises(ValueError):
        stream._validate_body_len(999)


def test_itransport_protocol_methods_raise() -> None:
    with pytest.raises(NotImplementedError):
        ITransport.is_connected(object())
    with pytest.raises(NotImplementedError):
        run(ITransport.connect(object(), "h", 1))
    with pytest.raises(NotImplementedError):
        run(ITransport.close(object()))
    with pytest.raises(NotImplementedError):
        run(ITransport.send(object(), b"x"))
    with pytest.raises(NotImplementedError):
        run(ITransport.recv_exactly(object(), 1))
    with pytest.raises(NotImplementedError):
        run(ITransport.receive(object(), 1))


def test_tcp_transport_connect_send_recv_and_close(monkeypatch: pytest.MonkeyPatch) -> None:
    class Reader:
        def __init__(self, result=b"ok", exc=None) -> None:
            self.result = result
            self.exc = exc

        async def readexactly(self, n: int) -> bytes:
            if self.exc:
                raise self.exc
            return self.result

    class Writer:
        def __init__(self, fail_drain=False, fail_wait_closed=False) -> None:
            self.fail_drain = fail_drain
            self.fail_wait_closed = fail_wait_closed
            self.data = []
            self.closed = False

        def write(self, data: bytes) -> None:
            self.data.append(data)

        async def drain(self) -> None:
            if self.fail_drain:
                raise RuntimeError("drain failed")

        def close(self) -> None:
            self.closed = True

        async def wait_closed(self) -> None:
            if self.fail_wait_closed:
                raise OSError("close failed")

    transport = TcpTransport()
    with pytest.raises(ValueError):
        run(transport.connect("x", 0))

    reader = Reader()
    writer = Writer()

    async def open_connection(host, port):
        return reader, writer

    async def wait_for(awaitable, timeout):
        return await awaitable

    monkeypatch.setattr(asyncio, "open_connection", open_connection)
    monkeypatch.setattr(asyncio, "wait_for", wait_for)

    run(transport.connect("localhost", 1234, timeout=0))
    assert transport.is_connected() is True
    run(transport.connect("localhost", 1234, timeout=1.5))
    assert transport.is_connected() is True

    run(transport.send(b"abc"))
    assert writer.data == [b"abc"]

    transport._reader = Reader(result=b"xyz")
    assert run(transport.recv_exactly(3)) == b"xyz"
    assert run(transport.receive(3)) == b"xyz"
    assert run(transport.recv_exactly(0)) == b""

    with pytest.raises(ValueError):
        run(transport.recv_exactly(-1))

    run(transport.close())
    assert transport.is_connected() is False

    transport._writer = Writer(fail_wait_closed=True)
    run(transport.close())  # OSError path
    assert transport.is_connected() is False


def test_tcp_transport_error_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    class Reader:
        def __init__(self, exc=None) -> None:
            self.exc = exc

        async def readexactly(self, n: int) -> bytes:
            if self.exc:
                raise self.exc
            return b"x" * n

    class Writer:
        def __init__(self, fail_drain=False) -> None:
            self.fail_drain = fail_drain

        def write(self, data: bytes) -> None:
            return None

        async def drain(self) -> None:
            if self.fail_drain:
                raise RuntimeError("send fail")

        def close(self) -> None:
            return None

        async def wait_closed(self) -> None:
            return None

    transport = TcpTransport()
    with pytest.raises(ConnectionError):
        run(transport.send(b"x"))

    transport._writer = Writer(fail_drain=True)
    with pytest.raises(TransportConnectionError):
        run(transport.send(b"x"))

    transport._reader = None
    with pytest.raises(ConnectionError):
        run(transport.recv_exactly(1))

    transport._reader = Reader(exc=asyncio.IncompleteReadError(partial=b"", expected=2))
    transport._writer = Writer()
    with pytest.raises(TransportConnectionError):
        run(transport.recv_exactly(2))

    transport._reader = Reader(exc=RuntimeError("boom"))
    transport._writer = Writer()
    with pytest.raises(TransportConnectionError):
        run(transport.recv_exactly(2))

    async def broken_open_connection(host, port):
        raise RuntimeError("nope")

    monkeypatch.setattr(asyncio, "open_connection", broken_open_connection)
    with pytest.raises(TransportConnectionError):
        run(transport.connect("localhost", 9999, timeout=0))


def test_session_connect_close_send_receive(monkeypatch: pytest.MonkeyPatch) -> None:
    transport = FakeTransport()
    stream = FakeStream()
    pipeline = FakePipeline()
    dispatcher = FakeDispatcher()
    session = Session(transport, stream, dispatcher, pipeline)

    monkeypatch.setattr(asyncio, "create_task", lambda coro: DummyTask(coro))
    run(session.connect("localhost", 7777))
    assert transport.connect_calls
    assert session._running is True
    assert session._reader_task is not None
    assert session._writer_task is not None

    packet = Packet(1, b"x")
    run(session.send(packet))
    assert run(session._send_queue.get()) == packet

    session._received_packets.put_nowait(packet)
    assert run(session.receive()) == packet
    session._received_packets.put_nowait(packet)
    assert run(session.receive(timeout=0.1)) == packet

    run(session.close())
    assert transport.closed is True
    assert session._running is False
    assert session._reader_task.cancelled is True
    assert session._writer_task.cancelled is True


def test_session_write_loop_paths() -> None:
    transport = FakeTransport()
    stream = FakeStream()
    pipeline = FakePipeline()
    dispatcher = FakeDispatcher()
    session = Session(transport, stream, dispatcher, pipeline)

    async def send_once(packet: Packet) -> None:
        stream.sent.append(packet)
        session._running = False

    stream.send = send_once
    session._running = True
    pkt = Packet(7, b"z")
    session._send_queue.put_nowait(pkt)
    run(session._write_loop())
    assert stream.sent == [pkt]

    async def bad_send(packet: Packet) -> None:
        raise OSError("send error")

    closed = {"called": False}

    async def fake_close() -> None:
        closed["called"] = True
        session._running = False

    stream.send = bad_send
    session.close = fake_close
    session._running = True
    session._send_queue.put_nowait(pkt)
    run(session._write_loop())
    assert closed["called"] is True


def test_session_read_loop_paths() -> None:
    transport = FakeTransport()
    stream = FakeStream()
    dispatcher = FakeDispatcher()
    pipeline = FakePipeline()
    session = Session(transport, stream, dispatcher, pipeline)

    pkt = Packet(9, b"a")

    async def read_once() -> Packet:
        session._running = False
        return pkt

    stream.read = read_once
    session._running = True
    run(session._read_loop())
    assert run(session._received_packets.get()) == pkt
    assert dispatcher.calls == [(session, pkt)]

    # packet dropped by middleware
    stream = FakeStream()
    dispatcher = FakeDispatcher()
    pipeline = FakePipeline(values=[None])
    session = Session(transport, stream, dispatcher, pipeline)

    async def read_drop() -> Packet:
        return pkt

    async def drop_process(s, p):
        session._running = False
        return None

    stream.read = read_drop
    pipeline.process = drop_process
    session._running = True
    run(session._read_loop())
    assert session._received_packets.empty()
    assert dispatcher.calls == []

    # exception path
    session = Session(transport, stream, dispatcher, pipeline)

    async def bad_read() -> Packet:
        raise OSError("read fail")

    closed = {"called": False}

    async def fake_close() -> None:
        closed["called"] = True
        session._running = False

    session.close = fake_close
    stream.read = bad_read
    session._running = True
    run(session._read_loop())
    assert closed["called"] is True


def test_network_package_export() -> None:
    assert SessionExport is Session
