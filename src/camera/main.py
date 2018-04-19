import math
import cv2
import time
import numpy
from Image import Image


def output_video():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # MJPG
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
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


def output_image_from_video():
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # videoFile = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    #yeet = cv2.IMREAD_ANYCOLOR(videoFile)


    cap = cv2.VideoCapture("output.avi")
    frameRate = cap.get(5)  # frame rate
    x = 1
    while (cap.isOpened()):
        frameId = cap.read  # current frame number

        # grey = cv2.cvtColor(frameId, cv2.COLOR_BGR2GRAY)
        ret, frame = cap.read
        if (not ret):
            break
        if (frameId % math.floor(frameRate) == 0):
            filename = './test_images/image' + str(int(x)) + ".jpg"
            x += 1
            cv2.imwrite(filename, frame)
        time.sleep(1)
    cap.release()
    print ("Done!")


def output_single_image():
    vidcap = cv2.VideoCapture(1) #change to "filename.mp4/avi"
    # success, image = vidcap.read()
    count = 0

    while count < 5:
        success, image = vidcap.read()
        # print("Read a new frame: " + str(success) + "\n")
        # if count%10 == 0:
        #     cv2.imwrite('frame%d.jpg'%count, image)
        #     print("success\n")

        cv2.imwrite('frame%d.jpg' % count, image)
        if success:
            print("VID CAP IS OPENED\n")

        success, image = vidcap.read()
        print('Read a new frame: '+ str(success))
        count += 1
        time.sleep(1)

    vidcap.release()
    cv2.destroyAllWindows()


def output_test():
    vidcap = cv2.VideoCapture(1)
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




# output_video()
# output_image_from_video()
# output_single_image()
output_test()