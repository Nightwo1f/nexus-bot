from __future__ import annotations


class PacketWriter:
    def __init__(self) -> None:
        self._buffer = bytearray()

    def write_u8(self, value: int) -> None:
        if not 0 <= value <= 0xFF:
            raise ValueError(f"u8 out of range: {value}")
        self._buffer.append(value)

    def write_u16(self, value: int) -> None:
        if not 0 <= value <= 0xFFFF:
            raise ValueError(f"u16 out of range: {value}")
        self._buffer.extend(value.to_bytes(2, "little"))

    def write_i32(self, value: int) -> None:
        self._buffer.extend(value.to_bytes(4, "little", signed=True))

    def write_bytes(self, data: bytes | bytearray | memoryview) -> None:
        self._buffer.extend(bytes(data))

    def write_string(self, value: str | None) -> None:
        if value is None:
            self.write_u8(0)
            return

        encoded = value.encode("utf-8")
        if len(encoded) > 0xFF:
            raise ValueError("string is too long for JTME short string encoding")

        self.write_u8(len(encoded))
        self.write_bytes(encoded)

    def to_bytes(self) -> bytes:
        return bytes(self._buffer)
