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

        self.tool_observer = ToolObservers(self.debug_ui)
        self.frame_observer_debug = FrameObserver(debug_ui.frame, debug_ui)

        self.classifications_observer_debug = ClassificationsObservers(debug_ui)
        self.classifications_observer_model = ClassificationsObservers(model)

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


class ClassificationsObservers(Observer):

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


class ToolObservers(Observer):
    def __init__(self, update_target):
        self.update_target = update_target
        self.line = None
        self.rect = None
        self.intersects = False

    def update(self):
        """
            Updates the current frame for all classes which use the frame.

            Parameters
            ----------
            classifications : []
                array of classified objects within the frame
        """
        if self.update_target.update_line() is not None:
            self.line = self.update_target.update_line()
        if self.update_target.update_rect() is not None:
            self.rect = self.update_target.update_rect()
        self.intersects = self.update_target.update_collision_boolean()
        # print(self.intersects)

    def get_rectangle(self):
        """
        Returns the rectangle object representing the traffic light object.

        Returns
        -------
        rect:
            Rectangle traffic light object.
        """
        if self.rect is None or len(self.rect) < 2:
            return -1
        return self.rect

    def get_intersects(self):
        return self.intersects

    def set_intersects_bool(self, value):
        self.intersects = value
