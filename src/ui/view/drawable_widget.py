import kivy
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from controller.observer import Observer
from kivy.graphics import *

from model import config
from util.double_point import DoublePoint


class DrawableWidget(FloatLayout):

    TRANSPARENCY = 0.2

    def clear_line(self):
        for child in self.canvas.children[::-1]:
            if isinstance(child, kivy.graphics.vertex_instructions.Line):
                self.canvas.remove(child)

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

    def draw_line(self, x1, y1, touch):
        """
            Draws line based on current coordinates
        """
        self.set_color((1., 0, 0))
        self.canvas.add(Line(points=[x1, y1, touch.x, touch.y], width=2))
        self.set_color((1, 0, 0))

        gradient = (touch.y - y1) / (touch.x - x1)
        constant = y1 / ((gradient if gradient != 0 else 1) * x1)

        down_by = 400

        y3 = y1 - down_by
        x3 = x1 - (touch.x - x1)

        y4 = touch.y - down_by
        x4 = touch.x - (touch.x - x1)

        self.set_color((0, 1, 0))

        # ensure that shape is still within screen bounds
        if (y3 < 0):
            y3 = 0
        if (y4 < 0):
            y4 = 0
        if (x3 < 0):
            x3 = 0
        if (x4 < 0):
            x4 = 0

        self.canvas.add(Line(points=[x3, y3, x4, y4], width=2))
        config.set_line(DoublePoint((x3, y3), (x4, y4)))

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

    #TODO: currently called when set rectangle button is pressed, this should be changed to be called when incident occurs. 
    def draw_alert(self):

        popup = Popup(title = 'Warning !', content=Label(text='Incident Occured!'), size=(70,10), size_hint=(0.5, 0.5))
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 5)