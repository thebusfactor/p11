import cv2
import numpy


class Image:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def convert_image_to_grayscale(frame):
        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return imgGray

    @staticmethod
    def convert_image_to_edge_mask(frame):
        edge_image = cv2.Canny(frame, 80, 150)
        return edge_image

    '''
    Converts image to HSV mask, and returns the masked image as a binary black and
    white file - white where green is present and detected. 
    '''
    @staticmethod
    def detect_green_and_mask_image(frame):
        lower_bound = numpy.array([33,80,40])
        upper_bound = numpy.array([102,255,255])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        return mask

    '''
    Converts image to HSV mask, and returns the masked image as a binary black and
    white file - white where yellow is present and detected. 
    '''
    @staticmethod
    def detect_yellow_and_mask_image(frame):
        lower_bound = numpy.array([18,120,200])
        upper_bound = numpy.array([28,255,255])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        # cv2.imshow("mask", mask)
        # cv2.imshow("cam", frame)
        # cv2.waitKey(0)
        return mask

    '''
    Converts image to HSV mask, and returns the masked image as a binary black and
    white file - white where red is present and detected. 
    '''
    @staticmethod
    def detect_red_and_mask_image(frame):
        # lower_bound = numpy.array([80,70,58])
        # upper_bound = numpy.array([130,255,255])
        lower_bound = numpy.array([100,15,17])
        upper_bound = numpy.array([200,56,50])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # imgHSV = cv2.cvtColor(numpy.uint8([[[0,0,255]]]), cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        res = cv2.bitwise_and(frame, frame, mask= mask)
        return mask