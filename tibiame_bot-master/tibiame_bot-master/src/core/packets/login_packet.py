from dataclasses import dataclass
from typing import Iterable

from core.protocol.byte_writer import ByteWriter
from core.protocol.packet import Packet


@dataclass(frozen=True)
class PackEntry:
    pack_id: int
    version: int
    priority: int = 0


class LoginPacket(Packet):

    OPCODE = 13

    PASSWORD_XOR_KEY = "HACKINGISCRIME"  # noqa: S105

    @staticmethod
    def _xor(data: bytes, key: str) -> bytes:

        key_bytes = key.encode("utf-8")

        raw = bytearray(data)

        for i in range(len(raw)):
            raw[i] ^= key_bytes[i % len(key_bytes)]

        return bytes(raw)

    @staticmethod
    def _write_serialized_bytes(writer: ByteWriter, raw: bytes) -> None:
        size = len(raw)

        if size > 0xFFFF:
            msg = "string payload exceeds 65535 bytes"
            raise ValueError(msg)

        if size <= 0xFE:
            writer.u8(size)
        else:
            writer.u8(0xFF)
            writer.u16(size)

        writer.raw(raw)

    @classmethod
    def create(
        cls,
        *,
        nickname: str,
        password: str,
        device_id: str,
        client_int_1: int,
        client_int_2: int,
        pack_entries: Iterable[PackEntry] | None = None,
    ) -> "LoginPacket":

        if not 0 <= client_int_1 <= 0xFFFFFFFF:
            msg = "client_int_1 must fit unsigned 32-bit"
            raise ValueError(msg)

        if not 0 <= client_int_2 <= 0xFFFFFFFF:
            msg = "client_int_2 must fit unsigned 32-bit"
            raise ValueError(msg)

        selected = list(
            pack_entries
            or [
                PackEntry(pack_id=2, version=63, priority=1),
                PackEntry(pack_id=3, version=74, priority=0),
            ]
        )[:255]

        max_priority = max((entry.priority for entry in selected), default=0)

        w = ByteWriter(endian="<")

        w.string(device_id, max_chars=50)
        w.u32(client_int_1)
        w.u32(client_int_2)
        w.string(nickname, max_chars=10)

        enc = cls._xor(password.encode("utf-8"), cls.PASSWORD_XOR_KEY)[:10]
        cls._write_serialized_bytes(w, enc)

        w.u8(len(selected))

        for entry in selected:
            if not 0 <= entry.pack_id <= 0xFF:
                msg = "pack_id must fit unsigned 8-bit"
                raise ValueError(msg)
            if not 0 <= entry.version <= 0xFFFF:
                msg = "pack version must fit unsigned 16-bit"
                raise ValueError(msg)
            if not 0 <= entry.priority <= 0xFF:
                msg = "pack priority must fit unsigned 8-bit"
                raise ValueError(msg)

            w.u8(entry.pack_id)
            w.u16(entry.version)

        w.u8(max_priority)

        payload = w.build()

        return cls(cls.OPCODE, payload)
