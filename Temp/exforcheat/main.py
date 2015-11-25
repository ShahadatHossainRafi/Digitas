import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.lang import Builder

Builder.load_file(r"openscreen.kv")
Builder.load_file(r"savescreen.kv")

class TestApp(App):
    def textfun(self, text):
        self.text = text

        

if __name__ == "__main__":
    TestApp().run()
