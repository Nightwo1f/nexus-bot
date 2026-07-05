from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from .config import APP_TITLE, MAX_AUTO_MOVE_TILES, UI_REFRESH_MS
from .data_provider import PlayerDataProvider
from .models import PlayerState, SlotUsage


class BotApp(ttk.Frame):
    def __init__(self, root: tk.Tk, provider: PlayerDataProvider) -> None:
        super().__init__(root, padding=16)
        self.root = root
        self.provider = provider
        self.root.title(APP_TITLE)
        self.root.minsize(520, 520)

        self.character_var = tk.StringVar(value="-")
        self.status_var = tk.StringVar(value="-")
        self.level_var = tk.StringVar(value="-")
        self.hp_var = tk.StringVar(value="-")
        self.mana_var = tk.StringVar(value="-")
        self.exp_current_var = tk.StringVar(value="-")
        self.exp_next_var = tk.StringVar(value="-")
        self.exp_missing_var = tk.StringVar(value="-")
        self.inventory_var = tk.StringVar(value="-")
        self.depot_var = tk.StringVar(value="-")
        self.depotmail_var = tk.StringVar(value="-")

        self.hp_bar: ttk.Progressbar
        self.mana_bar: ttk.Progressbar
        self.exp_bar: ttk.Progressbar
        self.inventory_bar: ttk.Progressbar
        self.depot_bar: ttk.Progressbar
        self.depotmail_bar: ttk.Progressbar

        self._configure_style()
        self._build()
        self._refresh()

    def _configure_style(self) -> None:
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Segoe UI", 18, "bold"))
        style.configure("Section.TLabelframe.Label", font=("Segoe UI", 10, "bold"))
        style.configure("Safety.TLabel", foreground="#8a4b00")

    def _build(self) -> None:
        self.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        header = ttk.Frame(self)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        header.columnconfigure(0, weight=1)

        ttk.Label(header, text=APP_TITLE, style="Title.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(header, textvariable=self.status_var).grid(row=0, column=1, sticky="e")

        self._build_character_section(row=1)
        self._build_vitals_section(row=2)
        self._build_experience_section(row=3)
        self._build_storage_section(row=4)

        ttk.Label(
            self,
            text=f"Movimento automático limitado a {MAX_AUTO_MOVE_TILES} blocos.",
            style="Safety.TLabel",
        ).grid(row=5, column=0, sticky="w", pady=(12, 0))

    def _build_character_section(self, row: int) -> None:
        frame = ttk.LabelFrame(self, text="Personagem", padding=12, style="Section.TLabelframe")
        frame.grid(row=row, column=0, sticky="ew", pady=6)
        frame.columnconfigure(1, weight=1)

        self._add_value_row(frame, 0, "Nome", self.character_var)
        self._add_value_row(frame, 1, "Nível", self.level_var)

    def _build_vitals_section(self, row: int) -> None:
        frame = ttk.LabelFrame(self, text="HP e Mana", padding=12, style="Section.TLabelframe")
        frame.grid(row=row, column=0, sticky="ew", pady=6)
        frame.columnconfigure(1, weight=1)

        self._add_value_row(frame, 0, "HP", self.hp_var)
        self.hp_bar = ttk.Progressbar(frame, maximum=100)
        self.hp_bar.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 8))

        self._add_value_row(frame, 2, "Mana", self.mana_var)
        self.mana_bar = ttk.Progressbar(frame, maximum=100)
        self.mana_bar.grid(row=3, column=0, columnspan=2, sticky="ew")

    def _build_experience_section(self, row: int) -> None:
        frame = ttk.LabelFrame(self, text="Experiência", padding=12, style="Section.TLabelframe")
        frame.grid(row=row, column=0, sticky="ew", pady=6)
        frame.columnconfigure(1, weight=1)

        self._add_value_row(frame, 0, "EXP atual", self.exp_current_var)
        self._add_value_row(frame, 1, "EXP próximo nível", self.exp_next_var)
        self._add_value_row(frame, 2, "EXP faltando", self.exp_missing_var)
        self.exp_bar = ttk.Progressbar(frame, maximum=100)
        self.exp_bar.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(8, 0))

    def _build_storage_section(self, row: int) -> None:
        frame = ttk.LabelFrame(self, text="Espaços disponíveis", padding=12, style="Section.TLabelframe")
        frame.grid(row=row, column=0, sticky="ew", pady=6)
        frame.columnconfigure(1, weight=1)

        self._add_value_row(frame, 0, "Inventário", self.inventory_var)
        self.inventory_bar = ttk.Progressbar(frame, maximum=100)
        self.inventory_bar.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 8))

        self._add_value_row(frame, 2, "Depot", self.depot_var)
        self.depot_bar = ttk.Progressbar(frame, maximum=100)
        self.depot_bar.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 8))

        self._add_value_row(frame, 4, "Depotmail", self.depotmail_var)
        self.depotmail_bar = ttk.Progressbar(frame, maximum=100)
        self.depotmail_bar.grid(row=5, column=0, columnspan=2, sticky="ew")

    def _add_value_row(self, parent: ttk.Frame, row: int, label: str, value: tk.StringVar) -> None:
        ttk.Label(parent, text=f"{label}:").grid(row=row, column=0, sticky="w", padx=(0, 10), pady=2)
        ttk.Label(parent, textvariable=value).grid(row=row, column=1, sticky="e", pady=2)

    def _refresh(self) -> None:
        self._render(self.provider.get_player_state())
        self.root.after(UI_REFRESH_MS, self._refresh)

    def _render(self, state: PlayerState) -> None:
        self.character_var.set(state.character_name)
        self.status_var.set(state.connection_status)
        self.level_var.set(str(state.progression.level))

        self.hp_var.set(f"{state.vitals.hp_current:,} / {state.vitals.hp_max:,}")
        self.mana_var.set(f"{state.vitals.mana_current:,} / {state.vitals.mana_max:,}")
        self.hp_bar["value"] = state.vitals.hp_percent
        self.mana_bar["value"] = state.vitals.mana_percent

        self.exp_current_var.set(f"{state.progression.exp_current:,}")
        self.exp_next_var.set(f"{state.progression.exp_next_level:,}")
        self.exp_missing_var.set(f"{state.progression.exp_missing:,}")
        self.exp_bar["value"] = state.progression.exp_percent

        self._render_slot_usage(state.storage.inventory, self.inventory_var, self.inventory_bar)
        self._render_slot_usage(state.storage.depot, self.depot_var, self.depot_bar)
        self._render_slot_usage(state.storage.depotmail, self.depotmail_var, self.depotmail_bar)

    def _render_slot_usage(
        self,
        usage: SlotUsage,
        text_var: tk.StringVar,
        progressbar: ttk.Progressbar,
    ) -> None:
        text_var.set(f"{usage.free:,} livres / {usage.total:,} total")
        progressbar["value"] = usage.used_percent
