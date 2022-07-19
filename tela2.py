from kivy.uix.screenmanager import Screen

class Menu(Screen):
    def voltar(self):
        self.parent.transition.direction = 'right'
        self.parent.current = 'Menu_Principal'
    pass
