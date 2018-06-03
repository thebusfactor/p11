from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
from kivy.uix.widget import Widget
import kivy
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import *
from model import config
from ui.view.cameraview import Draw
from util.double_point import DoublePoint


class KivyCam(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCam, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture


class CameraView(App):
    Builder.load_file('ui/view/gui.kv')

    def __init__(self, video, fps: int, **kwargs):
        super().__init__(**kwargs)
        self.capture = video.video
        self.kivy_cam = KivyCam(capture=self.capture, fps=fps)
        self.button = Button(text='Hello world', font_size=14)

    def test(self):
        print("hi")

    def build(self):
        Window.size = (750, 450)
        parent = Widget()
        parent.size = (750, 50)

        self.kivy_cam.pos = (0,-40)
        self.kivy_cam.size = (parent.size[0],500)

        draw = Draw()

        parent.add_widget(self.kivy_cam)
        parent.add_widget(setup_button(parent, draw))
        parent.add_widget(draw)

        return parent

    def on_stop(self):
        self.capture.release()


kivy_camera = None

def setup_button(parent: Widget, draw: Draw):
    button_layout = GridLayout(pos=(0, 395))
    button_layout.rows = 2
    button_layout.row_force_default = True
    button_layout.row_default_height = 20
    button_layout.cols = 4
    button_layout.size = (parent.size[0], 50)

    clear_button = Button(text='Clear', on_press=draw.delete_object)

    set_lights_button = Button(text='Set Lights', on_press=draw.set_rectangle)
    set_line_button = Button(text='Set Line', on_press=draw.set_line)
    capture_button = Button(text='Capture', on_press=draw.capture)


    button_layout.add_widget(clear_button)
    button_layout.add_widget(set_lights_button)
    button_layout.add_widget(set_line_button)
    button_layout.add_widget(capture_button)
    return button_layout


