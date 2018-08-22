from controller.observer import Observer
from model.model import Model
from ui.debug_ui import DebugGUI


class Controller:

    def __init__(self, model: Model, debug_ui: DebugGUI):
        self.model = model
        self.debug_ui = debug_ui
        self.line_observer = ToolObservers(self.debug_ui)
        self.frame_observer_debug = FrameObserver(debug_ui.frame, debug_ui)
        self.classifications_observer_debug = ClassificationsObservers(debug_ui)
        self.model.add_frame_observer(self.frame_observer_debug)
        self.model.add_classifications_observer(self.classifications_observer_debug)
        self.model.add_tool_observer(self.line_observer)


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
        print(self.intersects)
