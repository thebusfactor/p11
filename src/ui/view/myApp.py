import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.core.window import Window
import time


class CamApp(App):

    # Function to take a screenshot
    def screengrab(self, cam, numImage):
        #cam.play = False
        #outname = self.fileprefix+'_%(counter)04d.png'
        for i in range(numImage):
            outname = "image{}.png".format(i)
            Window.screenshot(name=outname)
            cam.play = True

    def start_timer(self, cam):
        millis = int(round(time.time()*1000))
        for i in range(5):
            print("in for loop\n")
            if millis % 10 == 0:
                print("in if millis % 0 loop\n")
                print("millis: %d", millis)
                self.screengrab(cam)

    def build(self):

        # create a floating layout as base
        camlayout = FloatLayout(size=(600, 600))
        #cam = Camera()        #Get the camera
        cam=Camera(resolution=(640,480), size=(640,480), index = 0)
        cam.play = True         #Start the camera
        camlayout.add_widget(cam)

        button=Button(text='Take Picture',size_hint=(0.12,0.12))
        # button.bind(on_press=self.screengrab(cam))
        camlayout.add_widget(button)    #Add button to Camera Layout
        self.fileprefix = 'snap'

        return camlayout


def on_touch_down(self, touch):
    # push the current coordinate, to be able to restore it later
    touch.push()

    # transform the touch coordinate to local space
    touch.apply_transform_2d(self.to_local)

    # dispatch the touch as usual to children
    # the coordinate in the touch is now in local space
    ret = super(..., self).on_touch_down(touch)

    # whatever the result, don't forget to pop your transformation
    # after the call, so the coordinate will be back in parent space
    touch.pop()
    print("YES")
    # return the result (depending what you want.)
    return ret


if __name__ == '__main__':
    CamApp().run()