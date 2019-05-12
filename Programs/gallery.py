# coding: utf-8
# python3.5.3
# gallery.py
# ------------------------------------------------------------------------
# purpose:
#   메인화면 프레임에 갤러리 화면을 얹어 구동시킴.

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



class Gallery(Screen):

    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바

    def __init__(self, **kwargs):
        super(Gallery, self).__init__(**kwargs)
        Clock.schedule_once(self.create_scrollview)

    def create_scrollview(self, dt):
        images = glob.glob('/home/ubuntu/Pictures/*.jpg')
        layout = GridLayout(
            cols=3,
            row_force_default=True,
            row_default_height=90,
            size_hint_y=None,
            spacing=5,
            padding=5,
        )
        layout.bind(minimum_height=layout.setter("height"))
        for i, img in enumerate(images):
            layout.add_widget(
                SmartTile(
                    id="Tile_{}".format(str(i)),
                    mipmap=True,
                    source=img,
                    on_release=self.callback,
                )
            )

        scrollview = ScrollView(
            size_hint=(1, None), 
            size=(Window.width, Window.height),
            do_scroll_x=False,
        )
        scrollview.add_widget(layout)
        self.view.add_widget(scrollview)

    def callback(self, obj):
        print(obj.source)
        self.manager.current = 'effects'

    