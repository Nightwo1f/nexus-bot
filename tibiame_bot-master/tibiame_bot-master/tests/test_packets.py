import struct

import pytest

from core.packets.client_ready_packet import ClientReadyPacket
from core.packets.combo_login_packet import ComboLoginPacket
from core.packets.handshake_packets import (
    HandshakeStep2Packet,
    HandshakeStep3Packet,
    LoginServerHelloPacket,
    SelectWorldPacket,
    parse_pack_entries,
    parse_redirect_endpoint,
)
from core.packets.hello_packet import ClientHelloPacket
from core.packets.login_packet import LoginPacket, PackEntry
from core.protocol.byte_reader import ByteReader
from core.protocol.byte_writer import ByteWriter
from core.protocol.packet import Packet


def test_basic_packet_builders() -> None:
    ready = ClientReadyPacket.create()
    hello = ClientHelloPacket.create()
    step1 = LoginServerHelloPacket.create()
    step2 = HandshakeStep2Packet.create()
    step3 = HandshakeStep3Packet.create()

    assert ready.opcode == 14 and ready.payload == b""
    assert hello.opcode == 3 and len(hello.payload) > 0
    assert step1.opcode == 3 and len(step1.payload) > 0
    assert step2.payload == b"%\x01"
    assert step3.payload == b"\x0c\x11\x01\x00"


def test_select_world_packet() -> None:
    pkt = SelectWorldPacket.create(42)
    assert pkt.opcode == 16
    assert pkt.payload == struct.pack("<H", 42)

    with pytest.raises(ValueError):
        SelectWorldPacket.create(-1)
    with pytest.raises(ValueError):
        SelectWorldPacket.create(70000)


def test_parse_redirect_endpoint() -> None:
    payload = b"\x00\x00\x00" + bytes([4]) + b"host" + struct.pack("<H", 9999)
    packet = Packet(100, payload)
    host, port = parse_redirect_endpoint(packet)
    assert host == "host"
    assert port == 9999

    with pytest.raises(ValueError):
        parse_redirect_endpoint(Packet(99, payload))
    with pytest.raises(ValueError):
        parse_redirect_endpoint(Packet(100, b"\x00"))
    with pytest.raises(ValueError):
        parse_redirect_endpoint(Packet(100, b"\x00\x00\x00\x05abc"))


def test_parse_pack_entries() -> None:
    payload = bytearray()
    payload.append(1)  # count_a
    payload.append(2)  # pack_id
    payload.extend(struct.pack("<H", 0x1234))
    payload.extend(struct.pack("<I", 777))
    payload.append(9)  # priority
    payload.append(1)  # count_b
    payload.extend(struct.pack("<H", 0x0044))

    entries = parse_pack_entries(Packet(50, bytes(payload)))
    assert entries[0] == PackEntry(pack_id=2, version=0x1234, priority=9)
    assert entries[1] == PackEntry(pack_id=3, version=0x0044, priority=0)

    assert parse_pack_entries(Packet(50, b"")) == []

    truncated = bytes([1, 2, 0, 0])  # count_a with incomplete entry
    assert parse_pack_entries(Packet(50, truncated)) == [PackEntry(pack_id=3, version=0, priority=0)]

    only_a = bytes([0])  # no payload beyond count_a
    assert parse_pack_entries(Packet(50, only_a)) == []

    with pytest.raises(ValueError):
        parse_pack_entries(Packet(49, b"\x00"))


def test_combo_login_packet() -> None:
    hello = Packet(3, b"aa")
    login = Packet(13, b"bb")
    combo = ComboLoginPacket.create(hello_packet=hello, login_packet=login)
    assert combo.opcode == 3
    assert combo.payload == b"aa" + bytes([13]) + b"bb"

    with pytest.raises(ValueError):
        ComboLoginPacket.create(hello_packet=Packet(9, b""), login_packet=login)


def test_login_packet_internal_helpers() -> None:
    assert LoginPacket._xor(b"\x00\x01", "ab") == bytes([ord("a"), ord("b") ^ 1])

    writer = ByteWriter("<")
    LoginPacket._write_serialized_bytes(writer, b"abc")
    assert writer.build() == b"\x03abc"

    big = b"x" * 300
    writer = ByteWriter("<")
    LoginPacket._write_serialized_bytes(writer, big)
    built = writer.build()
    assert built[0] == 0xFF
    assert struct.unpack_from("<H", built, 1)[0] == 300
    assert built[3:] == big

    with pytest.raises(ValueError):
        LoginPacket._write_serialized_bytes(ByteWriter("<"), b"x" * 70000)


def test_login_packet_create_success_and_defaults() -> None:
    packet = LoginPacket.create(
        nickname="nickname_ignored_after10chars",
        password="secret",
        device_id="12345678901234567890123456789012345678901234567890EXTRA",
        client_int_1=100,
        client_int_2=200,
    )
    assert packet.opcode == 13
    assert len(packet.payload) > 0

    reader = ByteReader(packet.payload, endian="<")
    device_id = reader.read_string()
    assert len(device_id) <= 50
    assert reader.read_uint32() == 100
    assert reader.read_uint32() == 200
    nickname = reader.read_string()
    assert len(nickname) <= 10


def test_login_packet_create_validations() -> None:
    base_kwargs = {
        "nickname": "a",
        "password": "b",
        "device_id": "c",
        "client_int_1": 1,
        "client_int_2": 2,
    }

    with pytest.raises(ValueError):
        LoginPacket.create(**{**base_kwargs, "client_int_1": -1})
    with pytest.raises(ValueError):
        LoginPacket.create(**{**base_kwargs, "client_int_2": 1 << 40})

    with pytest.raises(ValueError):
        LoginPacket.create(
            **base_kwargs,
            pack_entries=[PackEntry(pack_id=999, version=1, priority=1)],
        )
    with pytest.raises(ValueError):
        LoginPacket.create(
            **base_kwargs,
            pack_entries=[PackEntry(pack_id=1, version=999999, priority=1)],
        )
    with pytest.raises(ValueError):
        LoginPacket.create(
            **base_kwargs,
            pack_entries=[PackEntry(pack_id=1, version=1, priority=999)],
        )


def test_login_packet_create_truncates_pack_entries_to_255() -> None:
    many_entries = [PackEntry(pack_id=1, version=i % 65535, priority=1) for i in range(300)]
    packet = LoginPacket.create(
        nickname="a",
        password="b",
        device_id="c",
        client_int_1=1,
        client_int_2=2,
        pack_entries=many_entries,
    )
    reader = ByteReader(packet.payload, endian="<")
    reader.read_string()  # device
    reader.read_uint32()
    reader.read_uint32()
    reader.read_string()  # nickname
    _ = reader.read_string()  # encrypted password
    count = reader.read_uint8()
    assert count == 255
