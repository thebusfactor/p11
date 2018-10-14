# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from external.clip import clip_frame
from cv2 import cvtColor, inRange, countNonZero, COLOR_BGR2HSV
from numpy import array
from math import sqrt, pow


class TrafficLight:

    box: []
    z_threshold: int = 10

    def __init__(self):
        self.lower_bound = array([0, 10, 170])
        self.upper_bound = array([20, 160, 255])
        self.box = []

    def check_traffic_light(self, frame, res):
        """
            Uses points from the rectangle drawn on the screen by the user to clip the frame into a smaller region.
            This region has colour masks applied and the Z value is calculated to determine how much white is present in
            the selected frame after the colour masking.

            Parameters
            ----------
            frame : Frame
                Entire frame of the visible video feed window.
            res : []
                Resolution of the frame, (width, height).

            Returns
            -------
                True or False depending on if the masked traffic light result is greater than the threshold.
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
        """
            Update the box to be the new value.

            Parameters
            ----------
            box: []
                The box representing the traffic light region points.
        """
        self.box = box

    def distance_check(self, x1, x2, y1, y2):
        """
            Calculates vector distance between coordinates.

            Parameters
            ----------
            x1: int
                X value of first coordinate created on mouse action.
            x2: int
                X value of second coordinate created on mouse action.
            y1: int
                Y value of first coordinate created on mouse action.
            y2: int
                Y value of second coordinate created on mouse action.

            Returns
            -------
                True if the value of the distance is calculated to be greater than 5, False if not.
        """
        return sqrt(pow((x2-x1), 2) + pow((y2-y1), 2)) > 5

    def apply_light_mask(self, frame):
        """
            Converts a frame to a HSV (Hue-Saturation-Value) mask then converts to a binary mask of black and white
            pixels if there are any values within the lower and upper bounds.

            Parameters
            ----------
            frame : Frame
                Entire frame of the visible video feed window.

            Returns
            -------
                The mask object of the black and white binary mask.
        """
        hsv_image = cvtColor(frame, COLOR_BGR2HSV)
        mask = inRange(hsv_image, self.lower_bound, self.upper_bound)
        return countNonZero(mask)
