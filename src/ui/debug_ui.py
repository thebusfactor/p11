import cv2 as cv


class DebugGUI:

    ui_name = "Bus-Factor"
    frame = None

    def __init__(self, frame):
        self.frame = frame
        #self.play()

    def update_frame(self, frame):
        self.frame = frame
        cv.imshow(self.ui_name, self.frame)

    def play(self):
        while cv.getWindowProperty(self.ui_name, 0) >= 0:
            cv.imshow(self.ui_name, self.frame)
            # waits forever for the esc key to be pressed before exiting
            if cv.waitKey(50) == 27:
                break  # esc to quit
        cv.destroyAllWindows()

