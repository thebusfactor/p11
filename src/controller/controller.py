from controller.observer import Observer
from model.model import Model
from ui.debug_ui import DebugGUI
from model.ai import Ai
from util.double_point import DoublePoint


class Controller:

    def __init__(self, model: Model, ai: Ai, debug_ui: DebugGUI):
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
        if frame is None:
            return
        self.frame = frame
        self.update_target.update_frame(frame)


class ClassificationsObservers(Observer):

    def __init__(self, update_target):
        self.update_target = update_target
        self.classifications = None

    def update(self, classifications):
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
        if self.update_target.update_line() is not None:
            self.line = self.update_target.update_line()
        if self.update_target.update_rect() is not None:
            self.rect = self.update_target.update_rect()
        self.intersects = self.update_target.update_collision_boolean()
        # print(self.intersects)

    def get_rectangle(self):
        if self.rect is None or len(self.rect) < 2:
            return -1
        return DoublePoint(self.rect[0], self.rect[1])
