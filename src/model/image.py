import cv2

import numpy


class Image:
    def __init__(self):
        self

    @staticmethod
    def convert_image_to_grayscale(frame):
        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return imgGray

    @staticmethod
    def convert_image_to_edge_mask(frame):
        v = numpy.median(frame)
        sigma = 0.33
        # # TODO research function
        # blurred = cv2.GaussianBlur(frame, (3, 3), 0)
        #
        # lower = int(max(0, (1.0 - sigma) * v))
        # upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(blurred, lower, upper)
        return edged


    @staticmethod
    def detect_green_and_mask_image(frame):
        """
        Converts image to HSV mask, and returns the masked image as a binary black and white file - white where green
        is present and detected
        :param frame: the image to be masked
        :return: the masked image
        """
        lower_bound = numpy.array([33, 80, 40])
        upper_bound = numpy.array([102, 255, 255])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        return mask


    @staticmethod
    def detect_yellow_and_mask_image(frame):
        """
        Converts image to HSV mask, and returns the masked image as a binary black and white file - white where yellow
        is present and detected.
        :param frame: image to be masked
        :return: the masked image
        """
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 24    113   152
        lower_bound = numpy.array([0, 100, 140])
        upper_bound = numpy.array([40, 255, 255])

        # lower_bound = numpy.array([180, 280, 0])
        # upper_bound = numpy.array([255, 255, 100])

        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        kernel_open = numpy.ones((5, 5))
        kernel_close = numpy.ones((20, 20))

        mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
        mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)

        maskfinal = mask_close
        conts,h = cv2.findContours(maskfinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgHSV, conts, -1, (255, 0, 0), 3)

        for i in range(len(conts)):
            x, y, w, h = cv2.boundingRect(conts[i])
            cv2.rectangle(imgHSV, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return mask_close, mask


    @staticmethod
    def detect_red_and_mask_image(frame):
        """
        Converts image to HSV mask, and returns the masked image as a binary black and white file - white where red is
        present and detected.
        :param frame: Image passed in to be masked
        :return: the masked image
        """

        # lower_bound = numpy.array([80,70,58])
        # upper_bound = numpy.array([130,255,255])
        lower_bound = numpy.array([100,15,17])
        upper_bound = numpy.array([200,56,50])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # imgHSV = cv2.cvtColor(numpy.uint8([[[0,0,255]]]), cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        res = cv2.bitwise_and(frame, frame, mask= mask)
        return mask