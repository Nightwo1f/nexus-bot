"""
ByteReader

Utility class for sequentially reading primitive data types from a
binary buffer.

The reader wraps a ``memoryview`` of the provided data to avoid
unnecessary memory copies and keeps track of the current read position.

It is designed for binary network protocols such as game packets,
file formats, or custom serialization formats.

Supported primitive reads include:

    - unsigned integers (u8, u16, u32)
    - signed integers (i8, i16, i32)
    - raw byte sequences
    - strings
    - peek operations
    - skipping bytes

Example
-------
>>> data = b"\x01\x00\x05hello"
>>> reader = ByteReader(data)

>>> opcode = reader.read_uint8()
>>> length = reader.read_uint16()
>>> text = reader.read_bytes(length)

Notes
-----
The reader advances the internal cursor after each read operation.

If there are not enough bytes remaining in the buffer, a ``ValueError``
is raised.
"""

import struct
from typing import Union

Buffer = Union[bytes, bytearray, memoryview]


class ByteReader:
    """
    Sequential binary buffer reader.

    Parameters
    ----------
    data : bytes
        Raw binary buffer to read from.

    endian : str
        Endianness used when unpacking numeric values.

        Supported values:
        ">"  -> big endian (network order)
        "<"  -> little endian

    Attributes
    ----------
    _buffer : memoryview
        Internal view of the binary data.

    _position : int
        Current read position inside the buffer.

    _endian : str
        Endianness used for struct unpacking.
    """

    def __init__(self, data: bytes, endian: str = ">") -> None:
        self._buffer = memoryview(data)
        self._position = 0
        self._endian = endian

    @property
    def position(self) -> int:
        """
        Current read position in the buffer.

        Returns
        -------
        int
            Current cursor position.
        """
        return self._position

    @property
    def remaining(self) -> int:
        """
        Number of unread bytes remaining in the buffer.

        Returns
        -------
        int
            Remaining unread bytes.
        """
        return len(self._buffer) - self._position

    def _require(self, size: int) -> None:
        """
        Ensures that at least ``size`` bytes are available to read.

        Parameters
        ----------
        size : int
            Number of bytes required.

        Raises
        ------
        ValueError
            If the buffer does not contain enough remaining bytes.
        """
        if self.remaining < size:
            msg = "Not enough bytes remaining."
            raise ValueError(msg)

    def read_uint8(self) -> int:
        """
        Reads an unsigned 8-bit integer.

        Returns
        -------
        int
            Value between 0 and 255.
        """
        self._require(1)
        value = self._buffer[self._position]
        self._position += 1
        return int(value)

    def read_i8(self) -> int:
        """
        Reads a signed 8-bit integer.

        Returns
        -------
        int
            Value between -128 and 127.
        """
        self._require(1)
        value = struct.unpack_from(self._endian + "b", self._buffer, self._position)[0]
        self._position += 1
        return value

    def read_uint16(self) -> int:
        """
        Reads an unsigned 16-bit integer.

        Returns
        -------
        int
            Value between 0 and 65535.
        """
        self._require(2)
        value = struct.unpack_from(self._endian + "H", self._buffer, self._position)[0]
        self._position += 2
        return value

    def read_i16(self) -> int:
        """
        Reads a signed 16-bit integer.

        Returns
        -------
        int
            Value between -32768 and 32767.
        """
        self._require(2)
        value = struct.unpack_from(self._endian + "h", self._buffer, self._position)[0]
        self._position += 2
        return value

    def read_uint32(self) -> int:
        """
        Reads an unsigned 32-bit integer.

        Returns
        -------
        int
            Value between 0 and 4294967295.
        """
        self._require(4)
        value = struct.unpack_from(self._endian + "I", self._buffer, self._position)[0]
        self._position += 4
        return value

    def read_i32(self) -> int:
        """
        Reads a signed 32-bit integer.

        Returns
        -------
        int
            Signed integer value.
        """
        self._require(4)
        value = struct.unpack_from(self._endian + "i", self._buffer, self._position)[0]
        self._position += 4
        return value

    def read_bytes(self, length: int) -> bytes:
        """
        Reads a raw sequence of bytes.

        Parameters
        ----------
        length : int
            Number of bytes to read.

        Returns
        -------
        bytes
            Byte sequence extracted from the buffer.

        Raises
        ------
        ValueError
            If ``length`` is negative or exceeds remaining bytes.
        """
        if length < 0:
            msg = "length must be >= 0"
            raise ValueError(msg)

        self._require(length)
        start = self._position
        end = start + length
        self._position = end
        return self._buffer[start:end].tobytes()

    def read_string(self, encoding: str = "utf-8") -> str:
        """
        Reads a TibiaME protocol string.

        Format:

            if len <= 0xFE
                [u8 len] + data

            if len > 0xFE
                [0xFF] + [u16 len] + data
        """

        length = self.read_uint8()

        if length == 0xFF:
            length = self.read_uint16()

        raw = self.read_bytes(length)
        return raw.decode(encoding, errors="ignore")

    def skip(self, length: int) -> None:
        """
        Skips a number of bytes without reading them.

        Parameters
        ----------
        length : int
            Number of bytes to skip.

        Raises
        ------
        ValueError
            If ``length`` is negative or exceeds remaining bytes.
        """
        if length < 0:
            msg = "length must be >= 0"
            raise ValueError(msg)

        self._require(length)
        self._position += length

    def peak_uint8(self) -> int:
        """
        Reads an unsigned 8-bit integer without advancing the cursor.

        Returns
        -------
        int
            The next byte value in the buffer.
        """
        self._require(1)
        return int(self._buffer[self._position])
