"""
PacketRegistry

Responsible for storing the mapping between packet opcodes
and packet classes.

The registry acts as a central lookup table used by PacketFactory
to determine which packet class should be instantiated when a
packet is received from the network.

This avoids the need for large conditional structures such as:

    if opcode == 100:
        ...
    elif opcode == 101:
        ...

Instead, packet classes register themselves automatically
(using PacketMeta) and the factory performs a simple lookup.
"""

from typing import Dict, Optional

from core.protocol.packet_types import PacketConstructor


class PacketRegistry:
    """
    Maintains opcode → packet class mapping.

    Each opcode is associated with a packet constructor that
    accepts a payload and returns a Packet instance.
    """

    _GLOBAL = None  # type: Optional["PacketRegistry"]

    def __init__(self) -> None:
        self._packets: Dict[int, PacketConstructor] = {}

    @classmethod
    def global_registry(cls) -> "PacketRegistry":
        """
        Returns the global singleton PacketRegistry.

        This allows packets to register themselves automatically
        through the PacketMeta metaclass without requiring a manual
        registry instance to be passed around the application.
        """

        if cls._GLOBAL is None:
            cls._GLOBAL = PacketRegistry()

        return cls._GLOBAL

    def register(self, opcode: int, packet_class: PacketConstructor) -> None:
        """
        Registers a packet class for a specific opcode.

        Parameters
        ----------
        opcode : int
            Network opcode associated with the packet.

        packet_class : PacketConstructor
            Packet class that can be instantiated with payload.
        """

        if opcode in self._packets:
            msg = "Opcode already registered: " + str(opcode)
            raise ValueError(msg)

        self._packets[opcode] = packet_class

    def get(self, opcode: int) -> Optional[PacketConstructor]:
        """
        Returns the packet constructor associated with an opcode.

        Parameters
        ----------
        opcode : int

        Returns
        -------
        Optional[PacketConstructor]
            Packet class constructor or None if opcode is unknown.
        """

        return self._packets.get(opcode)

    def has(self, opcode: int) -> bool:
        """
        Checks if an opcode is registered.

        Returns
        -------
        bool
        """

        return opcode in self._packets
