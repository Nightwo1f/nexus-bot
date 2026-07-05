from core.handlers.base_handler import PacketHandler
from core.network.session import Session
from core.protocol.byte_reader import ByteReader
from core.protocol.packet import Packet


class ReceivePackList(PacketHandler):
    """
    Handler for opcode 50 (PackList).

    Payload:
    [countA][A...][countB][B...][countC][C...][countD][D...]
    """

    OPCODE = 50

    async def handle(self, session: Session, packet: Packet) -> None:
        reader = ByteReader(packet.payload, endian="<")

        try:
            # -----------------
            # GROUP A
            # -----------------
            count_a = reader.read_uint8()
            group_a = []

            for _ in range(count_a):
                pack_id = reader.read_uint8()
                version = reader.read_uint16()
                size = reader.read_uint32()
                priority = reader.read_uint8()

                group_a.append(
                    {
                        "pack_id": pack_id,
                        "version": version,
                        "size": size,
                        "priority": priority,
                    }
                )

            # -----------------
            # GROUP B
            # -----------------
            count_b = reader.read_uint8()
            group_b = []

            for _ in range(count_b):
                version = reader.read_uint16()
                size = reader.read_uint32()
                priority = reader.read_uint8()

                group_b.append(
                    {
                        "version": version,
                        "size": size,
                        "priority": priority,
                    }
                )

            # -----------------
            # GROUP C
            # -----------------
            count_c = reader.read_uint8()
            group_c = []

            for _ in range(count_c):
                version = reader.read_uint16()
                size = reader.read_uint32()
                language = reader.read_string()

                group_c.append(
                    {
                        "version": version,
                        "size": size,
                        "language": language,
                    }
                )

            # -----------------
            # GROUP D
            # -----------------
            count_d = reader.read_uint8()
            group_d = []

            for _ in range(count_d):
                version = reader.read_uint16()
                size = reader.read_uint32()
                audio_format = reader.read_string()

                group_d.append(
                    {
                        "version": version,
                        "size": size,
                        "audio_format": audio_format,
                    }
                )

        except ValueError as exc:
            print(f"opcode 50 inválido: {exc}")
            print("payload:", packet.payload.hex())
            return

        # -----------------
        # PRINT COMPLETO
        # -----------------

        print("\n=== PACK LIST ===")

        print(f"\nGroup A ({len(group_a)} packs)")
        for pack in group_a:
            print(
                f"  pack_id={pack['pack_id']} "
                f"version={pack['version']} "
                f"size={pack['size']} "
                f"priority={pack['priority']}"
            )

        print(f"\nGroup B ({len(group_b)} packs)")
        for pack in group_b:
            print(
                f"  version={pack['version']} "
                f"size={pack['size']} "
                f"priority={pack['priority']}"
            )

        print(f"\nGroup C ({len(group_c)} language packs)")
        for pack in group_c:
            print(
                f"  version={pack['version']} "
                f"size={pack['size']} "
                f"language={pack['language']}"
            )

        print(f"\nGroup D ({len(group_d)} audio packs)")
        for pack in group_d:
            print(
                f"  version={pack['version']} "
                f"size={pack['size']} "
                f"audio_format={pack['audio_format']}"
            )

        if reader.remaining != 0:
            print(f"\nopcode 50 com bytes extras no final: {reader.remaining}")
