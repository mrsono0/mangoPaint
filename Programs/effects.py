# coding: utf-8
# python3.5.3
# effects.py
# ------------------------------------------------------------------------
# purpose:
#   선택한 이미지 사진에 각종 필터들을 적용하여 보여주는 기능
#   필터의 대상들은 mangopaint.ini 에서 설정

import os
import sys
import math


from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.config import ConfigParser

from kivymd.imagelists import SmartTile
from kivymd.utils.cropimage import crop_image

from Libs.hover import MouseOver

directory = os.path.split(os.path.abspath(sys.argv[0]))[0]

class Effects(Screen):
    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바

    def __init__(self, **kwargs):
        super(Effects, self).__init__(**kwargs)
        self.pos = (0,0)
        self.size_hint = (1,1)
        self.effects_list = []
        self.config = ConfigParser()

    # effect 효과들 목록 얻어오기   
    def _get_effects(self):

        self.config.read(os.path.join(directory, 'Libs/mangopaint.ini'))        
        _items = self.config.items('Effects')
        for key, _item in _items:
            path_sh = _item.split()
            self.effects_list.extend(path_sh)        

    def create_effects(self, selectedImagePath):
        self._get_effects()
        # self.effects_bar = EffectsBar(meta=self.effects_list)
        self.ids.myimage.source = selectedImagePath
        # self.add_widget(self.effects_bar, index=0)

    # effects bar 업데이트
    def update_effects_bar(self):
        self.effects_bar.update()



class EffectsBar(BoxLayout):
    """ Dynamic amount of effects images that can be selected"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = 100
        self.size_hint = (1, None)
        self.pos = (0, 0)
        self.images = 10
        # self.update()

    def update(self):
        self.clear_widgets()
        for i in range(self.meta.pos - int(math.floor(self.images/2)),
                       self.meta.pos + int(math.ceil(self.images/2))):
            image_pos = i
            if image_pos < 0:
                image_pos = len(self.meta.list) + image_pos
            if image_pos >= len(self.meta.list):
                image_pos = image_pos - len(self.meta.list)
            img = EffectsImage(source=os.path.join(self.meta.base,
                                                self.meta.list[image_pos].image),
                            image_pos=image_pos,
                            selected=True if image_pos == self.meta.pos else False)
            self.add_widget(img)


class EffectsImage(ButtonBehavior, Image):
    """ effectsbar images. The current one will always have full opacity, 
        otherwise only ones being hovered over will be full opacity. """

    def __init__(self, image_pos=0, selected=False, **kwargs):
        self.image_pos = image_pos
        self.selected = selected
        super().__init__(**kwargs)
        self.width = 100
        if not self.selected:
            self.opacity = 0.6
        self.size_hint = None, None

    def on_press(self):
        if not self.selected:
            self.parent.parent.change_to_image(self.image_pos)

    def on_hover(self):
        if not self.selected:
            self.opacity = 1.0

    def on_exit(self):
        if not self.selected:
            self.opacity = 0.6



# 파일탐색기로는 이미지이외의 것들이 보여져서 그닥임. 이미지만 보이는 앨범으로 만들어져야함. 지금은 사용안함.
# class AlbumView(GridLayout):  

#     def __int__(self, **kwargs):
#         super().__init__(**kwargs)
