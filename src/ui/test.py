from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *


class DrawInput(Widget):

    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    placed = False
    line = False

    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:

            # Add a red color
            Color(1., 0, 0)

            if(self.x1 != -1 and self.y1 != -1 and self.x2 != -1 and self.y2 != -1):
                self.x1 = -1
                self.y1 = -1
                self.x2 = -1
                self.y2 = -1

            if(self.x1 == -1 and self.y1 == -1):
                self.x1 = touch.x
                self.y1 = touch.y
            else:
                self.x2 = touch.x
                self.y2 = touch.y
                self.placed = True

                if(self.line):
                    touch.ud["line"] = Line(points=[self.x1, self.y1, self.x2, self.y2], width=2)
                else:
                    # Add a rectangle
                    Rectangle(pos=(self.x1, self.y1), size=(abs((abs(self.x1) - abs(self.x2))), abs((abs(self.y1) - abs(self.y2)))))





    def on_motion(self, etype, motionevent):
        # will receive all motion events.
        pass

    def on_touch_move(self, touch):
        print("HERE")
        # print(touch)
        # if(self.x1 != -1 and self.y1 != -1):
        #     if(not self.placed):
        #         self.x2 = touch.x
        #         self.y2 = touch.y
        #         touch.ud["line"] = Line(points=[self.x1, self.y1, self.x2, self.y2], width=10)
        # # touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        print("RELEASED!", touch)


class SimpleKivy4(App):
    def build(self):
        return DrawInput()


if __name__ == "__main__":
    SimpleKivy4().run()
