import sys
import threading

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivy.config import Config

from model.image import Image
from ui.view import myApp
from ui.view.myApp import CamApp

Config.set('kivy', 'window_icon', '/img/icon.ico')

from kivy.core.window import Window


Builder.load_string('''
<CameraView>:
    id : mainwidget
    orientation: 'vertical'
       
    Camera:
        id: camera
        resolution: (1920,1080)
        play: True 
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
            on_press: mainwidget.capture(camera)
''')


class CameraView(FloatLayout):

    def line_select(self):
        pass
    def light_select(self):
        pass
    def open_config(self):
        pass
    def capture(self, cam):
        CamApp.screengrab(CamApp,cam, numImage=2)


class GUI(App):

    def build(self):
        Window.fullscreen = False
        return CameraView()
