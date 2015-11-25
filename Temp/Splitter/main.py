import kivy
kivy.require('1.8.1')
 
from kivy.app import App
from kivy.lang import Builder
 
root = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    Splitter:
        sizable_from: 'bottom'
        Button:
            text: 'something2'
    BoxLayout:
        Splitter:
            sizable_from: 'right'
            Button:
                text: 'something1'
        Splitter:
            sizable_from: "left"
            Label:
                text: 'empty area'
        Splitter:
            sizable_from: "bottom"
            Label:
                text: "yet another"
    Splitter:
        sizable_from: 'top'
        Button:
            text: 'something3'
''')
 
class TestApp(App):
    def build(self):
        return root
 
if __name__ == '__main__':
    TestApp().run()
