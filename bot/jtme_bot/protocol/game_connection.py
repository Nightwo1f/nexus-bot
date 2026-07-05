"""Game connection module for JTME game server based on decompiled code analysis.

This module implements the game server connection handshake based on values from:
- cashserver.txt: game server is at 52.67.80.70:7777
- brclass.py: game connection handshake values (aj calls)
"""
import socket
import threading
import time
from typing import List, Tuple
from enum import Enum

from jtme_bot.protocol.framing import encode_frame, read_frame
from jtme_bot.protocol.packet_writer import PacketWriter
from jtme_bot.protocol.packet_reader import PacketReader


class ConnectionError(Exception):
    """Raised when connection to game server fails."""
    pass


class NetState(Enum):
    """Network state for the game connection."""
    IDLE = 0
    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTED = 3


class GameServerConfig:
    """Configuration for game server connection based on analysis."""

    # From cashserver.txt
    DEFAULT_HOST = "52.67.80.70"
    DEFAULT_PORT = 7777
    DEFAULT_WORLD_ID = 200  # From cashserver.txt session/world id: 200

    # Timeout settings
    CONNECT_TIMEOUT = 5.0
    READ_TIMEOUT = 5.0

    # Buffer sizes
    BUFFER_SIZE = 1024
    MAX_RECONNECT_ATTEMPTS = 3


class GamePacket:
    """Represents a parsed game packet."""
    def __init__(self, opcode: int, data: bytes) -> None:
        self.opcode = opcode
        self.data = data

    def __repr__(self) -> str:
        return f"GamePacket(opcode={self.opcode}, data_length={len(self.data)})"


