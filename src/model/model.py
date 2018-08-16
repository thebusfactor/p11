#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2 as cv

from controller.observer import Observer
from external.cam import Cam
from external.stored_frames import StoredFrames
from model.ai import start_ai
from model.ai import classify

class Model:

    ui_name = "Bus-Factor"
    frame_observers = []
    classifications_observers = []

    frame_count: int = 30
    fps_to_check: int = 2
    # red: bool = False
    # bus: bool = False

    def __init__(self, cam: Cam, fps: int, res=(1280, 720)):
        self.cam = cam
        self.fps = fps
        self.frame = self.cam.get_frame()
        self.vid_clipper = StoredFrames(fps, res, 150)
        start_ai()

    def start(self):
        cur_frame = 0
        while True:
            # only check 'fps_to_check' frames per second.
            cur_frame += 1
            self.frame = self.cam.get_frame()
            if cur_frame >= self.frame_count / self.fps_to_check:
                self.update_classifications_observer(classify(self.frame))
                # upon event
                    # call method in StoredFrames to clip event
                cur_frame = 0
            self.update_frame_observer(self.frame)
            if cv.waitKey(50) == 27:
                break
        cv.destroyAllWindows()

    def add_frame_observer(self, observer: Observer):
        self.frame_observers.append(observer)

    def add_classifications_observer(self, observer: Observer):
        self.classifications_observers.append(observer)

    def update_frame_observer(self, frame):
        for frame_observer in self.frame_observers:
            frame_observer.update(frame)

    def update_classifications_observer(self, classifications):
        for classifications_observer in self.classifications_observers:
            classifications_observer.update(classifications)
