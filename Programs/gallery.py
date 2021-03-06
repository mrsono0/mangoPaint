# coding: utf-8
# python3.5.3
# gallery.py
# ------------------------------------------------------------------------
# purpose:
#   메인화면 프레임에 갤러리 화면을 얹어 구동시킴.

import os
import glob

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty

from kivymd.imagelists import SmartTile


class Gallery(Screen):

    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바
    selectedImagePath = StringProperty('')

    def __init__(self, **kwargs):
        super(Gallery, self).__init__(**kwargs)
        Clock.schedule_once(self.create_scrollview)

    def create_scrollview(self, dt):
        images = []
        for ext in ('*.gif', '*.png', '*.jpg', '*.jpeg'):
            # images.extend(sorted(glob.glob(os.path.join('/Users/jarvis/Pictures', ext)), key=os.path.getmtime))
            images.extend(sorted(glob.glob(os.path.join('/home/ubuntu/Pictures', ext)), key=os.path.getmtime))            
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
                    on_release=self.callback,  # 모바일에서는 on_touch_down 이벤트로 ???
                )
            )

        scrollview = ScrollView(
            size_hint=(1, None),
            size=(Window.width, Window.height),
            do_scroll_x=False,
        )
        scrollview.add_widget(layout)
        self.container.add_widget(scrollview)


    def callback(self, obj):
        print(obj.source)
        self.selectedImagePath = obj.source
        self.parent.current = 'effects'
        
