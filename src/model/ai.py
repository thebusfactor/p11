# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

from darkflow.net.build import TFNet
from threading import Thread

from controller.observer import Observer
from util.classification import Classification

class Ai:

    classifications_observers = []
    frame_count = 0
    count = 0

    def __init__(self, classification_rate=1, mode="gpu", weights=-1):
        if mode == "gpu":
            options = {"model": "../cfg/tiny-yolo-voc-1c.cfg",
                       "load": weights,
                       "threshold": 0.1,
                       "gpu": 0.9}
        else:
            options = {"model": "../cfg/tiny-yolo-voc-1c.cfg",
                       "load": weights,
                       "threshold": 0.1}
        self.tfnet = TFNet(options)
        self.frame = None
        self.debug_frame = None
        self.classification_rate = classification_rate

    def start_ai(self):
        """
            Begins the bus detection ai.
        """
        class_thread = Thread(target=self.classify_loop)
        class_thread.daemon = True
        class_thread.start()

    def update_ai_frame(self, frame, debug_frame):
        """
            Changes the current frame and increments the number of frames used.

            Parameters
            ----------
            frame :
                Current frame from the video feed being used.
        """
        self.frame_count += 1
        if frame is None or self.frame is not None:
            return
        self.count += 1
        self.frame = frame
        self.debug_frame = debug_frame

    def classify_loop(self):
        """
            Calls methods to classify the current frame when the frame count reaches a certain value.
        """
        while True:
            if self.frame_count >= self.classification_rate:
                self.classify(self.frame)
                self.frame_count = 0

    def classify(self, frame):
        """
            Classifies the passed in frame. Uses tfnet object to predict the object
            then creates a Classification object.

            Parameters
            ----------
            frame :
                Captured frame from the video feed.

            Returns
            -------
            out : []
                List used in classification
        """
        # frame = cv.resize(frame, (1920, 1080))
        if frame is None:
            return
        results = self.tfnet.return_predict(frame)
        out = []
        for res in results:
            clf = Classification(res)
            out.append(clf)
        self.frame = None
        self.update_classifications_observer(out)
        return out

    def add_classifications_observer(self, observer: Observer):
        """
            Sets the classifications observer to the passed in observer class.

            Parameters
            ----------
            observer : Observer
                The class which is to observe the classification.
        """
        self.classifications_observers.append(observer)

    def update_classifications_observer(self, classifications):
        """
           Updates the observing classes so that they have the correct information
           about the classified objects.

           Parameters
           ----------
           classifications : []
               Classified objects.
        """
        for classifications_observer in self.classifications_observers:
            classifications_observer.update(classifications)
