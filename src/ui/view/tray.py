from pystray import MenuItem as Item, Menu
import pystray
from PIL import Image


def display():
    image = Image.open("bus.jpg")
    menu: Menu = (Item('name', action),
                  Item('name', action))
    icon = pystray.Icon("name", image, "title", menu)
    icon.run(setup)


def setup(icon):
    icon.visible = True


def action():
    print("hi")
