import cv2
import time
import numpy


class Image:
    def __init__(self):
        self

        # self.output = output
        # self.frame = frame

    @staticmethod
    def detect_green_and_mask_image(frame):
        # frame = cv2.imread(output)
        # cv2.imwrite(output, frame)
        # greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite(output, greyscale)
        # img = cv2.imread(frame, cv2.IMREAD_GRAYSCALE)
        #for i in range(len(frame))
        lower_bound = numpy.array([33,80,40])
        upper_bound = numpy.array([102,255,255])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        cv2.imshow("mask", mask)
        cv2.imshow("cam", frame)
        cv2.waitKey(0)

    @staticmethod
    def detect_yellow_and_mask_image(frame):
        lower_bound = numpy.array([18,120,200])
        upper_bound = numpy.array([28,255,255])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        cv2.imshow("mask", mask)
        cv2.imshow("cam", frame)
        cv2.waitKey(0)

    @staticmethod
    def detect_red_and_mask_image(frame):
        # lower_bound = numpy.array([80,70,58])
        # upper_bound = numpy.array([130,255,255])
        lower_bound = numpy.array([100,15,17])
        upper_bound = numpy.array([200,56,50])
        imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # imgHSV = cv2.cvtColor(numpy.uint8([[[0,0,255]]]), cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        # res = cv2.bitwise_and(frame, frame, mask= mask)
        # cv2.imshow("res", res)
        cv2.imshow("mask", mask)
        cv2.imshow("cam", frame)
        cv2.waitKey(0)

    @staticmethod
    def show_image_on_screen(frame):
        greyscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        i = cv2.imshow("new window", greyscale_frame)
        print(frame)
        cv2.waitKey(500)
        # time.sleep(3)
        cv2.destroyAllWindows()