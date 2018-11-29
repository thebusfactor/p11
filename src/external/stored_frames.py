# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from cv2 import VideoWriter, VideoWriter_fourcc
from threading import Thread
from collections import deque
import time


class StoredFrames:

    count: int = 0
    trigger: bool = False
    fps: int = -1
    length: int = -1
    res = None

    def __init__(self, fps, res, length):

        self.fps = fps
        self.res = res
        self.length = length

        self.before_que = deque(maxlen=length)
        self.after_que = deque(maxlen=length)
        self.count = 0

    def start_clipping(self):
        """
            Starts the clipping checks in parallel,
            as the operation of producing a video file is quite expensive
        """
        Thread(target=self.__run__).start()

    def trigger_event(self):
        self.trigger = True

    def append_frame(self, frame):
        """
            Appends frame to either the queue before or after the violation
        """

        if not self.trigger:
            self.before_que.append(frame)
        else:
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

            Parameters
            ----------
            frame_array : []
                Frames to be converted.
        """
        height, width, layers = frame_array[0].shape
        size = (width, height)
        date = time.strftime("%c")
        date = time.strftime("%Y-%m-%d %H:%M")
        path_out = str(date) + '_' + str(self.count) + '.avi'
        path_out = path_out.replace(" ", "_")
        path_out = path_out.replace(":", "")
        print(path_out)
        self.count += 1
        out = VideoWriter(path_out, VideoWriter_fourcc('M', 'J', 'P', 'G'), self.fps, size)

        for i in range(len(frame_array)):
            out.write(frame_array[i])
        out.release()
        self.trigger = False

    def __run__(self):
        """
            Continuously checks to see if the video queues are full.
            If the 'after' queue is full, and an event has been triggered, then build a video file of the violation
        """
        while True:
            if self.trigger and len(self.after_que) >= 120:
                self.combine_videos()
                self.after_que = deque(maxlen=self.length)
