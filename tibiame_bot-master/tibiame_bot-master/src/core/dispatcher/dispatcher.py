from __future__ import annotations

from typing import TYPE_CHECKING

from core.handlers.handler_registry import HandlerRegistry

if TYPE_CHECKING:
    from core.network.session import Session
    from core.protocol.packet import Packet


class Dispatcher:
    """
    Dispatches packets to handlers.
    """
    def __init__(self) -> None:
        self._registry = HandlerRegistry.global_registry()

    async def dispatch(self, session: Session, packet: Packet) -> None:
        handler = self._registry.get(packet.opcode)
        if handler is None:
            return

        await handler.handle(session, packet)
