#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

from util.double_point import DoublePoint


def clip_frame(frame, double_point: DoublePoint, res):
    p1 = double_point.point1
    p2 = double_point.point2
    x1 = int(p1[0])
    x2 = int(p2[0])
    y1 = int(res[1] - p1[1])
    y2 = int(res[1] - p2[1])

    # WARNING KIVY 0,0 STARTS AT BOTTOM LEFT
    # CV2 0,0 START AT TOP LEFT (THE NORMAL WAY)
    f = frame[y2: y1, x1: x2]
    return f
