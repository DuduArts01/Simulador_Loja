from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (400, 800) 

class Gerenciador(ScreenManager):
    pass

class Menu_Principal(Screen):
    pass

class Simulador_loja(App):
    def build(self):
        return

Simulador_loja().run()
