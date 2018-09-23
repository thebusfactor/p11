#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11
import argparse
import cv2
import numpy as np

class BusDetection:

    # initialize the list of class labels MobileNet SSD was trained to
    # detect, then generate a set of bounding box colors for each class

    def __init__(self):
        self.args = {'image': 'C:\\Users\\james\\Documents\\Bus-Factor\\resources\\vid.avi',
                'prototxt': 'C:\\Users\\james\\Documents\\Bus-Factor\\MobileNetSSD_deploy.prototxt.txt',
                'model': 'C:\\Users\\james\\Documents\\Bus-Factor\\MobileNetSSD_deploy.caffemodel', 'confidence': 0.2}
        self.net = cv2.dnn.readNetFromCaffe(self.args['prototxt'], self.args['model'])
        self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
                   "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                   "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                   "sofa", "train", "tvmonitor"]
        self.COLORS = np.random.uniform(0, 255, size=(len(self.CLASSES), 3))


    def detect(self, frame):
        """
            Detects the bus object within the frame.

            Parameters
            ----------
                frame : Frame
                    The current frame displayed from the video feed.
        """

        image = frame
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

        # pass the blob through the network and obtain the detections and
        # predictions
        print("[INFO] computing object detections...")
        self.net.setInput(blob)
        detections = self.net.forward()

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):

            # extract the confidence (i.e., probability) associated with the
            # prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > self.args["confidence"]:
                # extract the index of the class label from the `detections`,
                # then compute the (x, y)-coordinates of the bounding box for
                # the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # display the prediction
                label = "{}: {:.2f}%".format(self.CLASSES[idx], confidence * 100)
                print("[INFO] {}".format(label))
                cv2.rectangle(image, (startX, startY), (endX, endY),
                              self.COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(image, label, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.COLORS[idx], 2)

        # show the output image
        # cv2.imshow("detect", image)
        # cv2.waitKey(1)