from __future__ import annotations

from abc import ABCMeta


class HandlerMeta(ABCMeta):
    """
    Metaclass for automatically registering PacketHandler subclasses.
    """
    def __new__(cls, name: str, bases: tuple[type, ...], namespace: dict[str, object]) -> type:
        cls = super().__new__(cls, name, bases, namespace)

        opcode = namespace.get("OPCODE")
        if opcode is not None and (isinstance(opcode, int) and opcode >= 0):
            print(f"Registering handler {cls.__name__} for opcode {opcode}...")
            from core.handlers.handler_registry import HandlerRegistry

            registry = HandlerRegistry.global_registry()
            handler_instance = cls()
            registry.register(handler_instance)

        return cls



