from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

gl = GridLayout(size_hint=(None, None), size=(500,800))
for index in range(10):
    index = str(index)
    btn = Button(text=index, size_hint=(None, None), size=(500, 80))
    gl.add_widget(btn)

sv = ScrollView()
sv.add_widget(gl)

class AdilsApp(App):
    def build(self):
        return sv

if __name__ == "__main__":
    AdilsApp().run()
