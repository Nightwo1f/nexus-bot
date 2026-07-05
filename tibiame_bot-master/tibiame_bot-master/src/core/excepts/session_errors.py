class SessionError(Exception):
    """
    Base session error.
    """
    pass


class SessionClosedError(SessionError):
    """
    Raised when session is closed unexpectedly.
    """
    pass
