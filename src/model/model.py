import cv2
import time

from model import traffic_light
from external.video import Video
from model.traffic_light import TrafficLight
from util.double_point import DoublePoint


class Model:

    frame_count: int = 0

    def __init__(self, video: Video, fps: int, res):
        self.video = video
        self.fps = fps
        self.res = res
        self.frame = self.video.get_frame()
        self.traffic_light = TrafficLight()
        self.traffic_light.box = DoublePoint((0, 0), (res[0], res[1]))

    def start(self):
        while True:
            self.frame = self.video.get_frame()
            if self.frame_count % 30 == 0:
                if self.traffic_light.check_traffic_light(self.frame, self.res):
                    print("Light is red")
            time.sleep(1/self.fps)
            self.frame_count += 1
