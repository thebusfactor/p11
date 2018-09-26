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

            # track bus position every frame
            buses = self.bus_tracker.update(self.classifications, self.res)

            # if traffic light rectangle has been placed down
            if self.tool_observers.get_traffic_rectangle() != -1:
                self.traffic_light.update_box(self.tool_observers.get_traffic_rectangle())
                red_light = self.traffic_light.check_traffic_light(self.frame, (1280, 720))

                if red_light:
                    # TODO make statement shorter/clean
                    if buses is not None and len(buses) > 0 and self.tool_observers is not None and self.tool_observers.get_line() != -1:
                        for bus in buses:
                            if not bus.get_has_intersected():
                                if self.detect_event(bus.tl_x, bus.tl_y, bus.br_x, bus.br_y, self.tool_observers.get_line()):
                                    print("intersection")
                                    bus.set_has_intersected(True)

            # ## TODO CHANGE
            # if i % self.fps == 0:
            #     if self.tool_observers.get_rectangle() != -1:
            #         self.traffic_light.update_box(self.tool_observers.get_rectangle())
            #         self.z_threshold_exceeded = self.traffic_light.check_traffic_light(self.frame, (1280, 720))
            #
            #         if self.z_threshold_exceeded:
            #             print("Tool get intersects:", self.tool_observers.get_intersects())
            #
            #             if self.tool_observers.get_intersects():
            #                 self.violation_count = BusCounter.traffic_violation_detected(BusCounter,
            #                                                                              count=self.violation_count)
            #                 self.tool_observers.set_intersects_bool(False)

            if cv.waitKey(50) == 27:
                self.stored_frames.trigger_event()
                break

            # If there is a violation
                # self.stored_frames.trigger_event()

            i += 1
            # if i % self.fps == 0:
                # print("I =", i % self.fps == 0)

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

    def detect_event(self, x1: int, y1: int, x2: int, y2: int, line_pt):
        """
            Method to check if a classified object is intersecting the intersection
            line specified by the user. point (x1, y2) are top left and (x2, y2)
            is bottom right of rectangle.

            Parameters
            ----------
            x1 : int
                x position of top left point of square
            y1 : int
                y position of top left point of square
            x2 : int
                x position of bottom right point of square
            y2 : int
                x position of bottom right point of square
        """
        if line_pt is not None:
            if len(line_pt) >= 2:

                line_x_points = []
                line_y_points = []

                x_width = (line_pt[1][0] - line_pt[0][0])
                y_width = (line_pt[1][1] - line_pt[0][1])

                x_iteration = (x_width/50)
                y_iteration = (y_width/50)

                # Required to account for different directions that the line can be drawn.
                current_x_point = line_pt[1][0]
                current_y_point = line_pt[1][1]
                y_iteration *= -1
                x_iteration *= -1

                # Iterates through the line and selects 50 intervals/points.
                for i in range(50):
                    line_x_points.append(current_x_point)
                    line_y_points.append(current_y_point)
                    current_x_point += x_iteration
                    current_y_point += y_iteration

                intersects = False

                # Iterates through the 50 points and checks if the point is within the box, if it is then
                # we can determine that the object intersects the line.
                while not intersects:
                    for i in range(50):
                        if self.contains(self, x1, y1, x2, y2, int(line_x_points[i]), int(line_y_points[i])):
                            intersects = True
                            cv.circle(self.frame, (int(line_x_points[i]), int(line_y_points[i])), 5, (244, 40, 0))
                        else:
                            intersects = False
                    break

        # print("Intersects bool:", self.intersects)
        return intersects

    @staticmethod
    def contains(self, x1: int, y1: int, x2: int, y2: int, px: int, py: int):
        """
            Check if point (px, py) is contained within rectangle [(x1, y1), (x2, y2)],
            where points are top left and bottom right respectively.

            Parameters
            ----------
            x1 : int
                x value of top left point of containing box.
            y1 : int
                y value of top left point of containing box.
            x2 : int
                x value of bottom right point of containing box.
            y2 : int
                y value of bottom right point of containing box.
            px : int
                x value of point that is being checked for.
            py : int
                y value of point that is being checked for.
        """
        return x1 <= px <= x2 and y1 <= py <= y2
