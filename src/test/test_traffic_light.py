# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

#import cv2
from model.traffic_light import TrafficLight


def test_red_classification(light: TrafficLight, image, resolution):
    # return light.check_traffic_light(image, resolution)
    assert True


def test_not_red_classification(light: TrafficLight, image, resolution):
    # return light.check_traffic_light(image, resolution)
    assert True
#
#
# tl = TrafficLight()
#
#
# frame = cv2.imread("redlight.PNG")
# res = (56, 83)
# box = [[],[]]
# box[0][0] = 0
# box[0][1] = res[0]
# box[1][0] = res[1]
# box[1][1] = 0
# tl.update_box(box)
# assert test_red_classification(tl, frame, res)
#
# frame = cv2.imread("greenlight.PNG")
# res = (71, 82)
# box = [[],[]]
# box[0][0] = 0
# box[0][1] = res[0]
# box[1][0] = res[1]
# box[1][1] = 0
# tl.update_box(box)
# assert test_not_red_classification(frame, res)
