from kivy.app import App
from kivy.properties import BooleanProperty

class TestApp(App):
    activevar = BooleanProperty(False)

if __name__ == "__main__":
    TestApp().run()
