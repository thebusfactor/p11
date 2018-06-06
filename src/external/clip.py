import cv2

from util.double_point import DoublePoint


def clip_frame(frame, double_point: DoublePoint):
    p1 = double_point.point1
    p2 = double_point.point2
    pad = 50
    print(p1)
    print(p2)
    f = frame[int(p1[1]):int(p2[1]), int(p1[0]):int(p1[0])]

    cv2.imwrite("test.png", f)
    return frame
