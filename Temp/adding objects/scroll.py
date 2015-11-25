from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

sv = ScrollView()
grid = GridLayout(size_hint=(None, None), size = (root.right, 1200))
sv.add_widget(grid)


