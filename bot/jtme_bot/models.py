from dataclasses import dataclass


@dataclass(frozen=True)
class Vitals:
    hp_current: int
    hp_max: int
    mana_current: int
    mana_max: int

    @property
    def hp_percent(self) -> int:
        return _percent(self.hp_current, self.hp_max)

    @property
    def mana_percent(self) -> int:
        return _percent(self.mana_current, self.mana_max)


@dataclass(frozen=True)
class Progression:
    level: int
    exp_current: int
    exp_next_level: int

    @property
    def exp_missing(self) -> int:
        return max(0, self.exp_next_level - self.exp_current)

    @property
    def exp_percent(self) -> int:
        return _percent(self.exp_current, self.exp_next_level)


@dataclass(frozen=True)
class SlotUsage:
    free: int
    total: int

    @property
    def used(self) -> int:
        return max(0, self.total - self.free)

    @property
    def used_percent(self) -> int:
        return _percent(self.used, self.total)


@dataclass(frozen=True)
class StorageInfo:
    inventory: SlotUsage
    depot: SlotUsage
    depotmail: SlotUsage


@dataclass(frozen=True)
class PlayerState:
    character_name: str
    connection_status: str
    vitals: Vitals
    progression: Progression
    storage: StorageInfo


def _percent(current: int, total: int) -> int:
    if total <= 0:
        return 0
    return max(0, min(100, round((current / total) * 100)))
