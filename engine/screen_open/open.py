from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

DigitasScrollView = ScrollView()

class MyApp(App):
    return DigitasScrollView

if __name__ == "__main__":
    MyApp().run()
