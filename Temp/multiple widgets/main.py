from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

btn = Button(text="Bismillah")

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

class MyApp(App):
    pass

if __name__ == "__main__":
    MyApp().run()
