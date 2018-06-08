import cv2

from controller.observer import Observer
from model import config, traffic_light
from ui.view.config_view import setup_button


class Controller:

    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    capture_counter = 1

    line = False
    rectangle = False

    def __init__(self, model, config_view, res):
        self.model = model
        self.config_view = config_view
        self.drawable_widget = config_view.drawable_widget
        self.frame_texture = config_view.frame_texture

        self.click_observer = ClickObserver(self)
        self.drawable_widget.add_observer(self.click_observer)
        self.frame_observer = FrameObserver(self)

        self.model.add_observer(self.frame_observer)

        config_view.button_layout = setup_button(self, res)

    def reset_coordinates(self):
        """
            Resets all 4 coordinates
        """
        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1

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
        #self.drawable_widget.draw_alert()

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
        cv2.imwrite("frame_capture_%d.png" % self.capture_counter, self.model.frame)
        self.capture_counter += 1

    def reset_tool(self):
        self.line = False
        self.rectangle = False


class FrameObserver(Observer):

    def __init__(self, controller: Controller):
        self.controller = controller
        self.frame_texture = self.controller.frame_texture

    def update(self, frame):
        self.frame_texture.update_frame(frame)
        if self.controller.model.red:
            self.controller.drawable_widget.draw_red()
        else:
            self.controller.drawable_widget.draw_not_red()


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
                self.drawable_widget.draw_line(x1=self.controller.x1, y1=self.controller.y1, touch=touch)
            elif self.controller.rectangle:
                self.drawable_widget.draw_rectangle(x1=self.controller.x1, y1=self.controller.y1, touch=touch)
                self.controller.model.traffic_light.box = config.get_box()

            self.controller.reset_tool()
