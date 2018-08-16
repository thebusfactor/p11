import cv2 as cv


class DebugGUI:

    ui_name = "Bus-Factor"
    classifications = None
    confidence_threshold = 0.01
    frame = None
    bus_colour = (0, 191, 255)
    not_bus_colour = (0, 0, 0)
    linePt = None
    line = False

    def __init__(self):
        self.frame = None
        #self.play()

    def click_and_crop(self, event, x, y, flags, params):
        if event == cv.EVENT_MOUSEMOVE and self.line:
            self.linePt.append((x, y))
        if event == cv.EVENT_LBUTTONDOWN:
            self.linePt = [(x, y)]
            self.line = True
            # check to see if the left mouse button was released
        elif event == cv.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates
            self.linePt[1] = (x, y)
            self.line = False


    def update_frame(self, frame):
        self.frame = frame
        self.draw_classifications_on_frame()
        cv.imshow(self.ui_name, self.frame)
        cv.setMouseCallback(self.ui_name, self.click_and_crop)

        if (self.linePt != None and len(self.linePt) > 1):
            print(self.linePt[0])
            print(self.linePt[1])
            cv.line(self.frame, self.linePt[0], self.linePt[1], (0, 255, 0), 5)

    def update_classifications(self, classifications):
        self.classifications = classifications

    def draw_classifications_on_frame(self):
        if self.classifications is None or self.frame is None: return
        # check every detected object
        for i in range(0, len(self.classifications)):
            c = self.classifications[i]
            # confidence level of detected object has to be above threshold
            if c.conf > self.confidence_threshold:
                if c.label == "bus":
                    cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.bus_colour, 2)
                    cv.putText(self.frame, c.label,(c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, self.bus_colour, 2)
                else:
                    cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.not_bus_colour, 2)
                    cv.putText(self.frame, c.label, (c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, self.not_bus_colour, 2)

    def play(self):
        while True:
            if self.frame is None:
                print("None")
                continue
            cv.imshow(self.ui_name, self.frame)
            # waits forever for the esc key to be pressed before exiting
            if cv.waitKey(50) == 27:
                break  # esc to quit
        cv.destroyAllWindows()