from kivy.app import App
from plyer import vibrator

class TempApp(App):
    def fun(self):
        vibrator.vibrate(.50)

if __name__ == "__main__":
    TempApp().run()
