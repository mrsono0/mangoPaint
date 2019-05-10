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
        Clock.schedule_once(self.create_scrollview)

    def create_scrollview(self, dt):
        images = glob.glob('/Users/jarvis/Pictures/*.jpg')
        # base = ["Tile_{}".format(i) for i in len(images)]
        layout = GridLayout(
            cols=3,
            row_default_height=(self.width - self.cols * self.spacing[0])/self.cols,
            row_force_default=True,
            size_hint_y=None,
            height=self.minimum_height,
            padding=(dp(4), dp(4)),
            spacing=4,
        )
        layout.bind(minimum_height=layout.setter("height"))
        for img in images:
            layout.add_widget(
                SmartTile(
                    mipmap=True,
                    font_style='Subhead',
                )
            )
        scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scrollview.add_widget(layout)
        self.view.add_widget(scrollview)

    # def _on_enter(self, instance_toolbar, instance_program):
    #     instance_toolbar.left_action_items = []
    #     instance_toolbar.title = instance_program.title

    def callback(self, obj, touch):
        print(obj.source)

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        if not os.path.exists(os.path.join(directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image    
    