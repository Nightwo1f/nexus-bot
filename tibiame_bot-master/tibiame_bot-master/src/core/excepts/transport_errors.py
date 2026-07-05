

class TransportError(Exception):
    """Base exception for transport-related errors."""
    pass

class TransportConnectionError(TransportError):
    """Raised when a connection attempt fails or the transport is not connected."""
    pass

class TransportSendError(TransportError):
    """Raised when sending data over the transport fails."""
    pass

class TransportReceiveError(TransportError):
    """Raised when receiving data from the transport fails."""
    pass

