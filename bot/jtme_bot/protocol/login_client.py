from __future__ import annotations

from dataclasses import dataclass
import socket

from .framing import encode_frame, read_frame
from .packet_reader import PacketReader
from .packet_writer import PacketWriter

LOGIN_HOST = "login.otjtme.com"
LOGIN_PORT = 9191
CLIENT_MAJOR = 126
PASSWORD_XOR_KEY = "HACKINGISCRIME"
LOGIN_OPCODE = 3
LOGIN_MAGIC = 36
GAME_REDIRECT_OPCODE = 100


@dataclass(frozen=True)
class LoginPacket:
    opcode: int
    payload: bytes


@dataclass(frozen=True)
class LoginServerRedirect:
    session_id: int
    game_host: str
    game_port: int


def encode_password(password: str) -> str:
    return "".join(
        chr(ord(char) ^ ord(PASSWORD_XOR_KEY[index % len(PASSWORD_XOR_KEY)]))
        for index, char in enumerate(password)
    )


def build_login_payload(
    character: str,
    password: str,
    world: int,
    client_major: int = CLIENT_MAJOR,
    password_is_encoded: bool = False,
) -> bytes:
    encoded_password = password if password_is_encoded else encode_password(password)

    writer = PacketWriter()
    writer.write_u8(LOGIN_OPCODE)
    writer.write_u8(LOGIN_MAGIC)
    writer.write_string(character)
    writer.write_u8(world)
    writer.write_u16(client_major)
    writer.write_u8(0)
    writer.write_string(encoded_password)
    return writer.to_bytes()


def parse_login_packet(payload: bytes) -> tuple[LoginPacket, PacketReader]:
    reader = PacketReader(payload)
    opcode = reader.read_u8()
    return LoginPacket(opcode=opcode, payload=payload), reader


def try_parse_game_redirect(payload: bytes) -> LoginServerRedirect | None:
    packet, reader = parse_login_packet(payload)
    if packet.opcode != GAME_REDIRECT_OPCODE:
        return None

    start_error: Exception | None = None
    for skipped_prefix_bytes in range(0, min(8, reader.remaining()) + 1):
        candidate = PacketReader(payload[1:])
        try:
            candidate.skip(skipped_prefix_bytes)
            session_id = candidate.read_u16()
            game_host = candidate.read_string()
            game_port = candidate.read_u16()
        except (EOFError, UnicodeDecodeError, ValueError) as exc:
            start_error = exc
            continue

        if game_host and 0 < game_port <= 0xFFFF:
            return LoginServerRedirect(
                session_id=session_id,
                game_host=game_host,
                game_port=game_port,
            )

    if start_error is not None:
        return None
    return None


class LoginClient:
    def __init__(self, host: str = LOGIN_HOST, port: int = LOGIN_PORT, timeout: float = 5.0) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout

    def connect_and_login(self, character: str, password: str, world: int) -> list[LoginPacket]:
        request = encode_frame(build_login_payload(character, password, world))
        packets: list[LoginPacket] = []

        with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
            sock.settimeout(self.timeout)
            sock.sendall(request)
            while True:
                payload = read_frame(sock)
                packet, _ = parse_login_packet(payload)
                packets.append(packet)
                if packet.opcode == GAME_REDIRECT_OPCODE:
                    return packets
