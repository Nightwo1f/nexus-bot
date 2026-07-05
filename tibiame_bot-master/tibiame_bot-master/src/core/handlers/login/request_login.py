

from core.handlers.base_handler import PacketHandler
from core.network.session import Session
from core.protocol.packet import Packet


class RequestLogin(PacketHandler):
    OPCODE = 3

    async def handle(self, session: Session, packet: Packet) -> None:
        print("Redirect packet (100) received. Login process should transition to game server.")
