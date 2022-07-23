from kivymd.app import MDApp as App
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, BooleanProperty

class Shopping_Cart(Screen):
    def deselect_all(self):
        self.ids.shop_bar.right_action_items = [["checkbox-multiple-outline", lambda x: self.select_all()]]
        for i in self.ids.cart_layout.children:
            i.selected = False
            i.md_bg_color = "#cccccc"

    def select_all(self):
        self.ids.shop_bar.right_action_items = [["checkbox-multiple-marked", lambda x: self.deselect_all()]]
        for i in self.ids.cart_layout.children:
            i.selected = True
            i.md_bg_color = "#c6bcd1"

    pass

class ShoppingItems(MDCard, RectangularElevationBehavior):
    text = StringProperty()
    ripple_behavior = True
    def select_mode(self, selected):
        screen = App.get_running_app().root.get_screen("Shopping Cart")
        if self.selected:
            self.selected = False
            self.md_bg_color = "#cccccc"
            #screen.ids.shop_bar.right_action_items = [["checkbox-multiple-outline"]]
        else:
            self.selected = True
            self.md_bg_color = "#c6bcd1"
            #screen.ids.shop_bar.right_action_items = [["checkbox-multiple-outline"]]


