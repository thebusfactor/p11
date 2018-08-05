# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2
from collections import deque
from queue import Queue
import cv2 as cv
import time

from future.moves import collections

from controller.observer import Observer
from external.cam import Cam
from model.bus_detection import BusDetection
import model.output
from model.traffic_light import TrafficLight
from util.double_point import DoublePoint
from ui.debug_ui import DebugGUI

# class StoredFrames:
#
#     def __init__(self):
#


"""
    general concept

    Add frames to collection during function, then when triggered add frames after then output video

    Ideas:
    Static int to increment videos
    Work out and test pulling frames from collection into video
    Efficient storage of frames
    Threading issues
"""

def convert_frames_to_video(frame_array, path_out, fps):
    height, width, layers = frame_array[0].shape
    size = (width, height)

    out = cv2.VideoWriter(path_out, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()


def main():
    cam = Cam()
    fps = 24
    res = (1280, 720)
    frame = cam.get_frame()
    debug_ui = DebugGUI(frame)
    before_que = deque(maxlen=120)
    after_que = deque(maxlen=240)
    print("Pre model")
    count = 0
    after = False
    while True:
        #print("Starting Model")
        frame = cam.get_frame()
        debug_ui.update_frame(frame)

        if cv.waitKey(50) == 27:
            after = True

        count += 1
        if count % 30 == 0:
            print('Before: ' + str(len(before_que)) + '\n')
            print('After: ' + str(len(after_que)))

        if after:
            after_que.append(frame)
        else:
            before_que.append(frame)

        if len(after_que) >= 120:
            break

    event = 0
    path_out = 'video' + str(event) + '.avi'
    b_q = list(before_que)
    a_q = list(after_que)
    combined = b_q + a_q
    convert_frames_to_video(combined, path_out, fps)
    cv.destroyAllWindows()


main()