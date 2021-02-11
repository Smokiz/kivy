from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


class myApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical')
        bl.add_widget(Button(text="1",
     background_color=[1,1,0,1],size_hint=(.5, .25),pos_hint={'center_x': .5, 'center_y': .5}
     ))
        bl.add_widget(Button(text="2",
        background_color=[1,2,0,1],size_hint=(.5, .25),pos_hint={'center_x': .5, 'center_y': .5}
        ))
        return bl
     
if __name__=="__main__":
    myApp().run()
