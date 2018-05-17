from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config
#Config.set('kivy', 'window_icon', 'icon.ico')
import time

# rows=1, row_force_default = True, row_default_height = 20, cols = 4, size_hint = (1000,1

Builder.load_string('''
<CameraView>:
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
''')


class CameraView(FloatLayout):
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