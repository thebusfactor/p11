import kivy
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from controller.observer import Observer
from kivy.graphics import *
from controller import crop
from model import config
from model.model import Model
from util.double_point import DoublePoint


class DrawableWidget(FloatLayout):
    TRANSPARENCY = 0.2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.light_state = Label()
        self.bus_state = Label()
        self.counter = -1
        self.draw_alert()

    def clear_line(self):
        lines = []
        for child in self.canvas.children[::-1]:
            if isinstance(child, kivy.graphics.vertex_instructions.Line):
                lines.append(child)
        if(len(lines) >= 2):
            for line in lines:
                self.canvas.remove(line)

    def clear_rectangle(self):
        for child in self.canvas.children[::-1]:
            if isinstance(child, kivy.graphics.vertex_instructions.Rectangle):
                self.canvas.remove(child)

    def add_observer(self, observer: Observer):
        self.observer = observer

    def on_touch_down(self, touch):
        self.observer.update(touch)

    def set_color(self, rgb: tuple):
        self.canvas.add(Color(rgb[0], rgb[1], rgb[2], self.TRANSPARENCY))

    def draw_red(self):
        self.remove_widget(self.light_state)
        self.light_state = Label(text="Light: Is Red", color=[1, 0, 0, 1], pos=(10, 400))
        self.add_widget(self.light_state)

    def draw_not_red(self):
        self.remove_widget(self.light_state)
        self.light_state = Label(text="Light: Not Red", color=[0, 1, 0, 1], pos=(10, 400))
        self.add_widget(self.light_state)

    def draw_line(self, x1, y1, touch):
        """
            Draws line based on current coordinates
        """
        self.set_color((1., 0, 0))
        self.canvas.add(Line(points=[x1, y1, touch.x, touch.y], width=2))
        self.set_color((1, 0, 0))

        #
        # self.canvas.add(Line(points=[x3, y3, x4, y4], width=2))
        # config.set_line(DoublePoint((x3, y3), (x4, y4)))

    def draw_rectangle(self, x1, y1, touch):
        """
            Draws rectangle based on current coordinates
        """

        width = abs(touch.x - x1)
        height = abs(touch.y - y1)

        self.set_color((1., 0, 0))

        pos = (0, 0)

        if (y1 - touch.y) < 0 and (x1 - touch.x) < 0:
            pos = (x1, y1)
        elif (x1 - touch.x) < 0:
            pos = (x1, touch.y)
        elif (y1 - touch.y) < 0:
            pos = (touch.x, y1)
        elif (x1 - touch.x) > 0:
            pos = (touch.x, touch.y)

        self.canvas.add(Rectangle(pos=pos, size=(width, height)))
        config.set_box(DoublePoint((pos[0], pos[1]), (pos[0] + width, pos[1] + height)))

    def draw_alert(self):
        self.counter += 1
        self.remove_widget(self.bus_state)
        self.bus_state = Label(text="Buses Skip Lights: " + str(self.counter), color=[1, 0, 0, 1], pos=(30, 375))
        self.add_widget(self.bus_state)
