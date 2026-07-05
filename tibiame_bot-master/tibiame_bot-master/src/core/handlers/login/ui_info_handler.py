from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.network.session import Session
    from core.protocol.packet import Packet


from core.handlers.base_handler import PacketHandler
from core.protocol.byte_reader import ByteReader


class UiInfoHandler(PacketHandler):
    OPCODE = 51

    async def handle(self, session: Session, packet: Packet) -> None:
        reader = ByteReader(packet.payload, endian="<")

        if reader.remaining < 7:
            print("opcode 51 inválido: payload curto")
            return

        ui_pack_version = reader.read_uint16()
        ui_pack_total_size = reader.read_uint32()
        ui_pack_name = reader.read_string()

        print("ui pack version:", ui_pack_version)
        print("ui pack total size:", ui_pack_total_size)
        print("ui pack name:", ui_pack_name)
        print("UiInfo packet received.")
