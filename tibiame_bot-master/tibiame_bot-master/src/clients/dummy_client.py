from __future__ import annotations

from typing import TYPE_CHECKING

from core.dispatcher.dispatcher import Dispatcher
from core.infrastructure.transport.tcp_transport import TcpTransport
from core.network.session import Session
from core.pipeline.logger_middleware import PacketDebugger
from core.pipeline.packet_pipeline import PacketPipeline
from core.stream.packet_stream import PacketStream

if TYPE_CHECKING:
    from core.protocol.packet import Packet


class DummyClient:
    """
    Headless client used by the bot.

    This client connects directly to the game server and
    uses the core Session to manage the connection.

    Responsibilities
    ----------------
    - create transport
    - create packet stream
    - create session
    - provide simple API for bot logic
    """

    def __init__(self) -> None:
        self._transport = TcpTransport()
        self._stream = PacketStream(self._transport)
        self.dispatcher = Dispatcher()
        self._pipeline = PacketPipeline()

        self._pipeline.add(PacketDebugger(500))

        self._session = Session(self._transport, self._stream, self.dispatcher, self._pipeline)

        self.host = ""
        self.port = 0

    async def connect(self, host: str, port: int) -> None:
        """
        Connects the bot to the server.
        """
        self.host = host
        self.port = port
        await self._session.connect(host, port)

    async def disconnect(self) -> None:
        """
        Disconnects the bot from the server.
        """
        await self._session.close()

    async def send_packet(self, packet: Packet) -> None:
        """
        Sends a packet to the server.
        """
        await self._session.send(packet)

    async def recv_packet(self, timeout: float | None = None) -> Packet:
        """
        Waits for the next received packet.
        """
        return await self._session.receive(timeout=timeout)

    def is_connected(self) -> bool:
        """
        Returns True if the bot is connected to the server.
        """
        return self._transport.is_connected()

    @property
    def session(self) -> Session:
        """
        Returns the current session instance.
        """
        return self._session
