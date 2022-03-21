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
import random,time
class timeshow(Widget):
    def __init__(self,**kwargs):
        super(timeshow,self).__init__(**kwargs)
        self.lbl=Label()
        self.pos=(400,500)
        self.lbl.text=str(self.lbl.pos)

        self.wi=Widget(pos=(1000,400))
        
        self.wi.add_widget(self.lbl)
        self.add_widget(self.wi)

class draw(Widget):
    def __init__(self,**kwargs):
        super(draw,self).__init__(**kwargs)
        for i in range(0,100):
            with self.canvas.before:
                Color(random.uniform(0,.999),random.uniform(0,.999),random.uniform(0,.999),1)
                self.el=Ellipse()
                self.el.size=(Window.width/100,Window.height/100)
                self.el.pos=(random.randint(0,Window.width),random.randint(0,Window.height))            
class toolkit(App):
    
    def build(self): 
        self.w=Widget()
        self.b=Button(text='Stop')
        # self.b.bind(on_release=draw.stopdraw)
        # self.w.add_widget(self.b)
        self.w.add_widget(draw())
        self.w.add_widget(timeshow())
        return self.w
if __name__ == "__main__":
    toolkit().run()
