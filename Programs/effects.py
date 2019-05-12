# coding: utf-8
# python3.5.3
# effects.py
# ------------------------------------------------------------------------
# purpose:
#   선택한 이미지 사진에 각종 필터들을 적용하여 보여주는 기능

import os
import sys
import glob

from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty

from kivymd.imagelists import SmartTile
from kivymd.utils.cropimage import crop_image


directory = os.path.split(os.path.abspath(sys.argv[0]))[0]


class Effects(Screen):
    pass