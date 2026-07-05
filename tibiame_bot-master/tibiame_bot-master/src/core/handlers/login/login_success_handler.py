from core.handlers.base_handler import PacketHandler
from core.network.session import Session
from core.packets.client_ready_packet import ClientReadyPacket
from core.protocol.packet import Packet


class LoginSuccessHandler(PacketHandler):
    OPCODE = 13

    async def handle(self, session: Session, packet: Packet) -> None:
        await session.send(ClientReadyPacket.create())
        print("ClientReady sent, waiting follow-up...")
