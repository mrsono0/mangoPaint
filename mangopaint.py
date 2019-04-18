# mangopaint.py
# python3.5.3,   coding: utf-8
# Screen Manager P/G : Screen Controller

import os
import traceback

import kivy

from kivy.uix.screenmanager import ScreenManager
from programs.start import Start

# from programs.gallery import Gallery
# from programs.camera import Camera
# from programs.settings import Settings
# from programs.filter import Filter
# from programs.segment import Segment
# from programs.mystuio import MyStudio
# from programs.paint import Paint
# from programs.purchase import Purchase

from kivy.config import Config
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


class MangoPaint(ScreenManager):
    print("++++++++++++++++++++")

    def __init__(self, **kwargs):
        super(MangoPaint, self).__init__(**kwargs)
        print("**************************")
        self.build()

    def build(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@")
        Start()