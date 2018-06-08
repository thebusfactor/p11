import cv2
import time

from controller.observer import Observer
from model import traffic_light
from external.video import Video
from model.bus_detection import BusDetection
from model.traffic_light import TrafficLight
from util.double_point import DoublePoint


class Model:

    frame_count: int = 30
    red: bool = False

    def __init__(self, video: Video, fps: int, res):
        self.video = video
        self.fps = fps
        self.res = res
        self.frame = self.video.get_frame()
        self.traffic_light = TrafficLight()
        self.bus_detection = BusDetection()
        self.traffic_light.box = DoublePoint((0, 0), (1, 1))

    def start(self):
        while True:
            self.frame = self.video.get_frame()
            self.observer.update(self.frame)
            if self.frame is None:
                self.video.reset_video()
                self.frame = self.video.get_frame()
            if self.frame_count % 30 == 0:
                self.red = False
                if self.traffic_light.check_traffic_light(self.frame, self.res):
                    self.red = True
                    self.bus_detection.crop(self.frame)
            time.sleep(1/self.fps)
            self.frame_count += 1


    def add_observer(self, observer: Observer):
        self.observer = observer
