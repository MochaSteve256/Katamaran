from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.webview import Webview

class GoogleMapsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        webview = Webview(url="https://www.google.com/maps")
        layout.add_widget(webview)
        return layout

if __name__ == '__main__':
    GoogleMapsApp().run()