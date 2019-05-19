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
from subprocess import Popen, PIPE, STDOUT
from box import Box

from kivy.uix.boxlayout import BoxLayout
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

# Effects 초기 화면 클래스
class Effects(Screen):
    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바

    def __init__(self, **kwargs):
        super(Effects, self).__init__(**kwargs)
        self.pos = (0,0)
        self.size_hint = (1,1)
        self.config = ConfigParser()
        self.effects_data = Box()
        self.effects_data.pos = 0
        self.effects_data.list = []


    # effect 효과의 타이틀명, 샘플이지미파일, 효과 프로그램명 정보 읽어오기  
    def _get_effects(self):
        self.config.read(os.path.join(directory, 'Libs/mangopaint.ini'))        
        _items = self.config.items('Effects')
        for i, (key, _item) in enumerate(_items):
            img_sh = _item.split(',')
            _data = {'key': key, 'image': img_sh[0], 'pgm': img_sh[1], 'order': img_sh[2] }
            self.effects_data.list.append(_data)
        
    # effects.kv 에서 호출하는 effects 화면 생성하기
    def create_effects(self, selectedImagePath):
        self._get_effects()
        self.effects_data.list.sort(key=lambda x: x['order'], reverse=True)
        self.effectsbar = EffectsBar(meta=self.effects_data)
        self.ids.myimage.source = selectedImagePath
        self.add_widget(self.effectsbar, index=0)

    # effectsbar 화면 랜더링
    def update_effectsbar(self):
        self.effectsbar.update()

    # ###########################################
    # effect 효과를 적용하도록 화면 변경하가
    # ###########################################
    def change_to_image(self, image_pos):
        # self.image_data.pos = image_pos
        _data = self.effects_data.list[image_pos]
        cmd = []

        if _data.key == 'sketch':
            args = self.sketch_arguments(image_pos)
        elif _data.key == 'water_color':
            args = self.sketch_arguments(image_pos)
        elif _data.key == 'oil_color':
            args = self.sketch_arguments(image_pos)
        else: 
            args = self.sketch_arguments(image_pos)

        cmd.append(sys.executable or 'python3')
        cmd.append(args)
        print(cmd[0] + cmd[1])
        process = Popen(cmd[0] + cmd[1], shell=True, stdout=PIPE, stderr=STDOUT)
        out, err = process.communicate()
        errcode = process.returncode

        # self.image.source = self.image.gen_image()
        # self.image.reload()

    def choice_effect(self):
        pass

    def run_effect(self):
        pass

    def save_temp(self):
        pass

    def sketch_arguments(self, image_pos):
        # python3 edge_detecting.py --content=$1 --output=$2 --blurred=$3
        # python3 edge_detecting.py --content "../../../images/mosaic.jpg" --output "mosaic_edge_result.png" --blurred 3
        args = " {} --content {} --blurred {}".format(self.effects_data.list[image_pos].pgm, self.ids.myimage.source, '3')
        return args

        
    # def gen_image(self):
    #     return os.path.join(directory, 'Effects',
    #                         self.meta.list[image_pos].image)


# 스크린 하단에 위치해있는 effects 리스트 클래스
class EffectsBar(BoxLayout):
    """ Dynamic amount of effects images that can be selected"""

    def __init__(self, meta=None, **kwargs):
        self.meta = meta
        super().__init__(**kwargs)
        self.height = 70
        self.size_hint = (1, None)
        self.pos = (0, 0)
        self.update()

    def update(self):
        self.clear_widgets()
        for i in range(self.meta.pos - int(math.floor(len(self.meta.list)/2)),
                       self.meta.pos + int(math.ceil(len(self.meta.list)/2))):
            image_pos = i
            if image_pos < 0:
                image_pos = len(self.meta.list) + image_pos
            if image_pos >= len(self.meta.list):
                image_pos = image_pos - len(self.meta.list)
            img = EffectsImage(source=os.path.join(directory, 'Effects',
                                                self.meta.list[image_pos].image),
                            image_pos=image_pos, 
                            selected=True if image_pos == self.meta.pos else False)
            self.add_widget(img)


# effectsbar 에 들어가는 effects들의 이미지버튼들 클래스
class EffectsImage(ButtonBehavior, Image):
    """ effectsbar images. The current one will always have full opacity, 
        otherwise only ones being hovered over will be full opacity. """

    def __init__(self, image_pos=0, selected=False, **kwargs):
        self.image_pos = image_pos
        self.selected = selected
        super().__init__(**kwargs)
        self.width = 70
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
