from kivy.app import App

class Btn(Button):
    def fun(self):
        print 1

class CollideTestApp(App):
    pass

if __name__ == "__main__":
    CollideTestApp().run()
