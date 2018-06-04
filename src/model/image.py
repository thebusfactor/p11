import cv2
import numpy


class Image:
    def __init__(self):
        self

    @staticmethod
    def convert_image_to_grayscale(image):
        """
        Converts image to Grayscale mask, and returns the masked image as a binary black and white file
        :param image: the image to be converted
        :return: the converted image
        """
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return img_gray

    @staticmethod
    def convert_image_to_edge_mask(image):
        """
        Converts image to Edge mask, and returns the masked image as a Canny converted image
        :param image: the image to be masked
        :return: the masked image
        """
        v = numpy.median(frame)
        sigma = 0.66
        blurred = cv2.GaussianBlur(frame, (3, 3), 0)
        l_bound = int(max(0, (1.0 - sigma) * v))
        u_bound = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(blurred, l_bound, u_bound)
        return edged

    @staticmethod
    def apply_masks_colours(image, l_bound, u_bound):
        """
        Converts image to HSV mask, and returns the masked image as a binary black and white file - white where green
        is present and detected
        :param u_bound: upper limit of colour to detect
        :param l_bound: lower limit of colour to detect
        :param image: the image to be masked
        :return: the masked image
        """
        kernel_open = numpy.ones((5, 5))
        kernel_close = numpy.ones((20, 20))
        lower_bound = l_bound
        upper_bound = u_bound
        # maybe get two masks working
        # run white, then run yellow
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
        mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
        mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)
        return mask_close

    @staticmethod
    def apply_masks_non_hsv(image, l_bound, u_bound):
        """
        Converts image to white only mask
        :param image:
        :return: the masked image
        """
        mask = cv2.inRange(image, l_bound, u_bound)
        return mask

    @staticmethod
    def add_two_images(image_one, image_two):
        """
        Takes
        :param image_one: first image to be combined
        :param image_two: second image to be combined
        :return: comb_img: combined image
        """
        mask = cv2.inRange(image, l_bound, u_bound)
        return mask
