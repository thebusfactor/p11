import cv2
import numpy


class Image:
    def __init__(self):
        self

    @staticmethod
    def convert_image_to_grayscale(frame):
        """
        Converts image to Grayscale mask, and returns the masked image as a binary black and white file
        :param frame: the image to be converted
        :return: the converted image
        """
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return img_gray


    @staticmethod
    def convert_image_to_edge_mask(frame):
        """
        Converts image to Edge mask, and returns the masked image as a Canny converted image
        :param frame: the image to be masked
        :return: the masked image
        """
        v = numpy.median(frame)
        sigma = 0.33
        blurred = cv2.GaussianBlur(frame, (3, 3), 0)
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(blurred, lower, upper)
        return edged


    @staticmethod
    def apply_masks(image, l_bound, u_bound):
        """
        Converts image to HSV mask, and returns the masked image as a binary black and white file - white where green
        is present and detected
        :param frame: the image to be masked
        :return: the masked image
        """
        kernel_open = numpy.ones((5, 5))
        kernel_close = numpy.ones((20, 20))
        lower_bound = l_bound
        upper_bound = u_bound
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
        mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
        mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)
        return mask_close