from __future__ import annotations

from .packet_reader import PacketReader


def describe_payload(payload: bytes | bytearray | memoryview) -> str:
    payload_bytes = bytes(payload)
    if not payload_bytes:
        return "empty payload"

    reader = PacketReader(payload_bytes)
    opcode = reader.read_u8()
    preview = payload_bytes[1:17].hex(" ")
    suffix = "..." if len(payload_bytes) > 17 else ""
    return f"opcode={opcode} length={len(payload_bytes)} remaining={reader.remaining()} preview={preview}{suffix}"
