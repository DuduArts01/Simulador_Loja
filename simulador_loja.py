from kivymd.app import MDApp as App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.clock import Clock


class Gerenciador(ScreenManager):
    pass

class Menu_Principal(Screen):
    def __init__(self, **kwargs):
        super(Menu_Principal, self).__init__(**kwargs)
        Clock.schedule_once(self.test)

    def test(self, dt):
        default_bg_color = "#cccccc"
        propriedades = {
                "ncards": 10
                }
        for i in range(propriedades["ncards"]):
            self.ids.cards.add_widget(  
                MD3Card(
                    line_color = (0.2, 0.2, 0.2, 0.8),
                    style = "elevated",
                    text = "aaaa",
                    md_bg_color = default_bg_color,
                )
            )

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
    
if __name__ == "__main__":
    Simulador_loja().run()
