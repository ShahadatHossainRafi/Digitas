#coding=utf-8

from kivy.app import App
from kivy.uix.label import Label

lbl = Label(text=u" ল + ড = ল্ড \n স + প = স্প \n দ + দ + ধ = দ্ধ", font_size = 40, font_name = "SolaimanLipi.ttf")

class KivyBengaliWritingProblemApp(App):
    def build(self):
        return lbl

if __name__ == "__main__":
    KivyBengaliWritingProblemApp().run()
