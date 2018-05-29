from kivy.app import App
from kivy.lang import Builder

from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from model import config
from ui.view.cameraview import CameraView

Builder.load_string('''
<MainView>:
    id : mainwidget
    orientation: 'vertical'

    CameraView:
        id: cameraView

    GridLayout:
        rows: 2
        row_force_default: True
        row_default_height: 20
        cols: 4
        size_hint: (1,1)
        Button:
            text: 'Clear'
            one_press: cameraView.delete_object()
        Button:
            text: 'Set Lights'
            on_press: cameraView.set_rectangle()
        Button:
            text: 'Set Line'
            on_press: cameraView.set_line()
        Button:
            text: 'Capture'
            on_press: cameraView.capture()
''')


class MainView(FloatLayout):
    pass


class GUI(App):

    def build(self):
        Window.fullscreen = False
        ##config setup here
        config.reset_config()
        return MainView()
