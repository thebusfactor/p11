import cv2

from external.clip import clip_frame
from model import config
from model.image import Image
from model.output import calc_z_value
from util.double_point import DoublePoint


class TrafficLight:
    box: DoublePoint

    def check_traffic_light(self, frame, res):
        clipped_frame = clip_frame(frame, self.box, res)
        light, hsv = Image.apply_light_mask(clipped_frame)
        z = calc_z_value(light)
        if z > 20:
            return True
        else:
            return False
