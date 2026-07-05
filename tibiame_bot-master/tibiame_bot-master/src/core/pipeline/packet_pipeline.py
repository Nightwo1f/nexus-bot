from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.network.session import Session
    from core.pipeline.middleware import Middleware
    from core.protocol.packet import Packet

class PacketPipeline:
    """
    Pipeline for processing packets through a series of middlewares.
    """
    def __init__(self) -> None:
        self._middlewares: list[Middleware] = []

    def add(self, middleware: Middleware) -> None:
        self._middlewares.append(middleware)

    async def process(self, session: Session, packet: Packet) -> Packet | None:

        current = packet

        for middleware in self._middlewares:
            if current is None:
                return None

            current = await middleware.process(session, current)

        return current

