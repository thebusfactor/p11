# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from external.clip import clip_frame
import cv2
import numpy
import math



class TrafficLight:

    box: []
    z_threshold: int = 10

    def __init__(self):
        self.lower_bound = numpy.array([0, 10, 170])
        self.upper_bound = numpy.array([20, 160, 255])

    def check_traffic_light(self, frame, res):
        """
        Uses points from the rectangle drawn on the screen by the user to clip the frame into a smaller region.
        This region has colour masks applied and the Z value is calculated to determine how much white is present in
        the selected frame after the colour masking.
        :param frame: entire frame of the visible video feed window
        :param res: resolution of the frame, (width, height)
        :return: True or False depending on if the masked traffic light result is greater than the threshold
        """
        x1 = self.box[0][0]
        y1 = res[1] - self.box[0][1]
        
        x2 = self.box[1][0]
        y2 = res[1] - self.box[1][1]

        if self.distance_check(x1, x2, y2, y1):
            point1 = (x1, y2)
            point2 = (x2, y1)
            if x2 > x1 and y1 < y2:
                point1 = (x1, y1)
                point2 = (x2, y2)
            elif x2 < x1 and y1 > y2:
                point1 = (x2, y2)
                point2 = (x1, y1)
            elif x2 < x1 and y1 < y2:
                point1 = (x2, y1)
                point2 = (x1, y2)
            new_dp = (point1, point2)
            clipped_frame = clip_frame(frame, new_dp, res)
            z = self.apply_light_mask(clipped_frame)
            return z > self.z_threshold
        return 0

    def update_box(self, box):
        self.box = box

    def distance_check(self, x1, x2, y1, y2):
        return math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2)) > 5

    def apply_light_mask(self, frame):
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image, self.lower_bound, self.upper_bound)
        return cv2.countNonZero(mask)
