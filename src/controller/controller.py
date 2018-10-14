# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from controller.observer import Observer
from model.model import Model
from ui.debug_ui import DebugGUI
from model.ai import Ai


class Controller:

    def __init__(self, model: Model, ai: Ai, debug_ui: DebugGUI):
        """
                Initial method setting up controller observers and references to other classes.

                Parameters
                ----------
                model : Model
                    Reference to programs model class.
                ai : Ai
                    Reference to programs AI class.
                debug_ui : DebugGUI
                    Reference to programs debug UI class.
        """
        self.model = model
        self.debug_ui = debug_ui
        self.ai = ai

        self.tool_observer = ToolObserver(self.debug_ui)
        self.frame_observer_debug = FrameObserver(debug_ui.frame, debug_ui)

        self.classifications_observer_debug = ClassificationsObserver(debug_ui)
        self.classifications_observer_model = ClassificationsObserver(model)

        self.model.add_frame_observer(self.frame_observer_debug)
        self.model.add_tool_observer(self.tool_observer)

        self.ai.add_classifications_observer(self.classifications_observer_debug)
        self.ai.add_classifications_observer(self.classifications_observer_model)


class FrameObserver(Observer):

    def __init__(self, frame, update_target):
        self.frame = frame
        self.update_target = update_target

    def update(self, frame):
        """
            Updates the current frame for all classes which use the frame.

            Parameters
            -----------
            frame :  Cam
                the current frame of the camera being used

        """
        if frame is None:
            return
        self.frame = frame
        self.update_target.update_frame(frame)


class ClassificationsObserver(Observer):

    def __init__(self, update_target):
        self.update_target = update_target
        self.classifications = None

    def update(self, classifications):
        """
            Updates the current frame for all classes which use the frame.

            Parameters
            ----------
            classifications : []
                array of classified objects within the frame
        """
        if classifications is None:
            return
        self.classifications = classifications
        self.update_target.update_classifications(classifications)


class ToolObserver(Observer):
    def __init__(self, update_target):
        self.update_target = update_target
        self.line = None
        self.traffic_rect = None
        self.traffic_light_red = False

    def update(self):
        """
            Updates the current frame for all classes which use the frame.
        """
        if self.update_target.update_line() is not None:
            self.line = self.update_target.update_line()
        if self.update_target.update_traffic_rect() is not None:
            self.traffic_rect = self.update_target.update_traffic_rect()

    def get_traffic_rectangle(self):
        """
        Returns the rectangle object representing the traffic light object.

        Returns
        -------
        rect:
            Rectangle traffic light object.
        """
        if self.traffic_rect is None or len(self.traffic_rect) < 2:
            return -1
        return self.traffic_rect

    def get_line(self):
        """
        Returns the line object representing the intersection line.

        Returns
        -------
        line:
            intersection line object.
        """
        if self.line is None or len(self.line) < 2:
            return -1
        return self.line

    def set_traffic_light_red(self, traffic_light_red):
        """
        Sets whether the traffic light has been detected red or not,
        and passes that information into the debug_ui so the visual
        display of the traffic light detection can be shown.
        """
        self.traffic_light_red = traffic_light_red
        self.update_target.set_traffic_light_red(self.traffic_light_red)
