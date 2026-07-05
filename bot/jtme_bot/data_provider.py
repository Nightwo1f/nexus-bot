from __future__ import annotations

from abc import ABC, abstractmethod
from random import randint

from .models import PlayerState, Progression, SlotUsage, StorageInfo, Vitals


class PlayerDataProvider(ABC):
    @abstractmethod
    def get_player_state(self) -> PlayerState:
        raise NotImplementedError


class MockPlayerDataProvider(PlayerDataProvider):
    def __init__(self) -> None:
        self._tick = 0

    def get_player_state(self) -> PlayerState:
        self._tick += 1
        hp = 820 + randint(-5, 5)
        mana = 430 + randint(-3, 3)
        exp_current = 124_500 + self._tick * 25
        exp_next = 130_000

        return PlayerState(
            character_name="Aguardando login",
            connection_status="Mock / desconectado",
            vitals=Vitals(
                hp_current=max(0, hp),
                hp_max=950,
                mana_current=max(0, mana),
                mana_max=520,
            ),
            progression=Progression(
                level=42,
                exp_current=exp_current,
                exp_next_level=exp_next,
            ),
            storage=StorageInfo(
                inventory=SlotUsage(free=18, total=32),
                depot=SlotUsage(free=74, total=100),
                depotmail=SlotUsage(free=9, total=20),
            ),
        )
