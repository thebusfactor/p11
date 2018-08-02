# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2
from collections import deque
from queue import Queue


class StoredFrames:

    def __init__(self):
        self.before_que = deque(maxlen=150)


    def add_frame(self, frame):
        self.que.append(frame)

    def clip_video(self):
        after_que = deque(maxlen=150)
"""
    general concept
    
    Add frames to collection during function, then when triggered add frames after then output video
    
    Ideas: 
    Static int to increment videos
    Work out and test pulling frames from collection into video
    Efficient storage of frames
    Threading issues
"""
#
# que = deque(maxlen=150)
#
# cap = cv2.VideoCapture(0)
#
# ## some videowriter props
# sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#
# fps = 20
# #fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# #fourcc = cv2.VideoWriter_fourcc('m', 'p', 'e', 'g')
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#
# ## open and set props
# vout = cv2.VideoWriter()
# vout.open('output.mp4',fourcc,fps,sz,True)


