from kivy import utils
from kivy.app import App
from kivy.uix.widget import Widget



class SlowaMain(Widget):
    pass


class SlowaApp(App):
    def build(self):
        return SlowaMain()

if __name__ == "__main__":
    SlowaApp().run()