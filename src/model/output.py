import math
import cv2
import time
import pickle
import numpy
import os
from src.model.image import Image

hsv_colours = {'Yellow': (numpy.array([15, 100, 145]), numpy.array([160, 255, 255]))}

# make masks for colours that don't show up well in HSV
bgr_colours = {'Orange': (numpy.array([0, 100, 200]), numpy.array([50, 180, 255])),
               'Green': (numpy.array([100, 130, 100]), numpy.array([160, 255, 135])),
               'White': (numpy.array([180, 180, 180]), numpy.array([255, 255, 255])),
               'Blue': (numpy.array([110, 60, 35]), numpy.array([190, 180, 110])),
               'Pink': (numpy.array([150, 90, 110]), numpy.array([225, 190, 200]))}


def output_video():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # MJPG
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 1)

            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def output_snapshot_every_second():
    ccap = cv2.VideoCapture("output.avi")
    frame_rate = cap.get(5)

    x = 0
    while cap.isOpened():
        frame_number = cap.get(1)
        ret, frame = cap.read()
        if not ret:
            break
        print("frameId: {}  | frameRate = {}.".format(frame_number, frame_rate))
        if frame_number % math.floor(frame_rate) == 0:
            cv2.imwrite("./images/image%d.jpg" %(x/frame_rate), frame)
            output_image_object("./images/object%d.im" %(x/frame_rate), frame)

        x += 1
        print("X = {}".format(x))

    cap.release()
    print("Done!")


def output_specific_number_of_images(no_of_images, camerain, x, y, w, h):
    vidcap = cv2.VideoCapture(camerain)  # change to "filename.mp4/avi" for output stills from video

    kernel_open = numpy.ones((5, 5))
    kernel_close = numpy.ones((20, 20))

    lower_bound = numpy.array([0, 100, 140])
    upper_bound = numpy.array([40, 255, 255])
    for i in range(no_of_images):
        success, image = vidcap.read()
        if success:
            grayscale_image = Image.convert_image_to_grayscale(image)
            edge_mask_image = Image.convert_image_to_edge_mask(grayscale_image)
            imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(imgHSV, lower_bound, upper_bound)

            # res = cv2.bitwise_and(image, image, mask=mask)

            mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
            maskclose = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)

            maskfinal = maskclose
            _, conts, _ = cv2.findContours(maskfinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(image, conts, -1, (255, 0, 0), 3)

            for i in range(len(conts)):
                x, y, w, h = cv2.boundingRect(conts[i])
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow("mask", mask)
            z = cv2.countNonZero(maskclose)
            print(z)

            cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # cv2.imwrite('frame%d.jpg' %i, edge_detection_image)
            # cv2.imwrite('frame_gray_%d.jpg' % i, grayscale_image)

        print('Read a new frame: ' + str(success) + "\n")

    vidcap.release()
    cv2.destroyAllWindows()


def establish_baseline():
    avg = 0
    count = 0
    correct = 0
    colour_value = 20000
    dir = '/Users/Sean/Desktop/ENGR301/Bus-Factor/Bus-Factor/resources/bus/YellowWhite/'
    path = dir

    for filename in os.listdir(path):
        if filename.endswith('.png'):
            file = path + filename
            image = cv2.imread(file, flags=cv2.IMREAD_COLOR)
            mask, hsv = Image.apply_masks_colours(image, hsv_colours['Yellow'][0], hsv_colours['Yellow'][1])
            white = white_mask(image)
            z = cv2.countNonZero(mask)
            count += 1
            print(count)
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
            cv2.imshow("test", white)
            cv2.waitKey(0)
            cv2.imshow("test", image)
            cv2.waitKey(0)

    return avg, count, correct


def calc_z_value(mask):
    return cv2.countNonZero(mask)


def mask_addition(mask_one, mask_two):
    return Image.add_two_images(mask_one, mask_two)


def determine_bus(image):
    return 1


def check_traffic_light():
    path = '/Users/Sean/Desktop/ENGR301/Bus-Factor/Bus-Factor/resources/tlRed/'
    for filename in os.listdir(path):
        image = cv2.imread(path + filename, flags=cv2.IMREAD_COLOR)
        light, hsv = Image.apply_light_mask(image)
        print(calc_z_value(light))
        cv2.imshow("hsv", hsv)
        cv2.imshow("mask_hsv", light)
        cv2.imshow("orig", image)
        cv2.waitKey(0)
        # if z > 20 return True avg = 133~
        # Black returns 0 almost always, so anything really.


def green_mask(image):
    colour = 'Green'
    lb = bgr_colours[colour][0]
    ub = bgr_colours[colour][1]
    return Image.apply_masks_non_hsv(image, lb, ub)


def white_mask(image):
    colour = 'White'
    lb = bgr_colours[colour][0]
    ub = bgr_colours[colour][1]
    return Image.apply_masks_non_hsv(image, lb, ub)


def green_white_mask(image):
    mask = green_mask(image)
    white = white_mask(image)
    output = mask_addition(mask, white)
    z = cv2.countNonZero(output)
    return z


def yellow_white_mask(image):
    mask = yellow_mask(image)
    white = white_mask(image)
    output = mask_addition(mask, white)
    z = cv2.countNonZero(output)
    return z


def yellow_mask(image):
    colour = 'Yellow'
    lb = hsv_colours[colour][0]
    ub = hsv_colours[colour][1]
    return Image.apply_masks_colours(image, lb, ub)


def check_images():
    averages, count, correct = establish_baseline()
    print(count)
    print(correct)
    print("* Correct% -", correct / count)
    # for i in range(len(averages)):
    #     avg[i] = averages[i]/33
    #     print(avg[i])


# TODO Get two masks working
# TODO then check z value of each one to see if combined
# TODO Finish masks
# Theory is -> Light is scanned every second, when red trigger
# Frames to be taken every X times a second, running this and the NN model on it
check_traffic_light()
