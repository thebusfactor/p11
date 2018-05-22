from pystray import Icon, Menu, MenuItem
from PIL import Image

from typing import Iterable

def make_menu() -> Iterable[MenuItem]:
    yield MenuItem("left", lambda: print("left"), default=True, visible=False)
    yield MenuItem("click", lambda: print("left"))
    yield MenuItem("exit", lambda icon: icon.stop())


def start() -> None:
    icon = Icon("test", Image.open("bus.jpg"), menu=Menu(make_menu))
    icon.run()
