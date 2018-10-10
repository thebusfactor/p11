# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from pystray import Icon, Menu, MenuItem
from PIL import Image

from typing import Iterable


def make_menu() -> Iterable[MenuItem]:
    # yield MenuItem("Open GUI", lambda: GUI().run(), default=True, visible=True)
    yield MenuItem("left", lambda: print("left"), visible=True)
    yield MenuItem("click", lambda: print("left"))
    yield MenuItem("exit", lambda icon: icon.stop())


def start() -> None:
    icon = Icon("test", Image.open("bus.jpg"), menu=Menu(make_menu))
    icon.run()
