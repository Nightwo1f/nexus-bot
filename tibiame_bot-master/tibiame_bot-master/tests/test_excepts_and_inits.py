from core.excepts import (
    InvalidOpcodeError,
    PacketDecodeError,
    PacketSizeError,
    SessionClosedError,
    TransportConnectionError,
    TransportReceiveError,
    TransportSendError,
)
from core.excepts.protocol_error import ProtocolError
from core.excepts.session_errors import SessionError
from core.excepts.transport_errors import TransportError


def test_exception_hierarchy_and_exports() -> None:
    assert issubclass(PacketDecodeError, ProtocolError)
    assert issubclass(InvalidOpcodeError, ProtocolError)
    assert issubclass(PacketSizeError, ProtocolError)
    assert issubclass(SessionClosedError, SessionError)
    assert issubclass(TransportConnectionError, TransportError)
    assert issubclass(TransportSendError, TransportError)
    assert issubclass(TransportReceiveError, TransportError)

    import core.excepts as excepts_pkg

    for name in excepts_pkg.__all__:
        assert hasattr(excepts_pkg, name)
