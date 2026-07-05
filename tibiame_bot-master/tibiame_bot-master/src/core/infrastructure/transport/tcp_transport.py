from __future__ import annotations

import asyncio

from core.excepts.transport_errors import TransportConnectionError
from core.infrastructure.interface.transport import ITransport


class TcpTransport(ITransport):
    def __init__(self) -> None:
        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None
        self._send_lock = asyncio.Lock()

    async def connect(self, host: str, port: int, timeout: float = 10.0) -> None:
        if port < 1 or port > 65535:
            msg = "Invalid port: " + str(port)
            raise ValueError(msg)

        await self.close()

        try:
            if timeout is None or timeout <= 0:
                reader, writer = await asyncio.open_connection(host, port)
            else:
                reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=timeout)
        except Exception as e:
            msg = (
                "Failed to connect to "
                + str(host)
                + ":"
                + str(port)
                + " cause="
                + str(e)
            )
            raise TransportConnectionError(msg) from e

        self._reader = reader
        self._writer = writer

    async def send(self, data: bytes) -> None:
        writer = self._writer
        if writer is None:
            msg = "Transport is not connected."
            raise ConnectionError(msg)

        async with self._send_lock:
            try:
                writer.write(data)
                await writer.drain()
            except Exception as e:
                await self.close()
                msg = "Failed to send payload bytes. cause=" + str(e)
                raise TransportConnectionError(msg) from e


    async def recv_exactly(self, n: int) -> bytes:
        if n < 0:
            msg = "n must be >= 0"
            raise ValueError(msg)
        if n == 0:
            return b""

        reader = self._reader
        if reader is None:
            msg = "Transport is not connected."
            raise ConnectionError(msg)

        try:
            return await reader.readexactly(n)
        except asyncio.IncompleteReadError:
            await self.close()
            msg = "Connection closed while receiving " + str(n) + " bytes."
            raise TransportConnectionError(msg) from None
        except Exception as exc:
            await self.close()
            msg = "Failed to receive bytes. cause = " + str(exc)
            raise TransportConnectionError(msg) from exc

    async def receive(self, count: int) -> bytes:
        return await self.recv_exactly(count)

    def is_connected(self) -> bool:
        return self._writer is not None

    async def close(self) -> None:
        writer = self._writer
        self._reader = None
        self._writer = None

        if writer is None:
            return

        try:
            writer.close()
            await writer.wait_closed()
        except OSError:
            return
