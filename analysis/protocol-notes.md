# JTME client protocol notes

Scope: compliant automation only. Allowed actions per user/server rules: use skills/spells, attack monsters, collect monster drops, reconnect. Movement automation must stay within 5 tiles and must not roam the whole map.

## Package observations

This folder is a packaged Java/libGDX client, not the OTserver source.

Launcher config:
- `app/JTME.json` main class: `jtme.game.lwjgl3.Lwjgl3Launcher`
- classpath: `JTME.jar`

The application code inside `JTME.jar` is heavily obfuscated under package `a/`.

## High-value classes from constant-pool scan

### `a/cq.class`
Likely settings/config class.

Relevant strings:
- `login.otjtme.com`
- `[GameSettings] ZoomMode: ... | Tiles: W=..., H=... | WebClient(2Bytes): ...`

### `a/bf.class`
Likely login connection/client.

Relevant strings:
- `LoginClient-Response`
- `java/net/Socket`
- `java/net/InetSocketAddress`
- `connect`
- `id_connect_to_login_server`
- `id_connection_to_login_server_failed`
- `id_connect_to_game_server`
- `id_connection_to_game_server_established`
- `id_downloading_game_data_counter_d_of_maxcounter_d`
- `Unk Packet LOGIN ID: 0x...`

### `a/br.class`
Likely game connection/client.

Relevant strings:
- `ServerClient`
- `GameConnectionThread`
- `GameResponseListener`
- `java/net/Socket`
- `java/net/InetSocketAddress`
- `java/net/SocketException`
- `id_connection_to_game_server_lost`
- `id_connection_to_game_server_preloading`
- `Unk Packet GAME ID: 0x...`
- `Dictionary ainda não carregado, mas já recebi pacote de mapa do servidor.`
- `Invalid/blocked URL from server: ...`

### `a/ct.class`
Likely UI/action enum or hotkey/action definitions.

Relevant strings:
- `Inventory`
- `Minimap`
- `OPEN_MINIMAP`
- `SHOWEXTENDEDINVENTORY`
- `USE_SKILL_1`
- `USE_SKILL_2`
- `Use Skill Attack`
- `Use Skill Defense`

### `a/fj.class`
Likely `GameScreen`.

Relevant strings:
- `GameScreen`
- `ConcurrentHashMap`
- references to `a/br` and `a/cq`

### `a/gb.class`
Likely minimap/settings UI.

Relevant strings:
- `JTME/map/minimap.dat`
- `Click to Walk`
- `Movement Indicator`
- `Show Creature Levels`

### `a/dl.class`
Likely inventory/skills UI.

Relevant strings:
- `Inventory`
- `Quest/Map`
- `Skill 1`
- `Skill 2`

## Confirmed packet helpers from decompiled files

Source files provided in `decompilar/`:

### `ilclass.py` writer mapping

- `aj(int)` => write one byte.
- `ak(int)` => write uint16/int16 little-endian.
- `al(int)` => write int32 little-endian.
- `B(String)` => write UTF-8 string with one-byte length prefix.
- `d(byte[])` => write raw bytes.
- `a()` => return final payload bytes.

### `ksclass.py` reader mapping

- `p()` => read uint8.
- `q()` => read uint16 little-endian.
- `r()` => read int32 little-endian.
- `a()` => read int64 little-endian.
- `f()` => read ISO-8859-1 string with one-byte length prefix; if length is 255, read uint16 extended length.
- `g()` => read UTF-8 string with fallback behavior.

### Framing

Login and game packets use:

```text
uint16_le payload_length
payload bytes
```

### Login payload candidate

From `bfclass.py`, the initial login payload is:

```text
u8  3
u8  36
str account
u8  client_minor/protocol = 22
u16 client_major/build = 126
u8  0
str password
```

Implemented in `bot/jtme_bot/protocol/` as local packet utilities and a diagnostic login client. Real login testing still requires a safe test account and manual confirmation of credential entry flow.

## Bot safety boundary

The bot implementation should enforce rules in code, not just UI/config:

- Movement origin anchor: character position when bot starts or reconnects.
- Max movement radius: Manhattan or Chebyshev distance <= 5 tiles, depending on game movement model.
- Reject pathing/click-walk outside allowed radius.
- No map roaming/search pathfinder.
- Allow only local combat decisions based on visible/currently received creatures.
- Allow loot only from visible/current local corpses/drops.
- Auto-reconnect allowed.
