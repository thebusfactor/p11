# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2
from collections import deque
import time


class StoredFrames:
    count: int = 0

    def __init__(self, fps, res, length):
        self.before_que = deque(maxlen=length)
        self.after_que = deque(maxlen=length)
        self.count = 0

    def append_before(self, frame):
        self.before_que.append(frame)

    def append_after(self, frame):
        self.after_que.append(frame)

    def combine_videos(self):
        """
        Combines both frame lists and passes them through for conversion
        """
        b_q = list(self.before_que)
        a_q = list(self.after_que)
        combined = b_q + a_q
        self.convert_frames_to_video(combined)

    def convert_frames_to_video(self, frame_array):
        """
        Takes list of frames and converts them to a video
        :param frame_array: frames to be converted
        :return: output video of event
        """
        height, width, layers = frame_array[0].shape
        size = (width, height)
        date = time.strftime("%c")
        path_out = str(date) + '_' + str(self.count) + '.avi'
        self.count += 1
        out = cv2.VideoWriter(path_out, cv2.VideoWriter_fourcc(*'DIVX'), self.fps, size)

        for i in range(len(frame_array)):
            out.write(frame_array[i])
        out.release()
