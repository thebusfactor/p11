# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11


def clip_frame(frame, point, res):
    """
        Clips the current frame given the parameters.

        Parameters
        ----------
        frame : Frame
            Current frame of the video feed being used.
        double_point : DoublePoint
            ares that the frame must be clipped within.
        res : []
            resolution of the video feed.

        Returns
        -------
        f : Frame
            Clipped frame given the parameters.
    """
    p1 = point[0]
    p2 = point[1]
    x1 = int(p1[0])
    x2 = int(p2[0])
    y1 = int(res[1] - p1[1])
    y2 = int(res[1] - p2[1])

    f = frame[y2: y1, x1: x2]
    return f
