# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2


class Cam:

    def __init__(self, path=None):
        """
            Initial method to set up the video feed. If there is not video at the specified
            location it will automatically use the live web cam footage.

            Parameters
            ----------
            path : String
                The location of the video footage to be used.
        """
        if path is None:
            self.video = open_cam()
        else:
            self.path = path
            self.video = open_video(path)

    def get_frame(self):
        """
            Returns the current camera frame.

            Returns
            -------
            frame : Frame
                the current frame of the video feed being used.
        """
        ret, frame = self.video.read()
        return frame

    def reset_video(self):
        self.video = cv2.VideoCapture(self.path)


def open_video(path):
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


def open_cam():
    """
        Opens the devices webcam. Method called if there is no specified video path.

        Returns
        -------
        video : VideoCapture
            The video capture of the webcam.
    """
    video = cv2.VideoCapture(0)

    # n = 1
    # while video is None and n < 10:
    #     video = cv2.VideoCapture(n)
    #     print("trying source ", n)
    #     n += 1

    return video
