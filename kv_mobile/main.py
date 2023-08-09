from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Container(BoxLayout):
	
	def change_label(self):
		pass

class StartApp(App):
	def build(self):
		
		return Container()
						
		
if __name__ == "__main__":
	StartApp().run()
	