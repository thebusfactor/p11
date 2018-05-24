import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import *

class DrawInput(Widget):

    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1

    line = True
    rectangle = False

    objects = []
    undolist = []

    '''
    Resets all 4 coordinates
    '''
    def reset_coordinates(self):
        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1

    '''
    Sets draw tool to line and resets all coordinates
    '''
    def set_line(self):
        self.line = True
        self.rectangle = False
        self.reset_coordinates()

    '''
    Sets draw tool to rectangle and resets all coordinates
    '''
    def set_rectangle(self):
        self.rectangle = True
        self.line = False
        self.reset_coordinates()

    def on_touch_down(self, touch):

        print("1:")
        print(self.canvas.children)
        print(touch)

        with self.canvas:

            if(self.x1 != -1 and self.y1 != -1 and self.x2 != -1 and self.y2 != -1):
                self.reset_coordinates()

            if(self.x1 == -1 and self.y1 == -1):
                self.x1 = touch.x
                self.y1 = touch.y
            else:
                self.x2 = touch.x
                self.y2 = touch.y

                if(self.line):
                    self.draw_line(touch)
                else:
                    # Add a rectangle
                    self.draw_rectangle()


    '''
    Draws line based on current coordinates
    '''
    def draw_line(self, touch):
        Color(1., 0, 0)
        touch.ud["line"] = Line(points=[self.x1, self.y1, self.x2, self.y2], width=2)
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

        Color(0, 1, 0)
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
        touch.ud["line"] = Line(points=[x3, y3, x4, y4], width=2)

    '''
    Draws rectangle based on current coordinates
    '''
    def draw_rectangle(self):

        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)

        Color(1., 0, 0)

        if ((self.y1 - self.y2) < 0 and (self.x1 - self.x2) < 0):
            Rectangle(pos=(self.x1, self.y1), size=(width, height))
        elif ((self.x1 - self.x2) < 0):
            Rectangle(pos=(self.x1, self.y2), size=(width, height))
        elif ((self.y1 - self.y2) < 0):
            Rectangle(pos=(self.x2, self.y1), size=(width, height))
        elif ((self.x1 - self.x2) > 0):
            Rectangle(pos=(self.x2, self.y2), size=(width, height))

    def undo(self):
        # item = self.objects.pop(-1)
        # self.undolist.append(item)
        print("CHILDREN")
        print(self.canvas.children)

        obj = None
        n=2
        for child in self.canvas.children[::-1]:
            if isinstance(child, kivy.graphics.vertex_instructions.Line):
                if(n > 0):
                    self.canvas.remove(child)
                    n -= 1

        # self.canvas.remove(obj)

        # self.canvas.remove(self.canvas.children[-1])

        # self.canvas.remove(self.canvas.children[-2])

    '''
    Returns the 4 rectangle coordinates
    '''
    def get_rectangle_coordinates(self):
        if(self.rectangle):
            return self.x1, self.y1, self.x2, self.y2

    '''
    Returns the 4 placed line coordinates, and the other two 4 coordinates of the second line
    '''
    def get_line_coordinates(self):
        if(self.line):
            return self.x1, self.y1, self.x2, self.y2 #add 4 more


    '''
    Deletes specified object (line or 
    '''
    def delete_object(self):
        #TODO later
        return None


    def on_motion(self, etype, motionevent):
        # will receive all motion events.
        pass

    def on_touch_move(self, touch):
        print("HERE")

    def on_touch_up(self, touch):
        print("RELEASED!", touch)


KV = """

BoxLayout:
    DrawInput:
        id: widget
    Button:
        text: "undo"
        size_hint: (0.2, 0.1)
        on_release:
            widget.undo()
    Button:
        text: "redo"
        size_hint: (0.2, 0.1)
        on_release:
            widget.redo()
    Button:
        text: "line"
        size_hint: (0.2, 0.1)
        on_release:
            widget.set_line()
    Button:
        text: "rectangle"
        size_hint: (0.2, 0.1)
        on_release:
            widget.set_rectangle()

"""

class SimpleKivy4(App):
    def build(self):
        # return DrawInput()
        root = Builder.load_string(KV)
        return root


if __name__ == "__main__":
    SimpleKivy4().run()
