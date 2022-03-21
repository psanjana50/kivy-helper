from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Canvas,Color,Ellipse,Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock
import random
class one(Widget):
    def __init__(self,**kwargs):
        super(one, self).__init__(**kwargs)
        with self.canvas:    
            Color(.234,.23,1,1)
            Ellipse(pos=(self.width,self.height/2))

class toolkit(App): 
    def build(self): 
        return one()
if __name__ == "__main__":
    toolkit().run()