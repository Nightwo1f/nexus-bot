import struct

import pytest

from core.protocol import (
    ByteReader,
    ByteWriter,
    ClientOpcode,
    LoginOpcode,
    Packet,
    PacketFactory,
    PacketMeta,
    PacketRegistry,
    ServerOpcode,
)


def test_byte_reader_reads_all_primitives() -> None:
    payload = struct.pack("<BbHhIi", 255, -5, 513, -123, 123456, -456789)
    reader = ByteReader(payload, endian="<")

    assert reader.read_uint8() == 255
    assert reader.read_i8() == -5
    assert reader.read_uint16() == 513
    assert reader.read_i16() == -123
    assert reader.read_uint32() == 123456
    assert reader.read_i32() == -456789
    assert reader.remaining == 0


def test_byte_reader_read_bytes_and_strings() -> None:
    small = b"\x03abc"
    long_raw = b"x" * 300
    long = b"\xff" + struct.pack("<H", 300) + long_raw
    reader = ByteReader(small + long, endian="<")

    assert reader.read_string() == "abc"
    assert reader.read_string() == "x" * 300
    assert reader.remaining == 0


def test_byte_reader_skip_peek_and_errors() -> None:
    reader = ByteReader(b"\x01\x02\x03", endian="<")
    assert reader.peak_uint8() == 1
    reader.skip(1)
    assert reader.position == 1
    assert reader.read_bytes(2) == b"\x02\x03"

    with pytest.raises(ValueError):
        reader.read_uint8()
    with pytest.raises(ValueError):
        ByteReader(b"\x01").read_uint16()
    with pytest.raises(ValueError):
        ByteReader(b"\x01").read_bytes(-1)
    with pytest.raises(ValueError):
        ByteReader(b"\x01").skip(-1)
    with pytest.raises(ValueError):
        ByteReader(b"").peak_uint8()


def test_byte_writer_happy_paths() -> None:
    writer = ByteWriter("<")
    clone = (
        writer.u8(1)
        .i8(-1)
        .u16(500)
        .i16(-7)
        .u32(99999)
        .i32(-99999)
        .raw(b"ab")
        .string("xy")
        .write_bool(value=True)
        .write_bool(value=False)
        .clone()
    )

    assert writer.size() == clone.size()
    assert writer.hex() == clone.hex()
    data = writer.build(clear=True)
    assert isinstance(data, bytes)
    assert writer.size() == 0
    assert clone.to_bytes() == data
    assert clone.clear().size() == 0


def test_byte_writer_validation_and_string_limits() -> None:
    with pytest.raises(ValueError):
        ByteWriter("?")

    writer = ByteWriter("<")
    with pytest.raises(ValueError):
        writer.u8(256)
    with pytest.raises(ValueError):
        writer.u16(-1)
    with pytest.raises(ValueError):
        writer.u32(1 << 40)
    with pytest.raises(ValueError):
        writer.string("a" * 70000)

    writer = ByteWriter("<", validate=False)
    writer.u8(300)
    assert writer.build() == bytes([300 & 0xFF])

    long_txt = "a" * 300
    long_data = ByteWriter("<").string(long_txt).build()
    assert long_data[0] == 0xFF
    assert struct.unpack_from("<H", long_data, 1)[0] == 300

    truncated = ByteWriter("<").string("abcdef", max_chars=3).build()
    assert truncated == b"\x03abc"


def test_packet_encode_decode_and_reader() -> None:
    packet = Packet(10, b"abc")
    frame = packet.encode(endian="<")

    decoded = Packet.decode_frame(frame, endian="<")
    assert decoded.opcode == 10
    assert decoded.payload == b"abc"
    assert decoded.payload_reader(endian="<").read_bytes(3) == b"abc"


def test_packet_decode_error_paths() -> None:
    with pytest.raises(ValueError):
        Packet(999, b"").encode()
    with pytest.raises(ValueError):
        Packet.decode(b"\x00", b"\x01")
    with pytest.raises(ValueError):
        Packet.decode(b"\x02\x00", b"\x01", strict=True)
    with pytest.raises(ValueError):
        Packet.decode(b"\x00\x00", b"")
    with pytest.raises(ValueError):
        Packet.decode_frame(b"\x00")
    with pytest.raises(ValueError):
        Packet._validate_opcode_u8(-1)


def test_packet_decode_non_strict_and_from_payload_writer() -> None:
    decoded = Packet.decode(b"\x05\x00", b"\x01a", strict=False, endian="<")
    assert decoded.opcode == 1
    assert decoded.payload == b"a"

    writer = ByteWriter("<").u8(9).u8(8)
    p1 = Packet.from_payload_writer(7, writer, clear=True)
    assert p1.payload == b"\x09\x08"
    assert writer.size() == 0

    writer.u8(1)
    p2 = Packet.from_payload_writer(7, writer, clear=False)
    assert p2.payload == b"\x01"
    assert writer.size() == 1


def test_packet_registry_and_factory() -> None:
    registry = PacketRegistry()
    assert registry.has(10) is False
    assert registry.get(10) is None

    registry.register(10, lambda payload: Packet(10, payload))
    assert registry.has(10) is True
    assert isinstance(registry.get(10), object)

    with pytest.raises(ValueError):
        registry.register(10, lambda payload: Packet(10, payload))

    factory = PacketFactory(registry)
    assert factory.create(99, b"x") == Packet(99, b"x")
    assert factory.create(10, b"y") == Packet(10, b"y")

    frame = Packet(10, b"z").encode(endian="<")
    assert factory.decode(frame) == Packet(10, b"z")

    global_one = PacketRegistry.global_registry()
    global_two = PacketRegistry.global_registry()
    assert global_one is global_two


def test_packet_meta_registers_and_skips(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[int, object]] = []

    class FakeRegistry:
        def register(self, opcode: int, constructor: object) -> None:
            calls.append((opcode, constructor))

    monkeypatch.setattr(
        "core.protocol.packet_registry.PacketRegistry.global_registry",
        lambda: FakeRegistry(),
    )

    class AutoPacket(metaclass=PacketMeta):
        OPCODE = 77

        def __init__(self, payload: bytes) -> None:
            self.payload = payload

    assert calls and calls[0][0] == 77
    constructor = calls[0][1]
    built = constructor(b"hello")
    assert isinstance(built, AutoPacket)
    assert built.payload == b"hello"

    before = len(calls)

    class NoOpcodePacket(metaclass=PacketMeta):
        pass

    assert len(calls) == before
    assert NoOpcodePacket.__name__ == "NoOpcodePacket"


def test_enums_and_protocol_exports() -> None:
    assert ClientOpcode.CLIENT_READY == 14
    assert LoginOpcode.SET_CONNECTION == 3
    assert ServerOpcode.QUIT_GAME == 255

    import core.protocol as protocol_pkg

    for name in protocol_pkg.__all__:
        assert hasattr(protocol_pkg, name)
