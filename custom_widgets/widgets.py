from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RectangularElevationBehavior

class MD3Card(MDCard, RectangularElevationBehavior):
    text = StringProperty()
    ripple_behavior = True

