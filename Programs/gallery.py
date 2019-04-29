# coding: utf-8
# python3.5.3
# gallery.py
# ------------------------------------------------------------------------
# purpose:
#   메인화면 프레임에 갤러리 화면을 얹어 구동시킴.

import os
import glob

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class MyImage(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(self.source)


class Image_Gallery(GridLayout):

    def __init__(self, **kwargs):
        super(Image_Gallery, self).__init__(**kwargs)
        images = glob.glob('/home/ubuntu/Pictures/*.jpg')
        self.cols = 3
        for img in images:
            thumb = MyImage(source=img)
            self.add_widget(thumb)

    def callback(self, obj, touch):
        print(obj.source)

    