import tkinter as tk

from jtme_bot.data_provider import MockPlayerDataProvider
from jtme_bot.ui import BotApp


def main() -> None:
    root = tk.Tk()
    BotApp(root, MockPlayerDataProvider())
    root.mainloop()


if __name__ == "__main__":
    main()
