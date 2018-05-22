from pystray import Icon, Menu, MenuItem
from PIL import Image

from typing import Iterable

from ui.view import gui


def make_menu() -> Iterable[MenuItem]:
    yield MenuItem("left", lambda: print("left"), default=True, visible=False)
    yield MenuItem("click", lambda: start_ui())
    yield MenuItem("exit", lambda icon: icon.stop())


def start() -> None:
    icon = Icon("test", Image.open("bus.jpg"), menu=Menu(make_menu))
    icon.run()


def start_ui():
    gui.GUI()
