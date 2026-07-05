from core.protocol.packet import Packet


class ClientReadyPacket(Packet):

    OPCODE = 14

    @classmethod
    def create(cls) -> "ClientReadyPacket":
        return cls(cls.OPCODE, b"")
