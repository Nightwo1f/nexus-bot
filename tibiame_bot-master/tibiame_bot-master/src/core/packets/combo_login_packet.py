from __future__ import annotations

from core.protocol.packet import Packet


class ComboLoginPacket(Packet):
    """
    Wrapper packet that sends msg3 + msg13 in a single frame.

    The resulting frame is encoded by Packet.encode() as:
    [u16 len][opcode=3][hello_payload][opcode=13][login_payload]
    """

    OPCODE = 3

    @classmethod
    def create(cls, *, hello_packet: Packet, login_packet: Packet) -> ComboLoginPacket:
        if hello_packet.opcode != cls.OPCODE:
            msg = f"hello_packet opcode must be {cls.OPCODE}."
            raise ValueError(msg)

        payload = hello_packet.payload + bytes([login_packet.opcode]) + login_packet.payload
        return cls(cls.OPCODE, payload)
