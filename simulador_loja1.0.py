from kivymd.app import MDApp as App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (400, 800) 

class Gerenciador(ScreenManager):
    pass

class Menu_Principal(Screen):
    def mudar_tela(self):
        self.parent.transition.direction = 'left'
        self.parent.current = "menu2"
    pass

class Simulador_loja(App):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        kv = Builder.load_file("./tela_inicial.kv")
        return kv
    pass

Simulador_loja().run()
