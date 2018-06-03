from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

# Credit: https://gist.github.com/ExpandOcean/de261e66949009f44ad2 for texture method

class Cv2FrameTexture(Image):
    def __init__(self, capture, fps, **kwargs):
        super(Cv2FrameTexture, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        if frame is None:
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if ret:
            flipped_frame = cv2.flip(frame, 0)
            frame_bytes = flipped_frame.tostring()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(frame_bytes, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = image_texture