# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from cv2 import VideoCapture


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
        self.video = open_video(path)

        self.video.set(3, 1280)
        self.video.set(4, 720)

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
        self.video = VideoCapture(self.path)


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
    video = VideoCapture(path)
    return video
