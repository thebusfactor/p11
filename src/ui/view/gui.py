import sys
import threading

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivy.config import Config

from model.image import Image

Config.set('kivy', 'window_icon', '/img/icon.ico')

from kivy.core.window import Window


Builder.load_string('''
<CameraView>:
    orientation: 'vertical'
       
    Camera:
        id: camera
        resolution: (1920,1080)
        play: False 
        pos: 0,0
        
    GridLayout:
        rows: 2
        row_force_default: True
        row_default_height: 20
        cols: 4
        size_hint: (1,1)
        Button:
            text: 'Configs'
        Button:
            text: 'Set Lights'
        Button:
            text: 'Set Line'
        Button:
            text: 'Capture'
''')


class CameraView(FloatLayout):

    def build_config(self):
        pass
    def line_select(self):
        pass
    def light_select(self):
        pass
    def open_config(self):
        pass




class GUI(App):

    def build(self):
        return CameraView()
