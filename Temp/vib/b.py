
from kivy.app import App
from kivy.lang import Builder
 
class Test(App):
    def build(self):
        return Builder.load_string("""
#:import vibrator plyer.vibrator

Button:
    text: 'Vibrate!'
    on_release:
        try: vibrator.vibrate(.2)
        except: pass
        """)
 
Test().run()
