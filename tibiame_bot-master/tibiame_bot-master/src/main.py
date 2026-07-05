import asyncio
import importlib
import pkgutil

import core.handlers
from clients.dummy_client import DummyClient
from core.packets.combo_login_packet import ComboLoginPacket
from core.packets.handshake_packets import (
    HandshakeStep2Packet,
    HandshakeStep3Packet,
    LoginServerHelloPacket,
    SelectWorldPacket,
    parse_pack_entries,
    parse_redirect_endpoint,
)
from core.packets.hello_packet import ClientHelloPacket
from core.packets.login_packet import LoginPacket

LOGIN_HOST = "44.242.62.47"
LOGIN_PORT = 9191
WORLD_ID = 1


def load_handlers() -> None:
    for module in pkgutil.walk_packages(core.handlers.__path__):
        # Import only package directories.
        if not module.ispkg:
            continue

        importlib.import_module(f"{core.handlers.__name__}.{module.name}")


async def wait_login_flow(client: DummyClient, timeout: float = 8.0) -> bool:
    try:
        first_response = await client.recv_packet(timeout=timeout)
    except asyncio.TimeoutError:
        print("No login response received in time.")
        await client.disconnect()
        return False

    print("Login response opcode:", first_response.opcode)

    if first_response.opcode == 13:
        try:
            follow_up = await client.recv_packet(timeout=timeout)
            print("Follow-up opcode:", follow_up.opcode)
        except asyncio.TimeoutError:
            print("No follow-up after ClientReady.")

    return True


async def main() -> None:
    client = DummyClient()
    await client.connect(LOGIN_HOST, LOGIN_PORT)

    print("Connected to login endpoint:", LOGIN_HOST, LOGIN_PORT)

    await client.send_packet(LoginServerHelloPacket.create())
    step1_response = await client.recv_packet(timeout=8.0)
    print("step1 opcode:", step1_response.opcode)

    await client.send_packet(HandshakeStep2Packet.create())
    step2_response = await client.recv_packet(timeout=8.0)
    print("step2 opcode:", step2_response.opcode)

    await client.send_packet(HandshakeStep3Packet.create())
    step3_response = await client.recv_packet(timeout=8.0)
    print("step3 opcode:", step3_response.opcode)

    await client.send_packet(SelectWorldPacket.create(WORLD_ID))
    step4_response = await client.recv_packet(timeout=8.0)
    print("step4 opcode:", step4_response.opcode)

    world_host, world_port = parse_redirect_endpoint(step4_response)
    pack_entries = parse_pack_entries(step2_response)
    print("Redirected world endpoint:", world_host, world_port)
    print("Pack entries:", len(pack_entries))

    await client.disconnect()
    await client.connect(world_host, world_port)
    print("Connected to world endpoint:", world_host, world_port)

    hello = ClientHelloPacket.create()
    login = LoginPacket.create(
        nickname="Tayo",
        password="123456",
        device_id="1234567891234",
        client_int_1=232,
        client_int_2=1169,
        pack_entries=pack_entries,
    )

    combo_login = ComboLoginPacket.create(hello_packet=hello, login_packet=login)

    await client.send_packet(combo_login)
    print("Sent combo login (msg3+msg13), waiting server response...")

    if not await wait_login_flow(client):
        return


def run() -> None:
    load_handlers()
    asyncio.run(main())


if __name__ == "__main__":
    run()
