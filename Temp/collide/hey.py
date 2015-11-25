
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
 
class Test(App):
    def change_color(self, window, pos):
        root = self.root
        button = root.button
        layout = root.layout
 
        if(button.collide_point(*layout.to_local(*pos))):
            button.background_color = (1, 0, 0, 1)
        else:
            button.background_color = (1, 1, 1, 1)
 
    def build(self):
        Window.bind(mouse_pos=self.change_color)
 
        return Builder.load_string("""
BoxLayout:
    button: button
    layout: layout

    orientation: 'vertical'

    RelativeLayout:
        id: layout

        Button:
            id: button

            text: ti.text

            size_hint: .15, .15
            pos_hint: {'center': (.5, .5)}

    TextInput:
        id: ti

        text: 'Some text'

        size_hint_y: None
        height: self.font_size * 2
        """)
 
if(__name__ == '__main__'):
    Test().run()
