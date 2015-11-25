from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

class Btn(Button):
    pass
btn = ObjectProperty()

class AdilsApp(App):
    pass

if __name__ == "__main__":
    AdilsApp().run()
