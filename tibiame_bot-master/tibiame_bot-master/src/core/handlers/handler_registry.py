from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.handlers.base_handler import PacketHandler

class HandlerRegistry:
    """
    Global registry storing packet handlers by opcode.
    """
    _instance = None

    def __init__(self) -> None:
        self._handlers: dict[int, PacketHandler] = {}

    @classmethod
    def global_registry(cls) -> HandlerRegistry:
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def register(self, handler: PacketHandler) -> None:
        opcode = handler.OPCODE

        if opcode < 0:
            msg = "Invalid opcode: " + str(opcode)
            raise ValueError(msg)
        if opcode in self._handlers:
            msg = "Handler already registered for opcode: " + str(opcode)
            raise ValueError(msg)

        self._handlers[opcode] = handler

    def get(self, opcode: int) -> PacketHandler | None:
        return self._handlers.get(opcode)




