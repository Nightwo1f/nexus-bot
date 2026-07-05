

class ProtocolError(Exception):
    """Base exception for protocol-related errors."""
    pass

class PacketDecodeError(ProtocolError):
    """
    Packet decoding failed.
    """
    pass


class InvalidOpcodeError(ProtocolError):
    """
    Invalid opcode received.
    """
    pass


class PacketSizeError(ProtocolError):
    """
    Packet size mismatch.
    """
    pass