class GameConnection:
    """Game server connection based on brclass.py analysis."""

    # Settings values from cashserver.txt analysis:
    # settings.S = 36 (LOGIN_MAGIC)
    # settings.T = 63
    # settings.bK = 22
    # settings.bJ = 126
    # settings.bV = 19
    # settings.bW = 17
    # settings.bK = 22 (appears twice in different contexts)
    # settings.bJ = 126
    # settings.bV = 19
    # settings.bW = 17

    def __init__(self, host: str = GameServerConfig.DEFAULT_HOST,
                 port: int = GameServerConfig.DEFAULT_PORT) -> None:
        self.host = host
        self.port = port
        self.socket = None
        self.reader_thread = None
        self.state = NetState.IDLE
        self.connected = False
        self.error_callback = None
        self.packet_callback = None
        self.thread = None

    def connect(self) -> bool:
        """Connect to game server using protocol from brclass.py.

        Based on handshake from brclass.py lines 603-607:
        - packet with opcode 3, value 36 (LOGIN_MAGIC)
        - packet with opcode 36, value 0
        - packet with opcode 5/0 (character info), value paramInt2
        - packet with opcode 22 (settings.bK)
        - packet with opcode 126 (settings.bJ)
        - packet with opcode 19 (settings.bV)
        - packet with opcode 17 (settings.bW)
        - packet with opcode 18 (emote/buffer size)
        """
        try:
            self.state = NetState.CONNECTING
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.settimeout(GameServerConfig.CONNECT_TIMEOUT)

            self.socket.connect((self.host, self.port))
            self.socket.settimeout(GameServerConfig.READ_TIMEOUT)

            # Start receive thread
            self.reader_thread = threading.Thread(target=self._receive_loop, daemon=True)
            self.reader_thread.start()

            # Wait briefly for connection to establish
            time.sleep(0.1)

            if self.reader_thread.is_alive():
                self.state = NetState.CONNECTED
                self.connected = True
                return True
            else:
                self.state = NetState.DISCONNECTED
                return False

        except Exception as e:
            self.state = NetState.DISCONNECTED
            if self.error_callback:
                self.error_callback(f"Connection failed: {e}")
            return False

    def disconnect(self) -> None:
        """Disconnect from game server."""
        self.connected = False

        if self.reader_thread:
            # Wait for thread to finish
            self.reader_thread.join(timeout=1.0)

        if self.socket:
            try:
                self.socket.close()
            except Exception:
                pass
            self.socket = None

        self.state = NetState.DISCONNECTED

    def send_packet(self, opcode: int, data: bytes = None) -> bool:
        """Send a packet to game server."""
        if not self.connected or not self.socket:
            return False

        try:
            writer = PacketWriter()
            writer.write_u8(opcode)
            if data:
                writer.write_bytes(data)

            packet = writer.to_bytes()
            frame = encode_frame(packet)
            self.socket.sendall(frame)
            return True

        except Exception as e:
            if self.error_callback:
                self.error_callback(f"Packet send failed: {e}")
            self.disconnect()
            return False

    def send_game_connect_packet(self, character_id: int, session_id: int) -> bool:
        """Send the complete game connection handshake from brclass.py.

        Based on brclass.py lines 603-607 and related methods.
        """
        packets = []

        # 1. Opcode 3 (game connect start), value 36 (LOGIN_MAGIC)
        writer1 = PacketWriter()
        writer1.write_u8(3)
        writer1.write_u8(36)
        packets.append((writer1.to_bytes(), "opcode 3 with magic"))

        # 2. Opcode 36, value 0
        writer2 = PacketWriter()
        writer2.write_u8(36)
        writer2.write_u8(0)
        packets.append((writer2.to_bytes(), "opcode 36 with zero"))

        # 3. Opcode 5/0, value paramInt2 (character info, 5 for char + 0 for something else)
        writer3a = PacketWriter()
        writer3a.write_u8(5)
        writer3a.write_u16(character_id)
        packets.append((writer3a.to_bytes(), "opcode 5 with character ID"))

        writer3b = PacketWriter()
        writer3b.write_u8(0)
        writer3b.write_u16(session_id)
        packets.append((writer3b.to_bytes(), "opcode 0 with session ID"))

        # 4-7. Settings values from analysis
        # 4. Opcode 22 (settings.bK)
        writer4 = PacketWriter()
        writer4.write_u8(22)
        writer4.write_u16(GameServerConfig.DEFAULT_WORLD_ID)
        packets.append((writer4.to_bytes(), "opcode 22 with world ID"))

        # 5. Opcode 126 (settings.bJ)
        writer5 = PacketWriter()
        writer5.write_u8(126)
        packets.append((writer5.to_bytes(), "opcode 126"))

        # 6. Opcode 19 (settings.bV)
        writer6 = PacketWriter()
        writer6.write_u8(19)
        packets.append((writer6.to_bytes(), "opcode 19"))

        # 7. Opcode 17 (settings.bW)
        writer7 = PacketWriter()
        writer7.write_u8(17)
        packets.append((writer7.to_bytes(), "opcode 17"))

        # 8. Opcode 18, value 12 (buffer/emote size)
        writer8 = PacketWriter()
        writer8.write_u8(18)
        writer8.write_u16(12)
        packets.append((writer8.to_bytes(), "opcode 18 with buffer size"))

        # Send all packets
        for packet_data, description in packets:
            if not self.send_packet(opcode=packet_data[0], data=packet_data[1:]):
                return False

        return True

    def _receive_loop(self) -> None:
        """Receive loop based on brclass.py packet handling."""
        try:
            while self.connected and self.socket:
                try:
                    frame = read_frame(self.socket)
                    if not frame:
                        break

                    # Parse packet from frame
                    if len(frame) > 0:
                        reader = PacketReader(frame)
                        opcode = reader.read_u8()
                        data = reader._read(reader.remaining())

                        packet = GamePacket(opcode, data)

                        if self.packet_callback:
                            self.packet_callback(packet)

                except Exception as e:
                    if self.error_callback:
                        self.error_callback(f"Receive error: {e}")
                    break

        except Exception as e:
            if self.error_callback:
                self.error_callback(f"Receive loop error: {e}")
        finally:
            self.connected = False
            self.state = NetState.DISCONNECTED

    def set_callbacks(self, error_callback=None, packet_callback=None) -> None:
        """Set callbacks for errors and packets."""
        self.error_callback = error_callback
        self.packet_callback = packet_callback


def test_connection() -> bool:
    """Test function to verify game server connection based on cashserver.txt values."""
    print("Testing game server connection...")
    print(f"Expected server: {GameServerConfig.DEFAULT_HOST}:{GameServerConfig.DEFAULT_PORT}")

    conn = GameConnection(GameServerConfig.DEFAULT_HOST, GameServerConfig.DEFAULT_PORT)

    def on_packet(packet):
        print(f"Received packet - opcode: {packet.opcode}, data length: {len(packet.data)}")

    def on_error(error):
        print(f"Connection error: {error}")

    conn.set_callbacks(on_error, on_packet)

    if conn.connect():
        print(f"Connection successful - state: {conn.state}")

        # Send game connect handshake
        print("Sending game connect handshake...")
        if conn.send_game_connect_packet(0, GameServerConfig.DEFAULT_WORLD_ID):  # character_id=0, session_id=world_id
            print("Handshake packets sent successfully")

        # Wait a bit to receive any responses
        time.sleep(2.0)

        conn.disconnect()
        return True
    else:
        print("Connection failed")
        return False


if __name__ == "__main__":
    # This would normally be called from the main bot code
    test_connection()