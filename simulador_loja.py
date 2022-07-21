from kivymd.app import MDApp as App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard

Window.size = (400, 800) 

class Gerenciador(ScreenManager):
    pass

class Menu_Principal(Screen):
    def mudar_tela(self):
        self.parent.transition.direction = 'left'
        self.parent.current = "tela2"
    pass

class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    '''Implements a material design v3 card.'''
    text = StringProperty()

class Simulador_loja(App):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        kv = Builder.load_file("./tela_inicial.kv")
        return kv
    pass
    
    def on_start(self):
        styles = {
                "Esponja":"#f6eeee", "image":"./images/cards/esponja.jpg" , "Cubo":"#f4dedc", "image":"./images/cards/cubo_magico.png"
        }
        for style in styles.keys():
            self.root.ids.gridlayout.box.add_widget(  
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.2, 0.8),
                    style=style,
                    text=style.capitalize(),
                    md_bg_color=styles[style],
                )
            )

if __name__ == "__main__":
    Simulador_loja().run()
