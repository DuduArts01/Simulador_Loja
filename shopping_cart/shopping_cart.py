from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

class Shopping_Cart(Screen):
    #def Product_in_cart(self):
    pass


class MD3Card(MDCard, RectangularElevationBehavior):
    text = StringProperty()
    pass


