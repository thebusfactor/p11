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
    line_obj = None
    intersects = False

    def __init__(self):
        self.frame = None
        self.play()

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
        cv.setMouseCallback(self.ui_name, self.click_and_crop)

        if (self.linePt != None and len(self.linePt) > 1):
            print(self.linePt[0])
            print(self.linePt[1])
            self.line_obj = cv.line(self.frame, self.linePt[0], self.linePt[1], (0, 255, 0), 5)

        cv.imshow(self.ui_name, self.frame)

    def update_classifications(self, classifications):
        self.classifications = classifications

    def draw_classifications_on_frame(self):
        if self.classifications is None or self.frame is None: return
        # check every detected object
        for i in range(0, len(self.classifications)):
            c = self.classifications[i]
            # confidence level of detected object has to be above threshold
            if c.conf > self.confidence_threshold:

                self.small_box(c.tl.get('x'), c.tl.get('y'), c.br.get('x'), c.br.get('y'))

                if c.label == "bus":
                    rect = cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.bus_colour, 2)
                    self.detect_event(c.tl.get('x'), c.tl.get('y'), c.br.get('x'), c.br.get('y'))
                    cv.putText(self.frame, c.label,(c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, self.bus_colour, 2)
                else:
                    rect = cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.not_bus_colour, 2)
                    self.detect_event(c.tl.get('x'), c.tl.get('y'), c.br.get('x'), c.br.get('y'))
                    cv.putText(self.frame, c.label, (c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, self.not_bus_colour, 2)


    def small_box(self, x1: int, y1: int, x2: int, y2: int):
        width = abs(x2-x1)
        height = abs(y2-y1)

        percentageToRemove = 0.3
        removedSectionWidth = width * percentageToRemove
        removedSectionHeight = height * percentageToRemove

        newX1 = int(removedSectionWidth + x1)
        newY1 = int(removedSectionHeight + y1)
        newX2 = int(x2 - removedSectionWidth)
        newY2 = int(y2 - removedSectionHeight)

        rectangle = cv.rectangle(self.frame, (newX1, newY1), (newX2, newY2), self.bus_colour, 2)

    def detect_event(self, x1: int, y1: int, x2: int, y2: int):

        if(self.linePt != None):

            if(len(self.linePt) >= 2):

                lineXPoints = []
                lineYPoints = []

                xWidth = abs(self.linePt[1][0] - self.linePt[0][0])
                yWidth = abs(self.linePt[1][1] - self.linePt[0][1])

                xIteration = xWidth/50
                yIteration = yWidth/50

                currentXPoint = self.linePt[0][0]
                currentYPoint = self.linePt[0][1]

                for i in range(50):
                    lineXPoints.append(currentXPoint + xIteration)
                    lineYPoints.append(currentYPoint + yIteration)

                for i in range(50):
                    if(self.contains(x1, y1, x2, y2, int(lineXPoints[i]), int(lineYPoints[i]))):
                        intersects = True
                        print(intersects)
                        cv.line(self.frame, (int(lineXPoints[i]), int(lineYPoints[i])), (int(lineXPoints[i])+10, int(lineYPoints[i])+10), (244, 40, 0), 4)

    def contains(self, x1: int, y1: int, x2: int, y2: int, px: int, py: int):
        return x1 < px < x2 and y1 < py < y2

    def play(self):

        while cv.getWindowProperty(self.ui_name, 0) >= 0:
            cv.imshow(self.ui_name, self.frame)
            # waits forever for the esc key to be pressed before exiting
            if cv.waitKey(50) == 27:
                break  # esc to quit
        cv.destroyAllWindows()