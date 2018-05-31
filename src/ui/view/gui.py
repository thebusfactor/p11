from kivy.app import App
from kivy.lang import Builder

from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from src.model import config
from ui.view.cameraview import CameraView

Builder.load_file('ui/view/gui.kv')


class MainView(FloatLayout):
    pass


class GUI(App):

    def build(self):
        Window.fullscreen = False
        return MainView()
