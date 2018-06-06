import cv2
import time

from model import traffic_light
from external.video import Video
from model.traffic_light import TrafficLight
from util.double_point import DoublePoint


class Model:

    def __init__(self, video: Video, fps: int):
        self.video = video
        self.fps = fps
        self.frame = self.video.get_frame()
        self.traffic_light = TrafficLight()
        self.traffic_light.box = DoublePoint((200, 200), (800, 800))

    def start(self):
        while True:
            self.frame = self.video.get_frame()
            if self.traffic_light.check_traffic_light(self.frame):
                print("Light is red")
            time.sleep(1/self.fps)
