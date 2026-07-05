"""Login protocol implementation based on the discovered flow from analysis.

Based on the latest testing results (Dec 2024), the correct login flow is:
1. Connect to login.otjtme.com:9191
2. Send opcode 17 with world -> Server responds with MOTD (opcode 20)
3. Send opcode 16 with world -> Server responds with game server redirect (opcode 100)
4. Connect to game server and establish game session

The package with username/password is likely used in a different flow or screen.
"""
import socket
from typing import List, Tuple, NamedTuple

from jtme_bot.protocol.framing import encode_frame, read_exact, read_frame
from jtme_bot.protocol.packet_writer import PacketWriter
from jtme_bot.protocol.packet_reader import PacketReader

# Connection constants
LOGIN_HOST = "login.otjtme.com"
LOGIN_PORT = 9191

# Packet opcodes
LOGIN_MAGIC = 0x24  # protocol magic byte (36)
LOGIN_OPCODE_PREPARE = 0x11  # opcode for prepare (17)
LOGIN_OPCODE_LOGIN = 0x10   # opcode for login (16)
GAME_REDIRECT_OPCODE = 0x64  # opcode for game redirect (100)

# Game server defaults (extracted from analysis)
DEFAULT_GAME_HOST = "52.67.80.70"
DEFAULT_GAME_PORT = 7777


class LoginPacket:
    """Represents a parsed login packet."""
    def __init__(self, opcode: int, data: bytes) -> None:
        self.opcode = opcode
        self.data = data

    def __repr__(self) -> str:
        return f"LoginPacket(opcode={self.opcode}, data={self.data!r})"


class LoginServerRedirect(NamedTuple):
    """Contains server redirect information from login server."""
    session_id: int
    game_host: str
    game_port: int


def build_prepare_payload(world: int) -> bytes:
    """Build the prepare packet (opcode 17)."""
    writer = PacketWriter()
    writer.write_u8(LOGIN_OPCODE_PREPARE)
    writer.write_u16(world)
    return writer.to_bytes()


def build_login_payload(character: str, password: str, world: int) -> bytes:
    """Build the traditional login payload (likely used in other flows)."""
    writer = PacketWriter()
    writer.write_u8(LOGIN_OPCODE_LOGIN)
    writer.write_string(character)
    writer.write_string(password)
    writer.write_u16(world)
    return writer.to_bytes()


def try_parse_game_redirect(payload: bytes) -> LoginServerRedirect | None:
    """Parse the game redirect packet from login server (opcode 100)."""
    if not payload or len(payload) < 3:
        return None

    start_error: Exception | None = None
    # Try reading from different starting positions (handle prefix bytes)
    for skipped_prefix_bytes in range(0, min(8, len(payload)) + 1):
        candidate = PacketReader(payload[1:])  # Use payload[1:] as in original
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


def parse_login_packet(payload: bytes) -> Tuple[LoginPacket, bytes]:
    """Parse a login packet into opcode and remaining data."""
    if not payload:
        raise ValueError("empty payload")

    reader = PacketReader(payload)
    opcode = reader.read_u8()
    remaining_data = reader._read(reader.remaining())

    return LoginPacket(opcode=opcode, data=remaining_data), remaining_data


def parse_motd_packet(payload: bytes) -> str:
    """Parse MOTD (Message of the Day) packet."""
    if not payload:
        return ""

    reader = PacketReader(payload)
    opcode = reader.read_u8()
    if opcode != 0x14:  # MOTD opcode
        raise ValueError(f"expected MOTD packet, got opcode={opcode}")

    motd_length = reader.read_u16()
    motd_data = reader._read(motd_length)
    return motd_data.decode('utf-8', errors='replace')


def connect_and_login_with_discovered_flow(character: str, password: str, world: int) -> Tuple[List[LoginPacket], LoginServerRedirect]:
    """Perform the discovered login flow to get game server redirect."""
    packets: List[LoginPacket] = []

    with socket.create_connection((LOGIN_HOST, LOGIN_PORT), timeout=5.0) as sock:
        sock.settimeout(5.0)

        # Step 1: Send prepare (opcode 17)
        prepare_payload = encode_frame(build_prepare_payload(world))
        sock.sendall(prepare_payload)
        packets.append(LoginPacket(opcode=LOGIN_OPCODE_PREPARE, data=prepare_payload))

        # Step 2: Receive MOTD (opcode 20)
        motd_frame = read_frame(sock)
        motd_packet, _ = parse_login_packet(motd_frame)
        packets.append(motd_packet)

        # Step 3: Send login (opcode 16)
        login_payload = encode_frame(build_login_payload(character, password, world))
        sock.sendall(login_payload)
        packets.append(LoginPacket(opcode=LOGIN_OPCODE_LOGIN, data=login_payload))

        # Step 4: Receive game server redirect (opcode 100)
        redirect_frame = read_frame(sock)
        redirect_packet, _ = parse_login_packet(redirect_frame)
        packets.append(redirect_packet)

        # Parse game redirect
        redirect_info = try_parse_game_redirect(redirect_frame)

        if not redirect_info:
            raise ConnectionError("Failed to parse game server redirect packet")

        return packets, redirect_info


class LoginClient:
    """Login client with discovered protocol flow."""

    def __init__(self, host: str = LOGIN_HOST, port: int = LOGIN_PORT, timeout: float = 5.0) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout

    def connect_and_login(self, character: str, password: str, world: int) -> Tuple[List[LoginPacket], LoginServerRedirect]:
        """Perform the complete login flow to get game server redirect."""
        return connect_and_login_with_discovered_flow(character, password, world)