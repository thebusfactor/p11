import cv2
import time

from model import light
from model.video import Video, open_video


def start():
    video = Video("C:/Users/Brandon/Documents/Git Projects/Bus-Factor/src/model/vid.avi")


    while(True):
        frame = video.get_frame()
        cv2.imwrite("frame.png", frame)
        if light.is_red(frame):
            print("Light is Red!")
        time.sleep(1)
