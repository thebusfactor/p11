import cv2
import time

from model import light
from model.video import Video, open_video

video = Video("C:/Users/Brandon/Documents/Git Projects/Bus-Factor/src/model/vid.avi")

def start():
    while(True):
        frame = video.get_frame()
        cv2.imwrite("frame.png", frame)
        if light.is_red(frame):
            print("Light is Red!")
        time.sleep(0.1)

