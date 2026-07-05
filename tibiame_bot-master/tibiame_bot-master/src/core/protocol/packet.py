"""
Packet model and framing implementation for the TibiaME protocol.

Supported frame format:

    [u16 body_len][u8 opcode][payload...]

Where:

    body_len = 1 + len(payload)
    opcode   = unsigned 8-bit integer
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from core.protocol.byte_reader import ByteReader
from core.protocol.byte_writer import ByteWriter


@dataclass(frozen=True)
class Packet:
    """
    Represents a logical protocol message.

    The class stores the packet opcode and payload, and provides
    utilities to encode and decode protocol frames.

    Frame structure:

        [u16 body_len][u8 opcode][payload...]

    Where:

        body_len = 1 (opcode) + payload length
    """

    opcode: int
    payload: bytes

    HEADER_LEN: ClassVar[int] = 2

    def encode(self, *, endian: str = "<") -> bytes:
        """
        Encodes the packet into a network frame.

        Returns
        -------
        bytes
            Frame ready to be sent over the network.

        Raises
        ------
        ValueError
            If opcode is outside the valid u8 range.
        """

        self._validate_opcode_u8(self.opcode)

        body_len = 1 + len(self.payload)

        writer = ByteWriter(endian=endian)

        writer.u16(body_len)
        writer.u8(self.opcode)

        if self.payload:
            writer.raw(self.payload)

        return writer.to_bytes()

    @classmethod
    def decode(
        cls,
        header: bytes,
        body: bytes,
        *,
        endian: str = "<",
        strict: bool = True,
    ) -> Packet:
        """
        Decodes a packet from header and body.

        Parameters
        ----------
        header : bytes
            Frame header containing `u16 body_len`.

        body : bytes
            Frame body containing `opcode + payload`.

        endian : str
            Endianness used to read body length.

        strict : bool
            When True validates body length and opcode.

        Returns
        -------
        Packet
        """

        if len(header) != cls.HEADER_LEN:
            msg = "header must have " + str(cls.HEADER_LEN) + " bytes"
            raise ValueError(msg)

        reader = ByteReader(header, endian=endian)

        declared_body_len = reader.read_uint16()

        if strict and declared_body_len != len(body):
            msg = (
                "body length mismatch header="
                + str(declared_body_len)
                + " actual="
                + str(len(body))
            )
            raise ValueError(msg)

        if not body:
            msg = "body is empty; opcode byte missing"
            raise ValueError(msg)

        opcode = body[0]
        payload = body[1:]

        if strict:
            cls._validate_opcode_u8(opcode)

        return cls(opcode=opcode, payload=payload)

    @classmethod
    def decode_frame(
        cls,
        frame: bytes,
        *,
        endian: str = "<",
        strict: bool = True,
    ) -> Packet:
        """
        Decodes a packet directly from a full frame.

        Parameters
        ----------
        frame : bytes
            Raw network frame.

        Returns
        -------
        Packet
        """

        if len(frame) < cls.HEADER_LEN + 1:
            msg = "frame too short"
            raise ValueError(msg)

        header = frame[: cls.HEADER_LEN]
        body = frame[cls.HEADER_LEN :]

        return cls.decode(
            header=header,
            body=body,
            endian=endian,
            strict=strict,
        )

    @classmethod
    def from_payload_writer(
        cls,
        opcode: int,
        writer: ByteWriter,
        *,
        clear: bool = True,
    ) -> Packet:
        """
        Creates a Packet using a ByteWriter as payload builder.
        """

        cls._validate_opcode_u8(opcode)

        payload = writer.to_bytes()

        if clear:
            writer.clear()

        return cls(opcode=opcode, payload=payload)

    def payload_reader(self, *, endian: str = "<") -> ByteReader:
        """
        Creates a ByteReader for parsing the payload.
        """

        return ByteReader(self.payload, endian=endian)

    @staticmethod
    def _validate_opcode_u8(opcode: int) -> None:
        """
        Validates that opcode fits into an unsigned byte.
        """

        if opcode < 0 or opcode > 255:
            msg = "opcode out of range: " + str(opcode)
            raise ValueError(msg)
