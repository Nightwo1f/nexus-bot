from __future__ import annotations

from typing import TYPE_CHECKING

from core.pipeline.middleware import Middleware
from core.protocol.byte_reader import ByteReader

if TYPE_CHECKING:
    from core.network.session import Session
    from core.protocol.packet import Packet


class PacketDebugger(Middleware):
    """
    Middleware used to inspect packets during development.

    Displays packet opcode and multiple payload interpretations
    useful for protocol reverse engineering.
    """

    def __init__(self, preview_limit: int = 16) -> None:

        self._limit = preview_limit

    async def process(self, session: Session, packet: Packet) -> Packet | None:

        payload = packet.payload

        print("\n=== PACKET DEBUG ===")

        print("opcode:", packet.opcode)
        print("payload_len:", len(payload))

        if not payload:
            print("payload: <empty>")
            return packet

        print("hex:", payload.hex())

        # u8 preview
        u8_preview = list(payload[: self._limit])
        print("u8 preview:", u8_preview)

        # u16 preview
        reader = ByteReader(payload)
        u16_preview = []

        while reader.remaining >= 2 and len(u16_preview) < self._limit:
            u16_preview.append(reader.read_uint16())

        print("u16 preview:", u16_preview)

        # ASCII preview
        ascii_preview = payload.decode("ascii", errors="ignore")
        print("ascii preview:", ascii_preview[: self._limit])

        print("====================\n")

        return packet
