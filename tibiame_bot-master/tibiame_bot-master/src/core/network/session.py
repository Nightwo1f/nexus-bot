from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.dispatcher.dispatcher import Dispatcher
    from core.infrastructure.interface.transport import ITransport
    from core.pipeline.packet_pipeline import PacketPipeline
    from core.protocol.packet import Packet
    from core.stream.packet_stream import PacketStream


class Session:
    def __init__(self, transport: ITransport, stream: PacketStream, dispatcher: Dispatcher, pipeline: PacketPipeline) -> None:
        self._transport = transport
        self._stream = stream
        self._dispatcher = dispatcher
        self._pipeline = pipeline

        self._running = False
        self._send_queue: asyncio.Queue[Packet] = asyncio.Queue()
        self._received_packets: asyncio.Queue[Packet] = asyncio.Queue()

        self._reader_task: asyncio.Task | None = None
        self._writer_task: asyncio.Task | None = None

    async def connect(self, host: str, port: int) -> None:
        await self._transport.connect(host, port)

        self._running = True

        self._reader_task = asyncio.create_task(self._read_loop())
        self._writer_task = asyncio.create_task(self._write_loop())

    async def close(self) -> None:
        self._running = False

        if self._reader_task:
            self._reader_task.cancel()

        if self._writer_task:
            self._writer_task.cancel()

        await self._transport.close()

    async def send(self, packet: Packet) -> None:
        await self._send_queue.put(packet)

    async def receive(self, timeout: float | None = None) -> Packet:
        if timeout is None:
            return await self._received_packets.get()

        return await asyncio.wait_for(self._received_packets.get(), timeout=timeout)

    async def _write_loop(self) -> None:
        while self._running:
            packet = await self._send_queue.get()
            try:
                await self._stream.send(packet)
            except (OSError, asyncio.CancelledError) as e:
                print(e)
                await self.close()

    async def _read_loop(self) -> None:
        while self._running:
            try:
                packet = await self._stream.read()
                packet = await self._pipeline.process(self, packet)

                if packet is None:
                    continue

                self._received_packets.put_nowait(packet)
                await self._dispatcher.dispatch(self, packet)

            except (OSError, asyncio.CancelledError) as e:
                print(e)
                await self.close()
