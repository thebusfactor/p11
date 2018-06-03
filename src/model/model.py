import cv2
import time

from model import traffic_light
from external.video import Video


class Model:

    def __init__(self, video: Video, fps: int):
        self.video = video
        self.fps = fps
        self.frame = self.video.get_frame()

    def start(self):
        while True:
            self.frame = self.video.get_frame()
            cv2.imwrite("frame.png", self.frame)
            if traffic_light.is_red(self.frame):
                print("Light is Red!")
            time.sleep(1/self.fps)
