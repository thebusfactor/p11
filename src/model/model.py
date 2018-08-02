#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2 as cv
import time

from controller.observer import Observer
from external.cam import Cam
from model.bus_detection import BusDetection
import model.output
from model.traffic_light import TrafficLight
from util.double_point import DoublePoint
from ui.debug_ui import DebugGUI


class Model:

    ui_name = "Bus-Factor"

    # frame_count: int = 30
    # red: bool = False
    # bus: bool = False

    def __init__(self, cam: Cam, fps: int, res):
        self.cam = cam
        self.fps = fps
        self.res = res
        self.frame = self.cam.get_frame()
        self.debug_ui = DebugGUI(self.frame)

    def start(self):
        while True:
            print("Starting Model")
            self.frame = self.cam.get_frame()
            self.debug_ui.update_frame(self.frame)

            if cv.waitKey(50) == 27:
                break
        cv.destroyAllWindows()


            # self.frame = self.video.get_frame()
            # self.observer.update(self.frame)
            # if self.frame is None:
            #     self.video.reset_video()
            #     self.frame = self.video.get_frame()
            # # if self.bus:
            # #     if self.frame_count % 300 == 0:
            # #         self.bus = False
            # # else:
            # #     self.red = False
            # #     self.bus_detection.detect(self.frame)
            # elif self.frame_count % 30 == 0:
            #     self.red = False
            #     self.bus_detection.detect(self.frame)
            #     # if self.traffic_light.check_traffic_light(self.frame, self.res):
            #     #     self.red = True
            #     #     img = self.bus_detection.crop(self.frame)
            #     #     check, z, colour = model.output.determine_bus(img)
            #     #     if check and colour != 'none':
            #     #         self.bus = True
            #     #         print("Bus crossed skipped light")
            #     #         print("colour: ", colour)
            #     #         print("z: ", z)
            #
            # time.sleep(1/self.fps)
            # self.frame_count += 1


    def add_observer(self, observer: Observer):
        self.observer = observer
