from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserIconView
import os
class toolkit(App):
    def fun1(self,instance):
        self.clearscreen()
    def folder_is(self,instance):
        self.clearscreen()
        #define add extentions details
        self.flay.add_widget(Label(text='Extentions: '+str(set([os.path.splitext(f)[1][1:] for f in os.listdir(self.file_chooser.selection[0]) if os.path.isfile(f)]))))
    def onlyd(self,instance,s):
        if os.path.isdir(s):
            return
    def fun2(self,instance):
        self.clearscreen()
        self.flay.rows=2
        self.flay.cols=1
        self.flay.padding=25
        self.flay.spacing=5
        self.file_chooser=FileChooserIconView(path='C:/Users/PS/Downloads/')
        self.file_chooser.dirselect=True
        self.file_chooser.filters=[self.onlyd]
        self.flay.add_widget(self.file_chooser)
        self.fb1=Button(text='Ok',size_hint_y=.1)
        self.flay.add_widget(self.fb1)
        #actions
        self.fb1.bind(on_release=self.folder_is)
    def del_empty(self,instance):
        ef, fwd=0, 0
        for a, b, c in os.walk(self.file_chooser.selection[0]):
            cp=a+'/'
            for f in b:
                try:
                    os.rmdir(cp+f)
                    ef+=1
                except:
                    fwd+=1
        self.lblc=Label(text=f'{ef} Empty Folders Deleted Successfully.\n{fwd} Folders have some data.')
        self.cokbtn=Button(text='Ok',size_hint_y=.4)
        self.clay=GridLayout(rows=2,cols=1,spacing=5)
        self.clay.add_widget(self.lblc)
        self.clay.add_widget(self.cokbtn)
        self.clearpop=Popup(title='Success',content=self.clay)
        self.clearpop.size_hint=(.35,.26)
        self.clearpop.open()
        #actions
        self.cokbtn.bind(on_release=self.clearpop.dismiss)
    def fun3(self,instance):
        # self.clearscreen()
        self.clearscreen()
        self.flay.rows=2
        self.flay.cols=1
        self.flay.padding=25
        self.flay.spacing=5
        self.file_chooser=FileChooserIconView(path='C:/Users/PS/Downloads/')
        self.file_chooser.dirselect=True
        self.file_chooser.filters=[self.onlyd]
        self.flay.add_widget(self.file_chooser)
        self.fb1=Button(text='Ok',size_hint_y=.1)
        self.flay.add_widget(self.fb1)
        #actions
        self.fb1.bind(on_release=self.del_empty)
    def clearscreen(self):
        self.flay.clear_widgets()
    def build(self):
        self.flay=GridLayout(rows=3,cols=1,padding=25,spacing=5)
        self.b1=Button(text='tool 1')
        self.b2=Button(text='Search All Extentions')
        self.b3=Button(text='Delete All Empty Folders')
        self.flay.add_widget(self.b1)
        self.flay.add_widget(self.b2)
        self.flay.add_widget(self.b3)
        #actions
        self.b1.bind(on_release=self.fun1)
        self.b2.bind(on_release=self.fun2)
        self.b3.bind(on_release=self.fun3)
        return self.flay
if __name__ == "__main__":
    toolkit().run()