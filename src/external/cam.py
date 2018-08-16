#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2


class Cam:

    def __init__(self, path=None):
        if path is None:
            self.video = open_cam()
        else:
            self.path = path
            self.video = open_cam()

    def get_frame(self):
        ret, frame = self.video.read()
        return frame

    def reset_video(self):
        self.video = cv2.VideoCapture(self.path)


def open_video(path):
    video = cv2.VideoCapture(path)
    return video


def open_cam():
    video = cv2.VideoCapture(0)
    return video
