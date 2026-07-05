from __future__ import annotations

import socket


MAX_FRAME_SIZE = 0xFFFF


def encode_frame(payload: bytes | bytearray | memoryview) -> bytes:
    payload_bytes = bytes(payload)
    if len(payload_bytes) > MAX_FRAME_SIZE:
        raise ValueError(f"payload too large: {len(payload_bytes)} bytes")
    return len(payload_bytes).to_bytes(2, "little") + payload_bytes


def read_exact(sock: socket.socket, size: int) -> bytes:
    if size < 0:
        raise ValueError("size cannot be negative")

    chunks = bytearray()
    while len(chunks) < size:
        chunk = sock.recv(size - len(chunks))
        if not chunk:
            raise ConnectionError("socket closed while reading frame")
        chunks.extend(chunk)
    return bytes(chunks)


def read_frame(sock: socket.socket) -> bytes:
    length = int.from_bytes(read_exact(sock, 2), "little")
    return read_exact(sock, length)
