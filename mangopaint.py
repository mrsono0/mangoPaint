# mangopaint.py
# python3.5.3,   coding: utf-8
# Screen Manager P/G : Screen Controller

import os
from random import choice
import traceback

import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty
from kivy.utils import get_hex_from_color, get_color_from_hex

from programs.start import Start
from Libs.uix.main_screen import MainScreen
from Libs.uix.mainmenu import MainMenuItem
from Libs.uix.actionmenu import ActionMenu
from Libs import settings

# from programs.gallery import Gallery
# from programs.camera import Camera
# from programs.settings import Settings
# from programs.filter import Filter
# from programs.segment import Segment
# from programs.mystuio import MyStudio
# from programs.paint import Paint
# from programs.purchase import Purchase

# from kivy.utils import platform

kivy.require('1.10.1')
__version__ = "0.0.1"

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()

platform = 'android'
if platform == 'android':
    Config.set('kivy', 'keyboard_mode', 'system')
    Config.set('graphics', 'width', '350')
    Config.set('graphics', 'height', '550')
    Config.set('graphics', 'resize', '0')


class MangoPaint(App):
    main_screen = ObjectProperty(None)
    screen = ObjectProperty(None)
    window_text_size = NumericProperty(15)

    def __init__(self, **kwargs):
        super(MangoPaint, self).__init__(**kwargs)
        Window.bind(on_keybord=self.events_function)

        self.Screen = Screen
        self.Clock = Clock
        self.mainmenu = MainMenuItem
        self.choice = choice
        self.get_color_from_hex = get_color_from_hex
        self.get_hex_from_color = get_hex_from_color
        self.settings = settings

    def build(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@")
        Start()