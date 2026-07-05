from core.protocol.byte_writer import ByteWriter
from core.protocol.packet import Packet


class ClientHelloPacket(Packet):

    OPCODE = 3

    @classmethod
    def create(cls) -> "ClientHelloPacket":

        writer = ByteWriter(endian="<")

        writer.u8(34)
        writer.string("en")
        writer.u8(10)
        writer.u16(232)
        writer.u8(0)
        writer.string("tablet_100")
        writer.u16(0)
        writer.u8(1)
        writer.u8(1)

        return cls(cls.OPCODE, writer.build())
