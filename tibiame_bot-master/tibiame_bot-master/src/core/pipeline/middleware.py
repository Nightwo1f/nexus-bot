from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.network.session import Session
    from core.protocol.packet import Packet


class Middleware(ABC):
    """
    Base middleware for packet processing pipelines.
    """

    @abstractmethod
    async def process(self, session: Session, packet: Packet) -> Packet | None:
        """
        Processes packet before dispatcher.

        Can return:
        - Packet (continue pipeline)
        - None (cancel packet)
        """
        raise NotImplementedError

