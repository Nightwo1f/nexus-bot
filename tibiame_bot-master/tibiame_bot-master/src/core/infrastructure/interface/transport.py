"""
Transport interface.

Defines the contract used by the networking layer of the bot.

The transport is responsible for managing the TCP connection and
providing async methods to send and receive raw bytes.

PacketStream and higher layers rely on this interface to remain
independent from the actual networking implementation.
"""

from typing import Protocol


class ITransport(Protocol):
    """
    Transport abstraction used by PacketStream.

    Implementations may use:

    - asyncio TCP sockets
    - TLS connections
    - proxy bridges
    - mock transports for testing
    """

    def is_connected(self) -> bool:
        """
        Returns whether the transport is currently connected.
        """
        raise NotImplementedError

    async def connect(
        self,
        host: str,
        port: int,
        timeout: float = 10.0,
    ) -> None:
        """
        Establishes a connection to the remote endpoint.

        Parameters
        ----------
        host : str
            Remote host.

        port : int
            Remote port.

        timeout : float
            Connection timeout in seconds.
        """
        raise NotImplementedError

    async def close(self) -> None:
        """
        Closes the connection.
        """
        raise NotImplementedError

    async def send(self, data: bytes) -> None:
        """
        Sends raw bytes through the transport.

        Parameters
        ----------
        data : bytes
        """
        raise NotImplementedError

    async def recv_exactly(self, n: int) -> bytes:
        """
        Receives exactly N bytes from the connection.

        Raises
        ------
        ConnectionError
            If the connection closes before receiving N bytes.
        """
        raise NotImplementedError

    async def receive(self, count: int) -> bytes:
        """
        Receives up to N bytes.

        This method may return fewer bytes than requested.
        """
        raise NotImplementedError
