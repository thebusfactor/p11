import cv2 as cv


class DebugGUI:

    ui_name = "Bus-Factor"
    classifications = None
    confidence_threshold = 0.01
    frame = None

    bus_colour = (0, 191, 255)
    not_bus_colour = (0, 0, 0)
    white = (255, 255, 255)

    # points of line
    line_pt = []
    # points for traffic light
    rect_pt = []

    # booleans for whether you should draw a new line/rect or not
    # false means draw, else true means its in process of being drawn).
    line = False
    rect = False

    # the objects
    line_obj = None
    rect_obj = None
    intersects = False

    # the chosen tool, -1 for none, 0 for rectangle, 1 for line
    line_tool = True

    def __init__(self):
        self.frame = None

    def update_line(self):
        return self.line_pt

    def update_classifications(self, classifications):
        self.classifications = classifications

    def update_rect(self):
        return self.rect_pt

    def update_collision_boolean(self):
        return self.intersects

    def toggle_tools(self):
        pass

    def click_and_crop(self, event, x, y, flags, params):
        """
        Method is responsible for performing the correct actions depending on
        the mouse event passed in. First it checks the appropriate tool being used.
        Then, it will mark the first point of the shape and follow the mouse until
        it is released where it records the second point.
        """
        if event == cv.EVENT_RBUTTONDOWN:
            self.line_tool = not self.line_tool

        if self.line_tool:
            if event == cv.EVENT_LBUTTONDOWN:
                self.line_pt = [(x, y)]
                self.line = True
                # check to see if the left mouse button was released
            elif event == cv.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates
                self.line_pt.append((x, y))
                self.line = False
        elif not self.line_tool:
            if event == cv.EVENT_LBUTTONDOWN:
                self.rect_pt = [(x, y)]
                self.rect = True
                # check to see if the left mouse button was released
            elif event == cv.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates
                self.rect_pt.append((x, y))
                self.rect = False

    def update_frame(self, frame):
        """
            Updates the frame by drawing the line and/or rectangle shape using the information
            stored from the user's clicks.
        """
        self.frame = frame
        self.draw_classifications_on_frame()
        cv.setMouseCallback(self.ui_name, self.click_and_crop)

        if len(self.line_pt) > 1:
            self.line_obj = cv.line(self.frame, self.line_pt[0], self.line_pt[1], (0, 255, 0), 5)
        if len(self.rect_pt) > 1:
            self.rect_obj = cv.rectangle(self.frame, self.rect_pt[0], self.rect_pt[1], (0, 0, 255), 5)

        cv.imshow(self.ui_name, self.frame)

    def draw_classifications_on_frame(self):
        """
            Method to display a box around a classified object, using the points from the
            classifications made by the model.
            tl = top left of classification box.
            br = bottom right of classification box.
        """

        if self.classifications is None or self.frame is None: return
        # check every detected object
        for i in range(0, len(self.classifications)):
            c = self.classifications[i]
            # confidence level of detected object has to be above threshold
            if c.conf > self.confidence_threshold:

                small_box = self.small_box(c.tl.get('x'), c.tl.get('y'), c.br.get('x'), c.br.get('y'))

                if c.label == "bus":
                    rect = cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.bus_colour, 1)
                    if self.detect_event(small_box[0][0], small_box[0][1], small_box[1][0], small_box[1][1]):
                        # event has been detected, increment counter
                        self.intersects = True
                    else:
                        # Reset intersection boolean
                        self.intersects = False
                    cv.putText(self.frame, c.label + " " + str(c.conf*100)[0:2] + "%",(c.tl.get('x')+10, c.tl.get('y') + 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, 2)
                else:
                    rect = cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.not_bus_colour, 1)
                    self.detect_event(small_box[0][0], small_box[0][1], small_box[1][0], small_box[1][1])
                    cv.putText(self.frame, c.label + " " + str(c.conf * 100)[0:2] + "%", (c.tl.get('x') + 10, c.tl.get('y') + 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, 2)

    def small_box(self, x1: int, y1: int, x2: int, y2: int):
        """
            This returns the top left and bottom right coordinates that define a small bounding box
            that make up a certain percentage. x1, y1 are top left, x2, y2 are bottom right.
        """
        width = abs(x2-x1)
        height = abs(y2-y1)

        percentage_to_remove = 0.3
        removed_section_width = width * percentage_to_remove
        removed_section_height = height * percentage_to_remove

        new_x1 = int(removed_section_width + x1)
        new_y1 = int(removed_section_height + y1)
        new_x2 = int(x2 - removed_section_width)
        new_y2 = int(y2 - removed_section_height)

        cv.rectangle(self.frame, (new_x1, new_y1), (new_x2, new_y2), self.bus_colour, 1)
        return [(new_x1, new_y1), (new_x2, new_y2)]

    def detect_event(self, x1: int, y1: int, x2: int, y2: int):
        """
        Method to check if a classified object is intersecting the intersection
        line specified by the user. point (x1, y2) are top left and (x2, y2) is bottom right of rectangle.
        """

        if self.line_pt is not None:
            if len(self.line_pt) >= 2:

                line_x_points = []
                line_y_points = []

                x_width = (self.line_pt[1][0] - self.line_pt[0][0])
                y_width = (self.line_pt[1][1] - self.line_pt[0][1])

                x_iteration = (x_width/50)
                y_iteration = (y_width/50)

                # Required to account for different directions that the line can be drawn.
                current_x_point = self.line_pt[1][0]
                current_y_point = self.line_pt[1][1]
                y_iteration *= -1
                x_iteration *= -1

                # Iterates through the line and selects 50 intervals/points.
                for i in range(50):
                    line_x_points.append(current_x_point)
                    line_y_points.append(current_y_point)
                    current_x_point += x_iteration
                    current_y_point += y_iteration

                # Iterates through the 50 points and checks if the point is within the box, if it is then
                # we can determine that the object intersects the line.
                for i in range(50):
                    if self.contains(self, x1, y1, x2, y2, int(line_x_points[i]), int(line_y_points[i])):
                        self.intersects = True
                        cv.circle(self.frame, (int(line_x_points[i]), int(line_y_points[i])), 5, (244, 40, 0))

    @staticmethod
    def contains(self, x1: int, y1: int, x2: int, y2: int, px: int, py: int):
        """
            Check if point (px, py) is contained within rectangle [(x1, y1), (x2, y2)],
            where points are top left and bottom right respectively.
        """
        return x1 < px < x2 and y1 < py < y2

    def play(self):
        while True:
            if self.frame is None:
                # print("None")
                continue
            cv.imshow(self.ui_name, self.frame)
            # waits forever for the esc key to be pressed before exiting
            if cv.waitKey(50) == 27:
                break  # esc to quit
        cv.destroyAllWindows()
