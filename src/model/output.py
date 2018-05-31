import math
import cv2
import time
import pickle
import numpy
from src.model.image import Image

colours = {'Yellow': (numpy.array([10, 100, 150]), numpy.array([50, 255, 255])),
           'Orange': (numpy.array([0, 100, 200]), numpy.array([50, 180, 255])),
           'Green': (numpy.array([0, 100, 0]), numpy.array([30, 255, 150])),
           'White': (numpy.array([0, 0, 70]), numpy.array([20, 10, 255])),
           'Blue': (numpy.array([50, 20, 0]), numpy.array([150, 100, 50])),
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
    cap = cv2.VideoCapture(0) #output.avi
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
            # image_object = Image()
            # output_image_object("./images/object%d.im" %(x/frame_rate), image_object)

        x += 1
        print("X = {}".format(x))

    cap.release()
    print ("Done!")


def output_image_object(filename, obj):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL) #highest_protocol = -1


def output_specific_number_of_images(no_of_images, camerain, x, y, w, h):
    #vidcap = cv2.VideoCapture(camerain) #change to "filename.mp4/avi" for output stills from video

    #for i in range(no_of_images):
    #while True:

    #success, image = vidcap.read()
    file_path = '/Users/Sean/Desktop/ENGR301/Bus-Factor/Bus-Factor/resources'
    image = cv2.imread(file_path+'/bus/bus5.png', flags=cv2.IMREAD_COLOR)
    kernel_open = numpy.ones((5, 5))
    kernel_close = numpy.ones((20, 20))

    lower_bound = numpy.array([0, 100, 140])
    upper_bound = numpy.array([40, 255, 255])

    if True:
        #cv2.namedWindow("test", cv2.WINDOW_NORMAL)
        #cv2.resizeWindow("test", 1920, 1080)
        #cv2.imshow("test", crop)
        # (x, y, w, h) = cv2.selectROI("testROI", damn)
        # pass in coords
        #image = crop[y:y + h, x:x + w]  # both opencv and numpy are "row-major", so y goes first
        #print("VIDEO CAPTURE IS OPENED")
        #time.sleep(2)
        #grayscale_image = Image.convert_image_to_grayscale(image)
        #edge_mask_image = Image.convert_image_to_edge_mask(grayscale_image)
        #res, yellow_mask = Image.detect_yellow_and_mask_image(image)

        #image = cv2.resize(image, (1280, 720))
        imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, lower_bound, upper_bound)

        #res = cv2.bitwise_and(image, image, mask=mask)



        mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
        maskclose = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)

        maskfinal = maskclose
        _, conts, _ = cv2.findContours(maskfinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(image, conts, -1, (255, 0, 0), 3)

        for i in range(len(conts)):
            x, y, w, h = cv2.boundingRect(conts[i])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # cv2.imshow("grayscale mask", grayscale_image)
        # cv2.imshow("edge mask", edge_mask_image)
        #cv2.imshow("mask", mask)
        # cv2.imshow("yellow mask", yellow_mask)
        #cv2.imshow("maskclose", maskclose)
        #cv2.imshow("maskopen", mask_open)


        cv2.imshow("mask", mask)
        z = cv2.countNonZero(maskclose)
        print(z)


        cv2.waitKey(0)
        #cv2.destroyAllWindows()
        # cv2.imwrite('frame%d.jpg' %i, edge_detection_image)
        # cv2.imwrite('frame_gray_%d.jpg' % i, grayscale_image)



    #print('Read a new frame: '+ str(success) + "\n")

#vidcap.release()
#cv2.destroyAllWindows()


def output_test():
    vidcap = cv2.VideoCapture(0)
    count = 0
    succ = True
    while succ:
        # cv2.imwrite("frame%d.jpg" % count, image)

        succ, image = vidcap.read()
        i = Image()
        i.detect_red_and_mask_image(image)
        # i.show_image_on_screen(image)

        print("image %d output" % count, succ)
        count += 1
        time.sleep(1)


def check_image():
    #run tests on image and return if true
    #TODO
    #establish baselines, sort out generic colour masks
    #make sure there is 90% detection between bus and none bus

    #Once detected make sure doesn't detect again

    #Edge detection?
    averages = establish_baseline(31)
    avg = [0] * 6
    for i in range(len(averages)):
        avg[i] = averages[i]/33
        print(avg[i])


def establish_baseline(no_of_images):
    length = len(colours)
    avg = [0] * length
    file_path = '/Users/james/OneDrive/Documents/GitHub/Bus-Factor/resources'
    for i in range(no_of_images):
        j = 0

        image = cv2.imread(file_path + '/emptyInt/emptyInt%d.png' % i,
                           flags=cv2.IMREAD_COLOR)
        print(file_path + '/emptyInt/emptyInt%d.png' % i)
        x = 200
        y = 200
        w = 400
        h = 400
        #image = crop[y:y + h, x:x + w]
        cv2.imshow("image", image)
        cv2.waitKey(0)
        # for key in colours:
        #     l_b = colours[key][0]
        #     u_b = colours[key][1]
        #     mask = apply_masks(image, l_b, u_b)
        #     z = cv2.countNonZero(mask)
        #     avg[j] = avg[j] + z
        #     j += 1
        mask = apply_masks(image, colours["Yellow"][0], colours["Yellow"][1])
        cv2.imshow("mask", mask)
        cv2.waitKey(0)
    return avg


def get_average_colour(path, colour):
    file_path = 'C:/Users/james/OneDrive/Documents/GitHub/Bus-Factor/resources'
    image = cv2.imread(file_path+path,flags=cv2.IMREAD_COLOR)
    ## get name
    #image = crop[y:y + h, x:x + w]
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("test", 800, 640)
    cv2.imshow("test", image)
    cv2.waitKey(0)
    l_b = colours[colour][0]
    u_b = colours[colour][1]
    print(l_b)
    print(u_b)
    mask = apply_masks(image, l_b, u_b)
    cv2.imshow("test", mask)
    cv2.waitKey(0)
    cv2.imshow("test", image)
    cv2.waitKey(0)
    cv2.imshow("test", mask)
    cv2.waitKey(0)
    z = cv2.countNonZero(mask)
    print(z)
    return z





#check_image()
#'/bus/Pink/bus23Pink.png', 'Pink'
#'/bus/Yellow/bus2.png', 'Yellow'
#'/bus/White/bus32.png', 'White'
#'/emptyInt/emptyInt4.png', 'Yellow'
establish_baseline(32)
# get_average_colour('/bus/White/bus32.png', 'Yellow')

# 3401.6666666666665
# 1139.2727272727273
# 1619.6363636363637
# 0.0
# 5663.272727272727
# 27.90909090909091