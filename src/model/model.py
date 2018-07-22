#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

import time

from external.video import Video
from model.bus_detection import BusDetection
import model.output
from model.traffic_light import TrafficLight
from util.double_point import DoublePoint


class Model:

    frame_count: int = 30
    red: bool = False
    bus: bool = False

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
            if self.bus:
                if self.frame_count % 300 == 0:
                    self.bus = False
            elif self.frame_count % 30 == 0:
                self.red = False
                if self.traffic_light.check_traffic_light(self.frame, self.res):
                    self.red = True
                    img = self.bus_detection.crop(self.frame)
                    check, z, colour = model.output.determine_bus(img)
                    if check and colour != 'none':
                        self.bus = True
                        print("Bus crossed skipped light")
                        print("colour: ", colour)
                        print("z: ", z)

            time.sleep(1/self.fps)
            self.frame_count += 1


    def add_observer(self, observer: Observer):
        self.observer = observer
