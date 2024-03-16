from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class KivyTest(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #add widgets to window
        self.window.add_widget(Label(text="Hello, World!"))
        self.window.add_widget(Image(source="test.png"))
        
        self.input = TextInput(multiline=False)
        self.window.add_widget(self.input)

        return self.window

if __name__ == "__main__":
    KivyTest().run()
