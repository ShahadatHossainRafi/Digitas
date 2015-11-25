
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color
from kivy.lang import Builder

kv = """
BoxLayout:
    orientation: 'vertical'
    Button:
        btn: btn
        text: "something"
        mouse_pos: btn.text="Text Changed"
    Button:
        id: btn
        text: "another thing"
"""

class Test(App):
    layout = ObjectProperty(None)
    def build(self):
        return Builder.load_string(kv)

if(__name__ == '__main__'):
    Test().run()
