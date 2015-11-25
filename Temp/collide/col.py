from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class CollideApp(App):
    def build(self):
    	root = FloatLayout()
    	self.btn = Button()
    	self.btn.pos_hint = {"center_x": .5, "center_y": .5}
    	self.btn.size_hint = [.5, .5]
    	root.add_widget(self.btn)
    	root.bind(on_touch_down=self.check_collision)

    	return root

    def check_collision(self, touch, *args):
    	print touch.pos
    	print self.btn.collide_point(*touch.pos)


if __name__ == "__main__":
	CollideApp().run()
