
#: -*- encoding: utf-8 -*-
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from plyer import vibrator
 
root = Builder.load_string('''

Button:
    text: 'Vibrate for 10 seconds!'
    on_release: app.vibrator_wrapper.vibrate(10)

''')
 
class VibratorWrapper(object):
 
    def vibrate(self, time):
        vibrator.vibrate(time)
 
    def stop(self):
        vibrator.cancel()
 
class VibratorExampleApp(App):
 
    vibrator_wrapper = ObjectProperty()
 
    def __init__(self, **kwargs):
        super(VibratorExampleApp, self).__init__(**kwargs)
        self.vibrator_wrapper = VibratorWrapper()
 
    def build(self):
        return root
    
if __name__ == '__main__':
    VibratorExampleApp().run()
