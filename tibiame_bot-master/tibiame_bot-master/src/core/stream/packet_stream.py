"""
PacketStream

High-level packet stream abstraction over a transport.

This component is responsible for reading and writing framed packets
according to the TibiaME protocol.

Frame format:

    [u16 body_len][u8 opcode][payload...]

Where:

    body_len = 1 (opcode) + payload length
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from core.protocol.byte_reader import ByteReader
from core.protocol.packet import Packet

if TYPE_CHECKING:
    from core.infrastructure.interface.transport import ITransport


@dataclass
class PacketStream:
    """
    Handles packet IO over a transport.

    The stream reads framed packets and converts them into `Packet`
    objects, and also serializes `Packet` objects into network frames.

    Parameters
    ----------
    transport : ITransport
        Transport implementation responsible for network IO.

    endian : str
        Endianness used for numeric values.

    max_body_len : int
        Maximum allowed body size for safety.
    """

    transport: ITransport
    endian: str = "<"
    max_body_len: int = 65536

    async def read(self) -> Packet:
        """
        Reads a single packet from the transport.

        Returns
        -------
        Packet
            Decoded packet instance.

        Raises
        ------
        ValueError
            If the packet framing is invalid.
        """

        header = await self._read_header()

        body_len = self._parse_body_len(header)

        self._validate_body_len(body_len)

        body = await self._read_body(body_len)

        return Packet.decode(
            header=header,
            body=body,
            endian=self.endian,
        )

    async def send(self, packet: Packet | int, payload: bytes = b"") -> None:
        """
        Sends a packet through the transport.

        Usage examples:

            await stream.send(packet)

        or

            await stream.send(opcode, payload)

        Parameters
        ----------
        packet : Packet | int
            Packet instance or opcode.

        payload : bytes
            Payload used when packet is an opcode.
        """

        _packet = packet if isinstance(packet, Packet) else Packet(packet, payload)

        frame = _packet.encode(endian=self.endian)

        await self.transport.send(frame)

    async def _read_header(self) -> bytes:
        """
        Reads the fixed-size frame header.

        Returns
        -------
        bytes
        """

        return await self.transport.recv_exactly(Packet.HEADER_LEN)

    def _parse_body_len(self, header: bytes) -> int:
        """
        Extracts the body length from the header.

        Returns
        -------
        int
        """

        reader = ByteReader(header, endian=self.endian)

        return reader.read_uint16()

    async def _read_body(self, lenght: int) -> bytes:
        """
        Reads the body of the packet.

        Returns
        -------
        bytes
        """

        return await self.transport.recv_exactly(lenght)

    def _validate_body_len(self, lenght: int) -> None:
        """
        Validates body size to avoid memory abuse.
        """

        if lenght < 1:
            msg = "invalid body length: " + str(lenght)
            raise ValueError(msg)

        if lenght > self.max_body_len:
            msg = "body length exceeds limit: " + str(lenght)
            raise ValueError(msg)
