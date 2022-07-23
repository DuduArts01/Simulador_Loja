from kivymd.app import MDApp as App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from custom_widgets.widgets import MD3Card
from shopping_cart.shopping_cart import ShoppingItems


class Gerenciador(ScreenManager):
    pass

class Menu_Principal(Screen):
    def __init__(self, **kwargs):
        super(Menu_Principal, self).__init__(**kwargs)
        Clock.schedule_once(self.gen_cards)

    def open_login(self):  #test acess login
        self.parent.current = "login_screen"

    def gen_cards(self, dt):
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

    def mudar_tela(self, tela):
        self.parent.transition.direction = 'left'
        self.parent.current = tela

    def open_cart(self):
        self.parent.current = "Shopping Cart"
        screen = App.get_running_app().root.get_screen("Shopping Cart")
        for i in range(20):
            screen.ids.cart_layout.add_widget(  
                ShoppingItems(
                    line_color = (0.2, 0.2, 0.2, 0.8),
                    style = "elevated",
                    text = "aaaa",
                    md_bg_color = "#cccccc",
                )
            )

    pass

class Simulador_loja(App):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        kv = Builder.load_file("./tela_inicial.kv")
        return kv
    pass
    
if __name__ == "__main__":
    Simulador_loja().run()
