#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

# Credit: https://gist.github.com/ExpandOcean/de261e66949009f44ad2 for texture method


class Cv2FrameTexture(Image):
    def __init__(self, fps, **kwargs):
        super(Cv2FrameTexture, self).__init__(**kwargs)
        self.frame = None
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        if self.frame is not None:
            flipped_frame = cv2.flip(self.frame, 0)
            frame_bytes = flipped_frame.tostring()
            image_texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(frame_bytes, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = image_texture

    def update_frame(self, frame):
        self.frame = frame