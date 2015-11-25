from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from var import var

layout = BoxLayout()
switch = Switch(text="setting")

if var == 0:
    switch.active = False
elif var == 1:
    switch.active = True

layout.add_widget(switch)

def fun(x, y):
    if y == True:
        f = opne("var.py", "w")

switch.bind(active=fun)

class MyApp(App):
    def build(self):
        return layout 

if __name__ == "__main__":
    MyApp().run()
