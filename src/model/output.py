import math
import cv2
import numpy
import os
from src.model.image import Image

hsv_colours = {'Yellow': (numpy.array([15, 100, 145]), numpy.array([160, 255, 255]))}

bgr_colours = {'Orange': (numpy.array([0, 100, 200]), numpy.array([50, 180, 255])),
               'Green': (numpy.array([100, 130, 100]), numpy.array([160, 255, 135])),
               'White': (numpy.array([180, 180, 180]), numpy.array([255, 255, 255])),
               'Blue': (numpy.array([110, 60, 35]), numpy.array([190, 180, 110])),
               'Pink': (numpy.array([150, 90, 110]), numpy.array([225, 190, 200]))}


def determine_bus(frame):
    """
    Main algorithm to detect bus, needs clipped part of frame
    Ordered in priority of colour bus is potentially
    1st. Yellow
    2nd. Yellow + White
    3rd. Green + White
    4th. Blue + white
    5th. Pink
    No data for: Orange, Green
    :param image: Clipped image from raw feed
    :return: Whether a bus has been detected
    """


    y_value = 19800
    yw_value = 19800
    gw_value = 15000
    bw_value = 15000
    p_value = 10000

    z = calc_z_value(yellow_mask(frame))
    if z > y_value:
        return True, z, "yellow"

    z = calc_z_value(yellow_white_mask(frame))
    if z > yw_value:
        return True, z, "yellow white"

    z = calc_z_value(green_white_mask(frame))
    if z > gw_value:
        return True, z, "green white"

    # z = calc_z_value(blue_white_mask(image))
    # if z > bw_value:
    #     return True, z, "blue white"
    #
    # z = calc_z_value(pink_mask(image))
    # if z > p_value:
    #     return True, z, "pink"

    return False, 0, "none"


def check_traffic_light(image):
    light = Image.apply_light_mask(image)
    z = calc_z_value(light)
    if z > 20:
        return True
    else:
        return False


def blue_white_mask(image):
    """
    :param image: Image to mask
    :return: Blue + White masked image
    """
    mask = blue_mask(image)
    white = white_mask(image)
    output = mask_addition(mask, white)
    return output


def pink_mask(image):
    """
    :param image: Image to mask
    :return: Pink masked image
    """
    colour = 'Pink'
    lb = bgr_colours[colour][0]
    ub = bgr_colours[colour][1]
    return Image.apply_masks_non_hsv(image, lb, ub)


def blue_mask(image):
    """
    :param image: Image to mask
    :return: Blue masked image
    """
    colour = 'Blue'
    lb = bgr_colours[colour][0]
    ub = bgr_colours[colour][1]
    return Image.apply_masks_non_hsv(image, lb, ub)


def green_mask(image):
    """
    :param image: Image to mask
    :return: Green masked image
    """
    colour = 'Green'
    lb = bgr_colours[colour][0]
    ub = bgr_colours[colour][1]
    return Image.apply_masks_non_hsv(image, lb, ub)


def white_mask(image):
    """
    :param image: Image to mask
    :return: White masked image
    """
    colour = 'White'
    lb = bgr_colours[colour][0]
    ub = bgr_colours[colour][1]
    return Image.apply_masks_non_hsv(image, lb, ub)


def green_white_mask(image):
    """
    :param image: Image to mask
    :return: Green + White masked image
    """
    mask = green_mask(image)
    white = white_mask(image)
    output = mask_addition(mask, white)
    return output


def yellow_white_mask(image):
    """
    :param image: Image to mask
    :return: Yellow + White masked image
    """
    mask = yellow_mask(image)
    white = white_mask(image)
    output = mask_addition(mask, white)
    return output


def calc_z_value(mask):
    """
    Calculate "amount" of white pixels in image
    :param mask: Mask to calculate white measure
    :return: value of white pixels
    """
    return cv2.countNonZero(mask)


def mask_addition(mask_one, mask_two):
    """
    Helper method to add two images
    :param mask_one: first image to be added
    :param mask_two: second image to be added
    :return: Combined image
    """
    return Image.add_two_images(mask_one, mask_two)


def yellow_mask(image):
    """
    :param image: Image to be mask
    :return: Yellow masked image
    """
    colour = 'Yellow'
    lb = hsv_colours[colour][0]
    ub = hsv_colours[colour][1]
    return Image.apply_masks_non_hsv(image, lb, ub)


def test_baseline(colour, path, z):
    avg = 0
    tot_z = 0
    count = 0
    correct = 0
    colour_value = z
    for filename in os.listdir(path):
        if filename.endswith('.png'):
            file = path + filename
            image = cv2.imread(file, flags=cv2.IMREAD_COLOR)
            if colour == 'y':
                mask = yellow_mask(image)
            elif colour == 'yw':
                mask = yellow_white_mask(image)
            elif colour == 'p':
                mask = pink_mask(image)
            elif colour == 'gw':
                mask = green_white_mask(image)
            elif colour == 'bw':
                mask = blue_white_mask(image)
            z = cv2.countNonZero(mask)
            tot_z += z
            count += 1
            if z > colour_value:
                print("* pass -", z)
                correct += 1
            else:
                print("* fail -", z)
            cv2.namedWindow("test", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("test", 900, 720)
            cv2.imshow("test", image)
            cv2.waitKey(0)
            cv2.imshow("test", mask)
            cv2.waitKey(0)
            cv2.imshow("test", image)
            cv2.waitKey(0)

    return avg, count, correct, tot_z


def check_images():
    colour = 'y'
    z = 10000
    path = '/Users/Sean/Desktop/ENGR301/Bus-Factor/Bus-Factor/resources/bus/yeet/'
    averages, count, correct, tot = test_baseline(colour, path, z)
    print("count: ", count)
    print("correct: ", correct)
    print("average: ", tot/count)
    print("* Correct% -", correct / count)

#check_images()