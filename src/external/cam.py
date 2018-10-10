# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2
from threading import Thread


class Cam:

    def __init__(self, path=0):
        """
            Initial method to set up the video feed. If there is not video at the specified
            location it will automatically use the live web cam footage.

            Parameters
            ----------
            path : String
                The location of the video footage to be used.
        """
        self.path = path
        self.video = self.open_video(path)

        self.video.set(3, 1280)
        self.video.set(4, 720)

        (self.grabbed, self.frame) = self.video.read()

        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.video.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

    def open_video(self, path):
        """
        Sets the video feed used by the program to the video location at the path specified in the parameters.

        Parameters
        ----------
        path : String
               The location of the video feed to be opened

        Returns
        -------
        video : VideoCapture
               The video capture of the video at the specified path
        """
        video = cv2.VideoCapture(path)
        return video
