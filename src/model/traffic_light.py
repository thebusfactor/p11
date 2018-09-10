#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

import cv2

from external.clip import clip_frame
from model import config
from model.image import Image
from model.output import calc_z_value
from util.double_point import DoublePoint


class TrafficLight:

    box: DoublePoint

    def check_traffic_light(self, frame, res):
        print("BOX P1:", self.box.point1)
        print("BOX P2:", self.box.point2)

        point1 = (self.box.point1[0], res[1] - self.box.point1[1])
        point2 = (self.box.point2[0], res[1] - self.box.point2[1])

        print("AFTER P1:", point1)
        print("AFTER P2:", point2)

        new_dp = DoublePoint(point2, point1)

        clipped_frame = clip_frame(frame, new_dp, res)
        light, hsv = Image.apply_light_mask(clipped_frame)
        z = calc_z_value(light)
        #cv2.imshow("image", light)
        print("Z value:", z)
        if z > 20:
            return True
        else:
            return False

    def update_box(self, box: DoublePoint):
        self.box = box
