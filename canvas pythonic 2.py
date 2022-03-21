from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.graphics import Canvas,Color,Ellipse,Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
import random
class canvasclass(Widget):
    def __init__(self,**kwargs):
        super(canvasclass,self).__init__(**kwargs)
        for i in range(0,111):
            with self.canvas:
                Color(random.uniform(0,.999),random.uniform(0,.999),random.uniform(0,.999),1)
                self.el=Ellipse()
                self.el.size=(Window.width/100,Window.height/100)
                self.el.pos=(random.randint(0,Window.width),random.randint(0,Window.height))
class toolkit(App):
    def on_start(self,*args):
        print(self.b1.size[0])
    def newpos(self,*args):
        # self.b1.pos=(random.randint(0,Window.width-10),random.randint(0,Window.height-10))
        self.lay.add_widget(canvasclass())
    def autorun(self,*args):
        self.clc=Clock.schedule_interval(self.newpos,2)
        self.lay.add_widget(self.b2)
    def stopautorun(self,*args):
        self.clc.cancel()
    def build(self): 
        self.cir=canvasclass()
        self.lay=Widget()
        self.lay.add_widget(self.cir)
        self.b1=Button(text='Start',size=(50,40),pos=(0,0))
        self.b2=Button(text='Stop',size=(50,40),pos=(self.b1.size[0]+10,0))
        self.b1.bind(on_release=self.autorun)
        self.lay.add_widget(self.b1)
        self.b2.bind(on_release=self.stopautorun)
        return self.lay
if __name__ == "__main__":
    toolkit().run()
