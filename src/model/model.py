# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2 as cv

from controller.observer import Observer
from external.cam import Cam
from external.stored_frames import StoredFrames
from model.ai import Ai
import model.bus_counter as count_gen
from model.traffic_light import TrafficLight


class Model:
    frame_observers = []
    tool_observers: Observer

    violation_count: int = 0

    def __init__(self, cam: Cam, ai: Ai, fps: int, res=(1280, 720)):
        self.classifications = None
        self.cam = cam
        self.fps = fps
        self.ai = ai
        self.frame = self.cam.get_frame()
        self.vid_clipper = StoredFrames(fps, res, 150)
        self.ai.start_ai()
        self.traffic_light = TrafficLight()

    def start(self):

        # need to move to when violation has been detected, not initially on startup
        self.violation_count = count_gen.traffic_violation_detected(self.violation_count)

        while True:
            # only check 'fps_to_check' frames per second.
            self.frame = self.cam.get_frame()

            self.ai.update_ai_frame(self.frame)
            self.update_frame_observer(self.frame)
            self.update_tool_observer()

            if self.tool_observers.get_rectangle() != -1:
                self.traffic_light.update_box(self.tool_observers.get_rectangle())
                # print(self.traffic_light.check_traffic_light(self.frame, (1280, 720)))


            if cv.waitKey(50) == 27:
                break
        cv.destroyAllWindows()

    def update_classifications(self, classifications):
        self.classifications = classifications

    def add_frame_observer(self, observer: Observer):
        self.frame_observers.append(observer)

    def update_frame_observer(self, frame):
        for frame_observer in self.frame_observers:
            frame_observer.update(frame)

    def add_tool_observer(self, observer: Observer):
        self.tool_observers = observer

    def update_tool_observer(self):
        self.tool_observers.update()
