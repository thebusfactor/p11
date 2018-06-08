from controller import crop
from controller.observer import Observer
from model import config, model
from ui.view.config_view import setup_button


class Controller:

    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    line_coords = []

    calculated_crop = False

    line = False
    rectangle = False

    def __init__(self, model, config_view, res):
        self.model = model
        self.config_view = config_view
        self.drawable_widget = config_view.drawable_widget
        self.click_observer = ClickObserver(self)
        self.drawable_widget.add_observer(self.click_observer)
        config_view.button_layout = setup_button(self)
        self.res = res
        self.width = res[0]
        self.height = res[1]

    def reset_coordinates(self):
        """
            Resets all 4 coordinates
        """
        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1
        # self.x3 = -1
        # self.y3 = -1
        # self.x4 = -1
        # self.y4 = -1

    def set_line(self, button):
        """
            Sets draw tool to line and resets all coordinates
        """
        self.line = True
        self.rectangle = False
        self.config_view.drawable_widget.clear_line()
        self.reset_coordinates()

    def set_rectangle(self, button):
        """
            Sets draw tool to rectangle and resets all coordinates
        """
        self.rectangle = True
        self.line = False
        self.drawable_widget.clear_rectangle()
        self.reset_coordinates()

    def delete_object(self, button):
        """
            Deletes objects drawn on the camera pane.
        """
        config.reset_config()
        self.drawable_widget.clear_line()
        self.drawable_widget.clear_rectangle()

    def capture(self, button):
        """
            Method to capture the image currently displayed in the camera input pane.
        """
        pass

    def reset_tool(self):
        self.line = False
        self.rectangle = False


    def crop_with_line(self):

        if not self.calculated_crop:
            print(self.line_coords[0][0], self.height - self.line_coords[0][1], self.line_coords[0][2],
                      self.height - self.line_coords[0][3], self.line_coords[1][0], self.height - self.line_coords[1][1],
                      self.line_coords[1][2], self.height - self.line_coords[1][3])

            img_width = self.width
            img_height = self.height
            print(img_width)
            print(img_height)

            x1_ratio = self.line_coords[0][0] / img_width
            y1_ratio = (self.height - self.line_coords[0][1]) / img_height
            print(x1_ratio)
            print(y1_ratio)
            x2_ratio = self.line_coords[0][2] / img_width
            y2_ratio = (self.height - self.line_coords[0][3]) / img_height
            x3_ratio = self.line_coords[1][0] / img_width
            y3_ratio = (self.height - self.line_coords[1][1]) / img_height
            x4_ratio = self.line_coords[1][2] / img_width
            y4_ratio = (self.height - self.line_coords[1][3]) / img_height

        crop.crop_image(x1_ratio, y1_ratio, x2_ratio,
                        y2_ratio, x3_ratio,
                        y3_ratio, x4_ratio,
                        y4_ratio, self.model.frame)

class ClickObserver(Observer):

    def __init__(self, controller: Controller):
        self.controller = controller
        self.drawable_widget = self.controller.drawable_widget

    def update(self, touch):
        """
        When the user selects a point on the screen this method detects the selection points
        and draws the appropriate object depending on the button selected.
        :param touch:
        """

        if self.controller.x1 != -1 and self.controller.y1 != -1 \
                and self.controller.x2 != -1 and self.controller.y2 != -1:
            self.controller.reset_coordinates()

        if self.controller.x1 == -1 and self.controller.y1 == -1:
            self.controller.x1 = touch.x
            self.controller.y1 = touch.y
        else:
            self.controller.x2 = touch.x
            self.controller.y2 = touch.y

            if self.controller.line:
                self.controller.line_coords.append([self.controller.x1, self.controller.y1, self.controller.x2, self.controller.y2])
                self.drawable_widget.draw_line(x1=self.controller.x1, y1=self.controller.y1, touch=touch)
                print(self.controller.line_coords)
                if(len(self.controller.line_coords) >= 2):
                    self.controller.crop_with_line()

            elif self.controller.rectangle:
                self.drawable_widget.draw_rectangle(x1=self.controller.x1, y1=self.controller.y1, touch=touch)

            self.controller.reset_tool()

