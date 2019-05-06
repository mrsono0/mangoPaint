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
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty


class MyImage(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(self.source)


class Gallery(Screen):

    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바

    def __init__(self, **kwargs):
        super(Gallery, self).__init__(**kwargs)

    def load_images(self):
        images = glob.glob('/home/ubuntu/Pictures/*.jpg')
        self.cols = 3
        for img in images:
            thumb = MyImage(source=img)
            # self.screen.ids.boxlayout_gallery.add_widget(thumb)

    def _on_enter(self, instance_toolbar, instance_program):
        instance_toolbar.left_action_items = []
        instance_toolbar.title = instance_program.title

    def callback(self, obj, touch):
        print(obj.source)

    