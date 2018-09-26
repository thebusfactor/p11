from darkflow.net.build import TFNet
import threading

from controller.observer import Observer
from util.classification import Classification


class Ai:

    classifications_observers = []
    ai_update_frame = 4
    frame_count = 0

    def __init__(self):
        options = {"model": "../cfg/tiny-yolo-voc-1c.cfg",
                   "load": 1625,
                   "threshold": 0.1}
        self.tfnet = TFNet(options)
        self.frame = None

    def start_ai(self):
        """
            Begins the bus detection ai.
        """
        class_thread = threading.Thread(target=self.classify_loop)
        class_thread.daemon = True
        class_thread.start()

    def update_ai_frame(self, frame):
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
        self.frame = frame

    def classify_loop(self):
        """
            Calls methods to classify the current frame when the frame count reaches a certain value.
        """
        while True:
            if self.frame_count >= self.ai_update_frame:
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
