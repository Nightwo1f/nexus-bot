"""
PacketFactory

Responsible for creating packet objects based on opcode.

The factory retrieves the correct packet class from PacketRegistry
and instantiates it using the provided payload.

If an opcode is not registered, a generic Packet instance is returned.

This design allows the protocol system to be extended by simply
adding new packet classes without modifying the factory logic.
"""

from core.protocol.packet import Packet
from core.protocol.packet_registry import PacketRegistry


class PacketFactory:
    """
    Factory responsible for creating packet objects.
    """

    def __init__(self, registry: PacketRegistry) -> None:
        """
        Initializes the PacketFactory.

        Parameters
        ----------
        registry : PacketRegistry
            Registry used to resolve packet classes.
        """

        self._registry = registry

    def create(self, opcode: int, payload: bytes) -> Packet:
        """
        Creates a packet instance from opcode and payload.

        Parameters
        ----------
        opcode : int
            Packet opcode received from network.

        payload : bytes
            Raw payload data.

        Returns
        -------
        Packet
            Specific packet instance if registered, otherwise
            a generic Packet object.
        """

        packet_class = self._registry.get(opcode)

        if packet_class is None:
            return Packet(opcode, payload)

        return packet_class(payload)

    def decode(self, frame: bytes) -> Packet:
        """
        Decodes a raw network frame into a packet instance.

        The frame format must follow the protocol framing:

            [u16 body_len][u8 opcode][payload...]

        Parameters
        ----------
        frame : bytes
            Raw frame received from network.

        Returns
        -------
        Packet
            Parsed packet instance.
        """

        base_packet = Packet.decode_frame(frame)

        return self.create(base_packet.opcode, base_packet.payload)
