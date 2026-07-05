"""
ByteWriter

Binary serialization helper used to build packet payloads for the TibiaME protocol.

This class provides a fluent interface for writing primitive types into a
contiguous byte buffer. The internal buffer uses ``bytearray`` for efficient
incremental writes.

String serialization format used by the TibiaME protocol:

    If length <= 0xFE
        [u8 length] + data

    If length > 0xFE
        [0xFF] + [u16 length] + data

This allows encoding strings up to 65535 bytes.

Typical usage:

    writer = ByteWriter()
    writer.u8(1)
    writer.u16(300)
    writer.string("hello")

    payload = writer.build()

The resulting payload can then be wrapped into a Packet.
"""

from __future__ import annotations

import struct
from typing import Union

Buffer = Union[bytes, bytearray, memoryview]


class ByteWriter:
    """
    Binary writer used to build packet payloads.

    The writer appends values sequentially into an internal ``bytearray`` buffer.
    Numeric types are encoded using the configured endianness.

    Features
    --------
    • Efficient incremental writes using ``bytearray``
    • Configurable endianness
    • Optional unsigned integer validation
    • TibiaME protocol string serialization support
    • Fluent API for chained writes

    Example
    -------
    >>> writer = ByteWriter("<")
    >>> writer.u8(1).u16(500).string("hello")
    >>> data = writer.build()
    """

    def __init__(self, endian: str = "<", *, validate: bool = True) -> None:
        """
        Initialize a new ByteWriter.

        Parameters
        ----------
        endian:
            Byte order used for numeric serialization.

            Supported values:
                "<"  little-endian
                ">"  big-endian
                "!"  network byte order (big-endian)

        validate:
            If True, unsigned integer writes validate that the value
            fits within the specified bit range.

            If False, values are masked to the allowed bit size.
        """
        if endian not in ("<", ">", "!"):
            raise ValueError("invalid endian: " + str(endian))

        self._buf = bytearray()
        self._endian = endian
        self._validate = bool(validate)

    # ---------------------------------------------------------
    # internal helpers
    # ---------------------------------------------------------

    def _check_u(self, value: int, bits: int) -> int:
        """
        Validate or mask an unsigned integer value.

        Parameters
        ----------
        value:
            Integer value to check.

        bits:
            Bit width of the unsigned type.

        Returns
        -------
        int
            Validated or masked integer.

        Raises
        ------
        ValueError
            If validation is enabled and the value exceeds the allowed range.
        """
        if not self._validate:
            return int(value) & ((1 << bits) - 1)

        max_value = (1 << bits) - 1

        if value < 0 or value > max_value:
            raise ValueError(
                "value out of range for u" + str(bits) + ": " + str(value)
            )

        return int(value)

    # ---------------------------------------------------------
    # numeric writes
    # ---------------------------------------------------------

    def u8(self, value: int) -> ByteWriter:
        """
        Write an unsigned 8-bit integer.

        Parameters
        ----------
        value:
            Integer in range [0, 255].

        Returns
        -------
        ByteWriter
            The writer instance (fluent API).
        """
        self._buf.append(self._check_u(value, 8))
        return self

    def i8(self, value: int) -> ByteWriter:
        """
        Write a signed 8-bit integer.

        Parameters
        ----------
        value:
            Integer in range [-128, 127].

        Returns
        -------
        ByteWriter
        """
        self._buf.extend(struct.pack(self._endian + "b", int(value)))
        return self

    def u16(self, value: int) -> ByteWriter:
        """
        Write an unsigned 16-bit integer.

        Parameters
        ----------
        value:
            Integer in range [0, 65535].

        Returns
        -------
        ByteWriter
        """
        value = self._check_u(value, 16)
        self._buf.extend(struct.pack(self._endian + "H", value))
        return self

    def i16(self, value: int) -> ByteWriter:
        """
        Write a signed 16-bit integer.

        Returns
        -------
        ByteWriter
        """
        self._buf.extend(struct.pack(self._endian + "h", int(value)))
        return self

    def u32(self, value: int) -> ByteWriter:
        """
        Write an unsigned 32-bit integer.

        Returns
        -------
        ByteWriter
        """
        value = self._check_u(value, 32)
        self._buf.extend(struct.pack(self._endian + "I", value))
        return self

    def i32(self, value: int) -> ByteWriter:
        """
        Write a signed 32-bit integer.

        Returns
        -------
        ByteWriter
        """
        self._buf.extend(struct.pack(self._endian + "i", int(value)))
        return self

    # ---------------------------------------------------------
    # raw bytes
    # ---------------------------------------------------------

    def raw(self, data: Buffer) -> ByteWriter:
        """
        Append raw bytes to the internal buffer.

        Parameters
        ----------
        data:
            Bytes-like object to append.

        Returns
        -------
        ByteWriter
        """
        if data:
            self._buf.extend(data)

        return self

    # ---------------------------------------------------------
    # string encoding
    # ---------------------------------------------------------

    def string(
        self,
        value: str,
        encoding: str = "utf-8",
        max_chars: int | None = None,
    ) -> ByteWriter:
        """
        Serialize a string using the TibiaME protocol format.

        Encoding format:

            If len <= 0xFE:
                [u8 length] + data

            If len > 0xFE:
                [0xFF] + [u16 length] + data

        Parameters
        ----------
        value:
            Source text string.

        encoding:
            Character encoding used to convert the string to bytes.

        max_chars:
            Optional maximum number of characters allowed before encoding.

        Returns
        -------
        ByteWriter

        Raises
        ------
        ValueError
            If the encoded string exceeds 65535 bytes.
        """
        text = value

        if max_chars is not None:
            text = text[: max(0, int(max_chars))]

        encoded = text.encode(encoding)
        size = len(encoded)

        if size > 0xFFFF:
            msg = "string payload exceeds 65535 bytes"
            raise ValueError(msg)

        if size <= 0xFE:
            self.u8(size)
        else:
            self.u8(0xFF)
            self.u16(size)

        self._buf.extend(encoded)

        return self

    # ---------------------------------------------------------
    # boolean
    # ---------------------------------------------------------

    def write_bool(self, *, value: bool) -> ByteWriter:
        """
        Write a boolean value as an unsigned byte.

        True  -> 1
        False -> 0
        """
        self._buf.append(1 if value else 0)
        return self

    # ---------------------------------------------------------
    # export
    # ---------------------------------------------------------

    def build(self, *,  clear: bool = False) -> bytes:
        """
        Export the current buffer as immutable bytes.

        Parameters
        ----------
        clear:
            If True, clears the internal buffer after exporting.

        Returns
        -------
        bytes
            Serialized byte sequence.
        """
        data = bytes(self._buf)

        if clear:
            self._buf.clear()

        return data

    def to_bytes(self, *, clear: bool = False) -> bytes:
        """
        Alias for :meth:`build`.

        Provided for compatibility with existing codebases.
        """
        return self.build(clear=clear)

    # ---------------------------------------------------------
    # helpers
    # ---------------------------------------------------------

    def clear(self) -> ByteWriter:
        """
        Clear the internal buffer.

        Returns
        -------
        ByteWriter
        """
        self._buf.clear()
        return self

    def size(self) -> int:
        """
        Return the current size of the buffer in bytes.
        """
        return len(self._buf)

    def hex(self) -> str:
        """
        Return a hexadecimal representation of the buffer.
        """
        return self._buf.hex()

    def clone(self) -> ByteWriter:
        """
        Create a copy of the writer with the same buffer content.
        """
        other = ByteWriter(self._endian, validate=self._validate)
        other._buf = bytearray(self._buf)
        return other
