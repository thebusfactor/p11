import math
import cv2
import time
from Image import Image
import pickle


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
    cap = cv2.VideoCapture(1) #output.avi
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

def output_specific_number_of_images(no_of_images):
    vidcap = cv2.VideoCapture(1) #change to "filename.mp4/avi" for output stills from video

    for i in range(no_of_images):

        success, image = vidcap.read()
        if success:
            print("VIDEO CAPTURE IS OPENED")
            time.sleep(2)
            grayscale_image = Image.convert_image_to_grayscale(image)
            edge_mask_image = Image.convert_image_to_edge_mask(grayscale_image)
            yellow_mask = Image.detect_green_and_mask_image(image)

            cv2.imshow("edge mask", edge_mask_image)
            cv2.imshow("yellow mask", yellow_mask)
            cv2.imshow("raw image", image)
            cv2.imshow("grayscale mask", grayscale_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # cv2.imwrite('frame%d.jpg' %i, edge_detection_image)
            # cv2.imwrite('frame_gray_%d.jpg' % i, grayscale_image)

        print('Read a new frame: '+ str(success) + "\n")

    vidcap.release()
    # cv2.destroyAllWindows()

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




output_specific_number_of_images(1)