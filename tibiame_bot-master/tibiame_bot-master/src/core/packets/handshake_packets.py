from __future__ import annotations

from core.packets.login_packet import PackEntry
from core.protocol.byte_writer import ByteWriter
from core.protocol.packet import Packet


class LoginServerHelloPacket(Packet):
    """
    Step1 packet sent to the login endpoint.

    This is the extended web-client handshake variant that precedes step2/3/4.
    """

    OPCODE = 3

    @classmethod
    def create(cls) -> LoginServerHelloPacket:
        writer = ByteWriter(endian="<")

        writer.u8(33)
        writer.string("en")
        writer.u8(10)
        writer.u16(232)
        writer.u8(0)
        writer.string("web client")
        writer.u16(0x8016)
        writer.u8(2)
        writer.u8(104)
        writer.u8(1)
        writer.u16(96)
        writer.u16(21)

        return cls(cls.OPCODE, writer.build())


class HandshakeStep2Packet(Packet):
    """Step2 packet: requests pack metadata from login endpoint."""

    OPCODE = 19

    @classmethod
    def create(cls) -> HandshakeStep2Packet:
        writer = ByteWriter(endian="<")
        writer.u8(37)
        writer.u8(1)
        return cls(cls.OPCODE, writer.build())


class HandshakeStep3Packet(Packet):
    """Step3 packet: continue handshake before world selection."""

    OPCODE = 18

    @classmethod
    def create(cls) -> HandshakeStep3Packet:
        writer = ByteWriter(endian="<")
        writer.u8(12)
        writer.u8(17)
        writer.u8(1)
        writer.u8(0)
        return cls(cls.OPCODE, writer.build())


class SelectWorldPacket(Packet):
    """Step4 packet: selects world id on login endpoint."""

    OPCODE = 16

    @classmethod
    def create(cls, world_id: int) -> SelectWorldPacket:
        if not 0 <= world_id <= 0xFFFF:
            msg = "world_id must fit unsigned 16-bit."
            raise ValueError(msg)

        writer = ByteWriter(endian="<")
        writer.u16(world_id)
        return cls(cls.OPCODE, writer.build())


def parse_redirect_endpoint(packet: Packet) -> tuple[str, int]:
    if packet.opcode != 100:
        msg = f"Expected redirect opcode 100, got {packet.opcode}"
        raise ValueError(msg)

    payload = packet.payload
    if len(payload) < 6:
        msg = "Redirect payload too short."
        raise ValueError(msg)

    host_len = payload[3]
    host_start = 4
    host_end = host_start + host_len
    if len(payload) < host_end + 2:
        msg = "Redirect payload missing host/port."
        raise ValueError(msg)

    host = payload[host_start:host_end].decode("ascii", errors="strict")
    port = payload[host_end] + (payload[host_end + 1] << 8)
    return host, port


def parse_pack_entries(step2_packet: Packet) -> list[PackEntry]:
    if step2_packet.opcode != 50:
        msg = f"Expected step2 opcode 50, got {step2_packet.opcode}"
        raise ValueError(msg)

    payload = step2_packet.payload
    if not payload:
        return []

    entries: list[PackEntry] = []
    idx = 0

    count_a = payload[idx]
    idx += 1
    for _ in range(count_a):
        if len(payload) < idx + 8:
            break
        pack_id = payload[idx]
        version = payload[idx + 1] + (payload[idx + 2] << 8)
        priority = payload[idx + 7]
        entries.append(PackEntry(pack_id=pack_id, version=version, priority=priority))
        idx += 8

    if len(payload) > idx:
        count_b = payload[idx]
        idx += 1
        if count_b > 0 and len(payload) >= idx + 2:
            version = payload[idx] + (payload[idx + 1] << 8)
            entries.append(PackEntry(pack_id=3, version=version, priority=0))

    return entries
