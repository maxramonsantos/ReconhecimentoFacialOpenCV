from py_principal import TPrincipal


from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy import Config
from kivy.lang import Builder

Config.set('graphics', 'resizable', True)
Config.set('kivy', 'exit_on_escape', '0')
# Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'width', 1000)
Config.set('graphics', 'height', 600)

class GerenciadorTelas(ScreenManager):
    def __init__(self):
        super().__init__()
        self.tprincipal = TPrincipal()

        

        self.add_widget(self.tprincipal)