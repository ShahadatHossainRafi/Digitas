from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

sv = ScrollView()
child = GridLayout(cols=1, size_hint=(None, None))
child.bind(minimum_height=child.setter('height'))   
sv.add_widget(child)

dict = {"x": 1, "y": 2, "z": 3, "new": 4, "old": 5}

for key, value in dict.items():
    lbl = Label(text = key, size_hint=(None, None), size = (100, 300))
    child.add_widget(lbl)

class MyApp(App):
    def build(self):
        return sv

if __name__== "__main__":
    MyApp().run()
