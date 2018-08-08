#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2 as cv
import time

from controller.observer import Observer
from external.cam import Cam
from external.stored_frames import StoredFrames
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
        self.vid_clipper = StoredFrames(fps, res, 150)
        self.debug_ui = DebugGUI(self.frame)

    def start(self):
        while True:
            print("Starting Model")
            self.frame = self.cam.get_frame()
            self.debug_ui.update_frame(self.frame)
            # upon event
                # call method in StoredFrames to clip event
            if cv.waitKey(50) == 27:
                break
        cv.destroyAllWindows()


    def add_observer(self, observer: Observer):
        self.observer = observer
