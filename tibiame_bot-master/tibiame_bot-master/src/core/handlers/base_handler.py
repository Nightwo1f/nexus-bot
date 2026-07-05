from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from core.handlers.handler_meta import HandlerMeta

if TYPE_CHECKING:
    from core.network.session import Session
    from core.protocol.packet import Packet


class PacketHandler(ABC, metaclass=HandlerMeta):
    """
    Base class for packet handlers.

    Each handler is responsible for processing a specific opcode.
    """

    OPCODE: int = -1

    @abstractmethod
    async def handle(self, session: Session, packet: Packet) -> None:
        """
        Handles an incoming packet.
        """
        raise NotImplementedError
