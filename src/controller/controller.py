from controller.observer import Observer
from model.model import Model
from ui.debug_ui import DebugGUI


class Controller:

    def __init__(self, model: Model, debug_ui: DebugGUI):
        self.model = model
        self.debug_ui = debug_ui
        self.frame_observer_debug = FrameObserver(debug_ui.frame, debug_ui)
        self.classifications_observer_debug = ClassificationsObservers(debug_ui)
        self.model.add_frame_observer(self.frame_observer_debug)
        self.model.add_classifications_observer(self.classifications_observer_debug)


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
