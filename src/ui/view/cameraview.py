import kivy

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *

from model import config
from util.double_point import DoublePoint

Builder.load_string('''
<CameraView>:
    id : mainwidget
    orientation: 'vertical'

    Camera:
        id: camera
        resolution: (1920,1080)
        play: True 
        pos: 0,0
''')

class CameraView(FloatLayout):

    """
        CameraView displays and controls the camera output screen on the user interface.
        Contains controls to use buttons and select line/light bounding boxes on screen.

    """

    def capture(self):
        """
            Method to capture the image currently displayed in the camera input pane.
        :return:
        """

        camera = self.ids['camera']
        self.screengrab(camera, numImage=1)

    ##TODO: this method doesn't currently work.
    def screengrab(self, cam, numImage):
        """
            Method to capture a number of images from the camera imput and store these images
            in a specified file.
        :param cam:
        :param numImage:
        :return:
        """

        # cam.play = False
        # outname = self.fileprefix+'_%(counter)04d.png'
        for i in range(numImage):
            outname = "image{}.png".format(i)
            Window.screenshot(name=outname)
            cam.play = True


    #################################################
    ##Intersection & Light Selection Methods Follow##
    #################################################


    TRANSPARENCY = 0.2

    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1

    line = False
    rectangle = False

    def reset_coordinates(self):
        '''
            Resets all 4 coordinates
        '''

        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1

    def set_line(self):
        '''
            Sets draw tool to line and resets all coordinates
        '''

        self.line = True
        self.rectangle = False
        self.reset_coordinates()


    def set_rectangle(self):
        '''
            Sets draw tool to rectangle and resets all coordinates
        '''

        self.rectangle = True
        self.line = False
        self.reset_coordinates()


    '''Set the Color to be used when drawing to the canvas, using the transparency constant'''
    def set_color(self, rgb: tuple):
        Color(rgb[0], rgb[1], rgb[2], self.TRANSPARENCY)

    def reset_tool(self):
        self.line = False
        self.rectangle = False

    def on_touch_down(self, touch):
        """
            When the user selects a point on the screen this method detects the selection points
            and draws the appropriate object depending on the button selected.
        :param touch:
        :return:
        """

        print("1:")
        print(self.canvas.children)
        print(touch)

        with self.canvas:

            if (self.x1 != -1 and self.y1 != -1 and self.x2 != -1 and self.y2 != -1):
                self.reset_coordinates()

            if (self.x1 == -1 and self.y1 == -1):
                self.x1 = touch.x
                self.y1 = touch.y
            else:
                self.x2 = touch.x
                self.y2 = touch.y

                if (self.line):
                    self.draw_line(touch)
                elif(self.rectangle):
                    # Add a rectangle
                    self.draw_rectangle()

                #reset the tool so the user can only draw one object at a time.
                self.reset_tool()

    def draw_line(self, touch):
        '''
            Draws line based on current coordinates
        '''
        Color(1., 0, 0)
        touch.ud["line"] = Line(points=[self.x1, self.y1, self.x2, self.y2], width=2)
        self.set_color((1, 0, 0))
        lineCoords = [(self.x1, self.y1), (self.x2, self.y2)]

        gradient = (self.y2 - self.y1) / (self.x2 - self.x1)
        constant = self.y1 / (gradient * self.x1)

        downBy = 400

        y3 = self.y1 - downBy
        x3 = self.x1 - (self.x2 - self.x1)

        y4 = self.y2 - downBy
        x4 = self.x2 - (self.x2 - self.x1)
        # (y4 - constant)/gradient

        print("x1={}, y1={}".format(self.x1, self.y1))
        print("x2={}, y2={}".format(self.x2, self.y2))

        self.set_color((0, 1, 0))
        # touch.ud["line"] = Line(points=[self.x1, y3, self.x2, y4], width=4)

        # ensure that shape is still within screen bounds
        if (y3 < 0):
            y3 = 0
        if (y4 < 0):
            y4 = 0
        if (x3 < 0):
            x3 = 0
        if (x4 < 0):
            x4 = 0
        ##touch.ud["line"] = Line(points=[x3, y3, x4, y4], width=2)
        config.set_line(DoublePoint((x3,y3),(x4,y4)))

    def draw_rectangle(self):
        '''
            Draws rectangle based on current coordinates
        '''

        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)

        self.set_color((1., 0, 0))

        pos = (0,0)

        if ((self.y1 - self.y2) < 0 and (self.x1 - self.x2) < 0):
            self.pos=(self.x1, self.y1)
        elif ((self.x1 - self.x2) < 0):
            self.pos=(self.x1, self.y2)
        elif ((self.y1 - self.y2) < 0):
            self.pos=(self.x2, self.y1)
        elif ((self.x1 - self.x2) > 0):
            self.pos=(self.x2, self.y2)

        Rectangle(pos = self.pos, size = (width,height))
        config.set_box(DoublePoint((pos[0],pos[1]),(pos[0]+width,pos[1]+height)))

    def get_line_coordinates(self):
        '''
            Returns the 4 placed line coordinates, and the other two 4 coordinates of the second line
        '''

        if (self.line):
            return self.x1, self.y1, self.x2, self.y2

    def delete_object(self):
        '''
            Deletes specified object (line or
        '''

        # TODO later
        print("Trying to delete")
        config.reset_config()

    def on_motion(self, etype, motionevent):
        #TODO: will receive all motion events.
        pass

    def on_touch_move(self, touch):
        print("HERE")

    def on_touch_up(self, touch):
        print("RELEASED!", touch)