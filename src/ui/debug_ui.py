import cv2 as cv


class DebugGUI:

    ui_name = "Bus-Factor"
    classifications = None
    confidence_threshold = 0.01
    frame = None
    once = True

    bus_colour = (0, 191, 255)
    not_bus_colour = (0, 0, 0)
    white = (255, 255, 255)

    # points of line
    line_pt = []
    # points for traffic light
    rect_pt = []
    # points for small box
    small_box_pt = []

    # toggle tool box
    toggle_x1 = 5
    toggle_x2 = 55
    toggle_y1 = 665
    toggle_y2 = 715
    toggle_bool = False

    # booleans for whether you should draw a new line/rect or not
    # false means draw, else true means its in process of being drawn).
    line = False
    rect = False

    # the objects
    line_obj = None
    rect_obj = None

    # the chosen tool, -1 for none, 0 for rectangle, 1 for line
    line_tool = True

    def __init__(self):
        self.frame = None

    def update_line(self):
        return self.line_pt

    def update_classifications(self, classifications):
        self.classifications = classifications

    def update_collision_rect(self):
        return self.small_box_pt

    def update_traffic_rect(self):
        return self.rect_pt

    def toggle_tools(self):
        pass

    def click_and_crop(self, event, x, y, flags, params):
        """
            Method is responsible for performing the correct actions depending on
            the mouse event passed in. First it checks the appropriate tool being used.
            Then, it will mark the first point of the shape and follow the mouse until
            it is released where it records the second point.


            Parameters
            ----------
            Event : Mouse Event
                the event when a user makes a mouse action.
            x : int
                the x point where the event occurred.
            y : int
                the y point where the event occurred.
        """
        if event == cv.EVENT_RBUTTONDOWN:
            self.line_tool = not self.line_tool
        elif event == cv.EVENT_LBUTTONDOWN:
            if self.check_mouse_coords(x, y):
                self.toggle_tool()

        if not self.check_mouse_coords(x, y):
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

    def check_mouse_coords(self, x, y):
        """
            Checks if the mouse points (x, y) are within the grey toggle box at the bottom left of the screen.
            This box has boundaries of toggle_x1, toggle_x2, toggle_y1, and toggle_y2.

            Parameters
            ----------
            x : int
                x value of mouse location.
            y : int
                y value of mouse location.

            Returns
            -------
            in_coords :
                True if mouse is within box, False if not
        """
        if self.toggle_x1 <= x <= self.toggle_x2 and self.toggle_y1 <= y <= self.toggle_y2:
            return True
        return False

    def toggle_tool(self):
        """
            Toggles the line tool.
        """
        self.line_tool = not self.line_tool

    def update_frame(self, frame):
        """
            Updates the frame by drawing the line and/or rectangle shape using the information
            stored from the user's clicks.

            Parameters
            ----------
            frame : Cam
                current camera frame
        """
        self.frame = frame
        self.draw_classifications_on_frame()
        cv.rectangle(self.frame, (self.toggle_x1, self.toggle_y1), (self.toggle_x2, self.toggle_y2),
                     (167, 170, 175), -2)

        if self.line_tool:
            cv.putText(self.frame, 'I', (25, 700), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_8, False)
        else:
            cv.putText(self.frame, 'TL', (15, 700), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_8, False)

        if len(self.line_pt) > 1:
            self.line_obj = cv.line(self.frame, self.line_pt[0], self.line_pt[1], (0, 255, 0), 5)
        if len(self.rect_pt) > 1:
            self.rect_obj = cv.rectangle(self.frame, self.rect_pt[0], self.rect_pt[1], (0, 0, 255), 5)

        cv.imshow(self.ui_name, self.frame)

        if self.once:
            cv.setMouseCallback(self.ui_name, self.click_and_crop)
            self.once = False

    def draw_classifications_on_frame(self):
        """
            Method to display a box around a classified object, using the points from the
            classifications made by the model.
            tl = top left of classification box.
            br = bottom right of classification box.
        """

        if self.classifications is None or self.frame is None:
            return

        classifications_to_draw = self.classifications

        # check every detected object
        for i in range(0, len(classifications_to_draw)):
            c = classifications_to_draw[i]
            # confidence level of detected object has to be above threshold
            if c.conf > self.confidence_threshold:

                self.small_box_pt = self.small_box(c.tl.get('x'), c.tl.get('y'), c.br.get('x'), c.br.get('y'))

    def small_box(self, x1: int, y1: int, x2: int, y2: int):
        """
            This returns the top left and bottom right coordinates that define a small bounding box
            that make up a certain percentage. x1, y1 are top left, x2, y2 are bottom right.

            Parameters
            ----------
            x1 : int
                x position of the top left point of the larger, classification box.
            y1 : int
                y position of the top left point of the larger, classification box.
            x2 : int
                x position of the bottom right point of the larger, classification box.
            y2 : int
                y position of the bottom right point of the larger, classification box.

            Returns
            -------
            smallBox : []
                2d array representing the small box
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

    def play(self):
        """
            Plays the video feed on the debug ui screen.
        """
        while True:
            if self.frame is None:
                continue
            cv.imshow(self.ui_name, self.frame)
            # waits forever for the esc key to be pressed before exiting
            if cv.waitKey(50) == 27:
                break  # esc to quit
        cv.destroyAllWindows()
