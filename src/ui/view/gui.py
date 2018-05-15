'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import time

# rows=1, row_force_default = True, row_default_height = 20, cols = 4, size_hint = (1000,1

Builder.load_string('''
<CameraView>:
    orientation: 'vertical'
    GridLayout:
        rows: 1
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
    Camera:
        id: camera
        resolution: (1920,1080)
        play: True''')


class CameraView(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class GUI(App):

    def build(self):
        return CameraView()


Window.fullscreen = False
GUI().run()