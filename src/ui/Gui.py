from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import kivy

class Gui(App):

    def callback(instance):
        print('The button <%s> is being pressed' % instance.text)

    def build(self):
        button1 = Button(text='Intersection Line')
        #button1.bind(on_press=callback())



Gui().run()
