from __future__ import annotations


class PacketReader:
    def __init__(self, data: bytes | bytearray | memoryview) -> None:
        self._data = memoryview(bytes(data))
        self._offset = 0

    def read_u8(self) -> int:
        self._require(1)
        value = self._data[self._offset]
        self._offset += 1
        return int(value)

    def read_u16(self) -> int:
        return int.from_bytes(self._read(2), "little")

    def read_i32(self) -> int:
        return int.from_bytes(self._read(4), "little", signed=True)

    def read_i64(self) -> int:
        return int.from_bytes(self._read(8), "little", signed=True)

    def read_string(self) -> str:
        length = self.read_u8()
        if length == 0:
            return ""
        if length == 0xFF:
            length = self.read_u16()
            if length == 0:
                return ""
        return self._read(length).decode("iso-8859-1")

    def read_utf_string(self) -> str:
        length = self.read_u8()
        if length == 0:
            return ""
        if length == 0xFF:
            length = self.read_u16()
            if length == 0:
                return ""
        raw = self._read(length)
        try:
            return raw.decode("utf-8")
        except UnicodeDecodeError:
            return raw.decode("iso-8859-1")

    def skip(self, count: int) -> None:
        if count < 0:
            raise ValueError("skip count cannot be negative")
        self._require(count)
        self._offset += count

    def remaining(self) -> int:
        return len(self._data) - self._offset

    def _read(self, size: int) -> bytes:
        self._require(size)
        start = self._offset
        self._offset += size
        return self._data[start:self._offset].tobytes()

    def _require(self, size: int) -> None:
        if self.remaining() < size:
            raise EOFError(f"packet underflow: need {size} bytes, have {self.remaining()}")
