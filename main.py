# File name: main.py (Digitas "main" .py file)


import kivy
kivy.require('1.8.0')

from engine import home
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

Builder.load_file(r'menu.kv')
Builder.load_file(r'date.kv')
Builder.load_file(r'screens/home_screen.kv')
Builder.load_file(r'screens/salat_screen.kv')
Builder.load_file(r'screens/gadget/gadget_screen.kv')
Builder.load_file(r'screens/gadget/calendar_screen.kv')
Builder.load_file(r'screens/gadget/dhikr_screen.kv')
Builder.load_file(r'screens/settings_screen.kv')
Builder.load_file(r'screens/about_screen.kv')
Builder.load_file(r'screens/reset_to_screen.kv')
Builder.load_file(r'screens/limit_screen.kv')
Builder.load_file(r'screens/save_screen.kv')
Builder.load_file(r'screens/open_screen.kv')
Builder.load_file(r'buttons.kv')

class DigitasMain(BoxLayout):
    def Counter(self, display_text):
        home.Counter(display_text)

    def Back(self, display_text):
        home.Back(display_text)

    def Reset(self, display_text):
        home.Reset(display_text)

    def Reset_to(self, reset_to_screen):
        home.Reset_to(reset_to_screen)

    def Limit(self, limit_display):
        home.Limit(limit_display)

    def Save_Fun1(self, save_display):
        home.Save_Fun1(save_display)

    def Save_Fun2(self, save_display):
        home.Save_Fun2(save_display)

###############- Time & Date -###############
class TimeDate():
    home.TimeDate()


class DigitasApp(App):
    pass

if __name__ == '__main__':
   DigitasApp().run()
