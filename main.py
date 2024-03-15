from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
import random

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    
    def generate_number(self):
        self.random_number.text = str(random.randint(0, 100))

class MainApp(MDApp):
    def build(self):
        #return MDLabel(text="test", halign="center")
        return MyRoot()

if __name__ == '__main__' :    
    MainApp().run()
