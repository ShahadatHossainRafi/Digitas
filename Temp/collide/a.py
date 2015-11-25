from kivy.app import App
from kivy.uix.button import Button

Btn = Button()
Btn.size_hint = .5, .5
Btn.pos_hint = {"center_x": .5, "center_y": .5}

class Collide(object):
    def __init__(self):
        name = Btn.collide_point(x, y)

class ColApp(App):
    def build(self):
        return Btn

if __name__ == "__main__":
    ColApp().run()
