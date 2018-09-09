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
                   "load": 875,
                   "threshold": 0.1}
        self.tfnet = TFNet(options)
        self.frame = None

    def start_ai(self):
        class_thread = threading.Thread(target=self.classify_loop)
        class_thread.daemon = True
        class_thread.start()

    def update_ai_frame(self, frame):
        self.frame_count += 1
        if frame is None or self.frame is not None:
            return
        self.frame = frame

    def classify_loop(self):
        while True:
            if self.frame_count >= self.ai_update_frame:
                self.classify(self.frame)
                self.frame_count = 0


    def classify(self, frame):
        # frame = cv.resize(frame, (1920, 1080))
        if frame is None:
            return
        results = self.tfnet.return_predict(frame)
        out = []
        for res in results:
            clf = Classification(res)
            out.append(clf)
            # print(clf)
        self.frame = None
        self.update_classifications_observer(out)
        return out

    def add_classifications_observer(self, observer: Observer):
        self.classifications_observers.append(observer)

    def update_classifications_observer(self, classifications):
        for classifications_observer in self.classifications_observers:
            classifications_observer.update(classifications)