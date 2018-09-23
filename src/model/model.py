# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2 as cv

from controller.observer import Observer
from external.cam import Cam
from external.stored_frames import StoredFrames
from model.ai import Ai
import model.bus_counter as count_gen
from model.bus_tracker import BusTracker
from model.bus_counter import BusCounter
from model.traffic_light import TrafficLight


class Model:
    frame_observers = []
    tool_observers: Observer

    violation_count: int = 0
    red_light: bool = True
    z_threshold_exceeded: bool

    def __init__(self, cam: Cam, ai: Ai, fps: int, res=(1280, 720)):
        self.classifications = None
        self.cam = cam
        self.res = res
        self.fps = fps
        self.ai = ai
        self.frame = self.cam.get_frame()
        self.vid_clipper = StoredFrames(fps, self.res, 150)
        self.ai.start_ai()
        self.traffic_light = TrafficLight()
        self.stored_frames = StoredFrames(self.fps, self.res, 120)
        self.stored_frames.start_clipping()
        self.bus_tracker = BusTracker()
        self.z_threshold_exceeded = False

    def start(self):
        """
            Method sets up the frame object and updates the classes which observe the frame object.
        """
        i = 0
        while True:

            # only check 'fps_to_check' frames per second.
            self.frame = self.cam.get_frame()
            self.stored_frames.append_frame(self.frame)

            # self.stored_frames.append_frame(self.frame, self.red_light)
            self.ai.update_ai_frame(self.frame)
            self.update_frame_observer(self.frame)
            self.update_tool_observer()

            if self.classifications is not None:
                self.bus_tracker.update(self.classifications, self.res)

            if self.tool_observers.get_rectangle() != -1:
                self.traffic_light.update_box(self.tool_observers.get_rectangle())
                print(self.traffic_light.check_traffic_light(self.frame, (1280, 720)))

            if i % self.fps == 0:
                if self.tool_observers.get_rectangle() != -1:
                    self.traffic_light.update_box(self.tool_observers.get_rectangle())
                    self.z_threshold_exceeded = self.traffic_light.check_traffic_light(self.frame, (1280, 720))

                    if self.z_threshold_exceeded:
                        print("Tool get intersects:", self.tool_observers.get_intersects())

                        if not self.tool_observers.get_intersects():
                            print("VIOLATION OCCURRED")
                            # self.violation_count = bus_counter.traffic_violation_detected(self.violation_count)
                            self.violation_count = BusCounter.traffic_violation_detected(BusCounter, count=self.violation_count)
                            self.tool_observers.set_intersects_bool()

            if cv.waitKey(50) == 27:
                self.stored_frames.trigger_event()
                break

            # If there is a violation
                # self.stored_frames.trigger_event()

            i += 1
            if i % self.fps == 0:
                print("I =", i % self.fps == 0)

        cv.destroyAllWindows()

    def update_classifications(self, classifications):
        """
            Update the classifications when new objects are detected.
        """
        self.classifications = classifications

    def add_frame_observer(self, observer: Observer):
        """
            Adds an observer to the model to observe the frame.

            Parameters
            ----------
            observer : Observer
                The observer to be added.
        """
        self.frame_observers.append(observer)

    def update_frame_observer(self, frame):
        """
            Updates the frame for every observer of the model.

           Parameters
           ----------
           frame : Frame
               Current frame from video input.
        """
        for frame_observer in self.frame_observers:
            frame_observer.update(frame)

    def add_tool_observer(self, observer: Observer):
        """
           Adds an observer for the line tool of the model.

           Parameters
           ----------
           observer : Observer
               The observer to be added to the model.
        """
        self.tool_observers = observer

    def update_tool_observer(self):
        """
            Updates the line tool for every observer of the model.
        """
        self.tool_observers.update()
