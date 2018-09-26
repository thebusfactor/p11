# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from external.clip import clip_frame
from model.image import Image
import cv2


class TrafficLight:

    box: []
    z_threshold: int = 20

    def check_traffic_light(self, frame, res):
        """
        Uses points from the rectangle drawn on the screen by the user to clip the frame into a smaller region.
        This region has colour masks applied and the Z value is calculated to determine how much white is present in
        the selected frame after the colour masking.
        :param frame: entire frame of the visible video feed window
        :param res: resolution of the frame, (width, height)
        :return: True or False depending on if the masked traffic light result is greater than the threshold
        """

        print(self.box)
        # get x and y points from the rectangle drawn by the user
        point1 = (self.box[0][0], res[1] - self.box[1][1])
        point2 = (self.box[1][0], res[1] - self.box[0][1])

        new_dp = (point1, point2)

        clipped_frame = clip_frame(frame, new_dp, res)
        light, hsv = Image.apply_light_mask(clipped_frame)
        z = self.calc_z_value(self, light)

        return z > self.z_threshold

    def update_box(self, box):
        self.box = box

    @staticmethod
    def calc_z_value(self, mask):
        return cv2.countNonZero(mask)
