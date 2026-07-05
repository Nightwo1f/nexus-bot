from core.handlers.base_handler import PacketHandler
from core.network.session import Session
from core.protocol.byte_reader import ByteReader
from core.protocol.packet import Packet


class LoginErrorHandler(PacketHandler):
    OPCODE = 11

    async def handle(self, session: Session, packet: Packet) -> None:
        error_text = self._decode_login_error_text(packet)
        if error_text:
            print("Login error:", error_text)
        else:
            print("Login error packet received.")

    @staticmethod
    def _decode_login_error_text(packet: Packet) -> str:
        read = ByteReader(packet.payload, endian="<")

        if read.remaining < 4:
            return ""

        read.skip(2)
        return read.read_string()
