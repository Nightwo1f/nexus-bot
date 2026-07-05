"""
Opcode definitions for the TibiaME network protocol.

This module centralizes all opcode identifiers extracted from the
TibiaME client library (libtibiame-lib.so).

Opcodes are separated by direction:

    - ClientOpcode  -> packets sent from client to server
    - LoginOpcode   -> packets used during login stage
    - ServerOpcode  -> packets sent from server to client

Using enums prevents magic numbers and simplifies packet dispatching.
"""

from enum import IntEnum

# -------------------------------------------------
# Client → Server (game)
# -------------------------------------------------


class ClientOpcode(IntEnum):
    """
    Opcodes sent from client to server during gameplay.
    """

    CLIENT_READY = 14
    REQUEST_OUTFIT = 15
    QUIT_GAME = 20

    PONG = 30
    SNAPBACK_OK = 31

    GET_AUTOMAP = 40

    PAYMENT_SMS_RESULT = 60
    PAYMENT_NETWORK_RESULT = 65
    PAYMENT_RECEIPT = 66
    PAYMENT_BUSY = 69

    DIALOG_MENU_RESULT = 70
    DIALOG_LIST_RESULT = 71
    DIALOG_INPUT_RESULT = 72
    DIALOG_CANCEL = 73
    DIALOG_INVENTORY_RESULT = 74

    GO_NORTH = 100
    GO_EAST = 101
    GO_SOUTH = 102
    GO_WEST = 103

    GET_OBJECT = 110
    DROP_OBJECT = 111
    USE_OBJECT = 120

    LOOK_MAP = 130
    LOOK_INVENTORY = 131

    ATTACK = 140

    TALK = 150
    MESSAGE = 151
    ADDRESS_NPC = 152
    LEAVE_NPC = 153
    ANSWER_NPC = 154

    ENTER_SHOP = 160
    LEAVE_SHOP = 161

    RETRIEVE_OBJECT = 164
    STORE_OBJECT = 165
    CHANGE_DEPOT = 169

    SET_OUTFIT = 170


# -------------------------------------------------
# Client → Server (login phase)
# -------------------------------------------------


class LoginOpcode(IntEnum):
    """
    Opcodes used during the login phase.
    """

    SET_CONNECTION = 3
    GET_GRAPHIC_PACK = 12
    GET_SOUND = 20
    GET_UI = 21
    GET_UI_INFO = 22


# -------------------------------------------------
# Server → Client
# -------------------------------------------------


class ServerOpcode(IntEnum):
    """
    Opcodes sent from server to client.
    """

    START_GAME = 1

    LOGIN_ERROR_TEXT = 11
    CREATE_CHARACTER_INFO = 12
    OBJECT_REPRESENTATIONS = 13

    PING = 20

    AUTOMAP = 40
    AUTOMAP_OK = 41

    PREMIUM_STATUS = 51
    CIP_CREDITS_BALANCE = 52
    SHOW_INTERSTITIAL = 59

    PAYMENT_SMS = 60
    PAYMENT_NETWORK_DATA = 65
    PAYMENT_INAPP = 66
    PAYMENT_CONFIRM = 67
    PAYMENT_WEBSITE_FORWARDING = 68

    DIALOG_START = 70
    DIALOG_TEXT = 71
    DIALOG_INPUT = 72
    DIALOG_LIST = 73
    DIALOG_MENU = 74
    DIALOG_ABORT = 75
    DIALOG_INVENTORY = 76

    FULLSCREEN = 100
    ROW = 101
    SET_POSITION = 105

    SET_OBJECT = 110
    DELETE_OBJECT = 111
    STATIC_ANIMATION = 112
    SET_STATICS = 115

    OWN_PET_STATUS = 117
    CREATURE_STATUS_EX = 118
    CREATURE_STATUS = 119
    CREATURE_OUTFIT = 120

    MOVE_CREATURE = 121
    DELETE_CREATURE = 125
    CREATURE_INFO = 126
    SET_NEW_CREATURE = 127
    SET_OLD_CREATURE = 128

    ROTATE_CREATURE = 129
    GRAPHICAL_EFFECT = 130
    TEXTUAL_EFFECT = 131
    CREATURE_ANIMATION = 132
    PLAYER_ANIMATION = 133
    ROTATE_PLAYER = 134

    FULL_INVENTORY = 140
    SET_INVENTORY = 141
    DELETE_INVENTORY = 142
    BOOST_STATUS = 143

    FULL_STATUS = 150
    SET_STATUS_HP = 151
    SET_STATUS_MANA = 152
    SET_STATUS_EXP = 153
    SET_STATUS_LEVEL = 154
    SET_STATUS_GOLD = 155
    SET_STATUS_COOLDOWN = 156
    SET_STATUS_FLAGS = 157

    USER_DATA = 160
    SKILL_FULL = 161
    SKILL_STATUS = 162

    GUILD_MESSAGE = 169
    TALK = 170
    MESSAGE = 171
    ANSWERS = 172
    LEAVE_NPC = 173
    NPC_TALK = 174

    LEAVE_SHOP = 176
    DEPOT = 177
    SET_DEPOT = 178
    DELETE_DEPOT = 179

    GAME_MESSAGE = 180
    STATUS_MESSAGE = 181
    OBJECT_DESCRIPTION = 182

    OUTFIT_LIST = 184
    SEND_PM = 186
    DIALOG_SHOP = 188

    DIRECTIONAL_MARKER = 190
    TUTORIAL_HINT = 191
    SOUND_EFFECT = 192
    CHANGE_AMBIENT = 193
    QUEST_MISSION_STEP = 194

    TRACK_EVENT = 195
    TRACK_REVENUE_EVENT = 196

    QUIT_GAME = 255
