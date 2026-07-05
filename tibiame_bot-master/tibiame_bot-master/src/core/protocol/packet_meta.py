"""
PacketMeta

Metaclass responsible for automatically registering packet classes
into the PacketRegistry.

Any class that defines an OPCODE attribute will be automatically
registered in the global PacketRegistry.

This removes the need for manual registration such as:

    registry.register(100, MovePacket)

Instead, defining the class is enough:

    class MovePacket(Packet):
        OPCODE = 100

        def __init__(self, payload: bytes):
            super().__init__(self.OPCODE, payload)

During class creation the metaclass detects the OPCODE attribute
and registers the class automatically.
"""

from typing import TYPE_CHECKING, Any, Dict, Tuple, Type

if TYPE_CHECKING:
    from core.protocol.packet import Packet

PacketType = Type["Packet"]


class PacketMeta(PacketType):
    """
    Metaclass used to automatically register packet classes.

    When a subclass of Packet defines an OPCODE attribute,
    it will automatically be registered in the PacketRegistry.

    This enables a plugin-like architecture where new packet
    types can be added without modifying central logic.
    """

    def __new__(
        mcls,
        name: str,
        bases: Tuple[type, ...],
        namespace: Dict[str, Any],
    ) -> type:
        """
        Creates a new packet class.

        During class creation this method checks whether the class
        defines an OPCODE attribute. If present, the class will be
        registered in the global PacketRegistry.

        Parameters
        ----------
        name : str
            Name of the class being created.

        bases : Tuple[type, ...]
            Base classes of the new class.

        namespace : Dict[str, Any]
            Class body attributes.

        Returns
        -------
        type
            Newly created class.
        """

        cls = super().__new__(mcls, name, bases, namespace)

        opcode = namespace.get("OPCODE")

        if opcode is not None:
            from core.protocol.packet_registry import PacketRegistry

            registry = PacketRegistry.global_registry()

            registry.register(int(opcode), lambda payload: cls(payload))

        return cls
