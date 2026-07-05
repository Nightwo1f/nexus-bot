"""
Packet type definitions used by the protocol system.

This module defines structural typing contracts used to describe
packet constructors. The goal is to help static type checkers
(Pylance, MyPy, Ruff) understand how packet classes are instantiated.

In this architecture packet classes are created with:

    packet_class(payload)

Instead of:

    packet_class(opcode, payload)

because each packet class defines its own OPCODE constant.
"""

from typing import Protocol

from core.protocol.packet import Packet


class PacketConstructor(Protocol):
    """
    Represents a callable packet class.

    Packet classes registered in PacketRegistry must be callable
    with a single argument (payload) and must return a Packet instance.

    Example
    -------
    class MovePacket(Packet):

        OPCODE = 100

        def __init__(self, payload: bytes):
            super().__init__(self.OPCODE, payload)

    When PacketFactory creates a packet it will call:

        packet_class(payload)

    which matches this protocol.
    """

    def __call__(self, payload: bytes) -> Packet:
        ...
