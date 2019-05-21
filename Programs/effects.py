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
import collections
from subprocess import Popen, PIPE, STDOUT
from box import Box


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
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
    global_selectedImagePath = ''

    def __init__(self, **kwargs):
        super(Effects, self).__init__(**kwargs)
        self.pos = (0,0)
        self.size_hint = (1,1)
        self.config = ConfigParser()


    # effect 효과의 타이틀명, 샘플이지미파일, 효과 프로그램명 정보 읽어오기  
    def _get_effects(self):
        self.config.read(os.path.join(directory, 'Libs/mangopaint.ini'))        
        _items = self.config.items('Effects')
        for key, _item in _items:
            img_sh = _item.split(',')
            _data = {'key': key, 'image': img_sh[0], 'pgm': img_sh[1], 'order': img_sh[2]}
            self.effects_data.list.append(_data)
        
    # effects.kv 에서 호출하는 effects 화면 생성하기
    def create_effects(self, selectedImagePath):
        self.effects_data = Box()
        self.effects_data.pos = 0
        self.effects_data.list = []
        self._get_effects()
        self.effects_data.list.sort(key=lambda x: int(x['order']))
        self.effectsbar = EffectsBar(meta=self.effects_data)
        self.global_selectedImagePath = selectedImagePath
        self.ids.myimage.source = self.global_selectedImagePath
        self.add_widget(self.effectsbar, index=0)

    # effectsbar 화면 랜더링
    # def update_effectsbar(self):
    #     self.effectsbar.update()

    # ###########################################
    # effect 효과를 적용하도록 화면 변경하가
    # ###########################################
    def transform_to_image(self, image_pos):
        self.effects_data.pos = image_pos
        _data = self.effects_data.list[image_pos]
        cmd = []

        # if 조건이 exclusive 하지 않아 혹 조건을 빠져나갈수 있는 위험이 있으니 주의할것!
        # 우선 뉴럴스타일이면, 다음으로 특정스타일을 물어보는 식이라...
        if _data.pgm == 'neural_style.py':
            args, output = self.neural_style_arguments(image_pos, _data.key)

        elif _data.key == 'edge_detect':
            args, output = self.edge_detect_arguments(image_pos)
        elif _data.key == 'water_color':
            args, output = self.water_color_arguments(image_pos)
        elif _data.key == 'oil_color':
            args, output = self.oil_color_arguments(image_pos)
        else: 
            args, output = self.edge_detect_arguments(image_pos)

        cmd.append(sys.executable or 'python3')
        cmd.append(args)
        print(cmd[0] + cmd[1])
        process = Popen(cmd[0] + cmd[1], shell=True, stdout=PIPE, stderr=STDOUT)
        out, err = process.communicate()
        self.ids.myimage.source = output
        print('effect function end: ' + _data.key + ' <==================')
        self.ids.myimage.reload()





    # 뉴럴스타일 방식의 패턴은 아래 함수로 집중
    def neural_style_arguments(self, image_pos, key):
        # python3 ./fast_neural_style/neural_style.py eval --content-image ../../../images/Colorful-Paint-with-Paper-Texture.jpg --model ./fast_neural_style/saved_models/mosaic.model --output-image ../Data/temp.png --cuda 0
        _pgm = os.path.join(directory, 'Effects/fast_neural_style', self.effects_data.list[image_pos].pgm)
        output = os.path.join(directory, 'Data', 'temp.png')
        _cuda = 1
        _model = os.path.join(directory, 'Effects/fast_neural_style/saved_models', key + '.model')
        args = " {} eval --content-image {} --model {} --output-image {} --cuda {}".format(_pgm, self.global_selectedImagePath, _model, output, _cuda)
        return args, output


    # 흑백 스케치 느낌 (아직은 칼라네요....)
    def edge_detect_arguments(self, image_pos):
        # python3 edge_detecting.py --content=$1 --output=$2 --blurred=$3
        # python3 edge_detecting.py --content "../../../images/mosaic.jpg" --output "../Data/mosaic_edge_result.png" --blurred 3
        _pgm = os.path.join(directory, 'Effects', self.effects_data.list[image_pos].pgm)
        output = os.path.join(directory, 'Data', 'temp.png')
        args = " {} --content {} --output {} --blurred {}".format(_pgm, self.global_selectedImagePath, output, 3)
        return args, output


    # 유화 느낌
    def oil_color_arguments(self, image_pos):
        # python oil_painting.py --content=$1 --output=$2 --radius=$3 --intensity=$4
        # python3 oil_coloring.py --content "../../../images/mosaic.jpg" --output "../Data/mosaic_oil_result.png" --radius 5 --intensity 20
        _pgm = os.path.join(directory, 'Effects', self.effects_data.list[image_pos].pgm)
        output = os.path.join(directory, 'Data', 'temp.png')
        args = " {} --content {} --output {} --radius {}  --intensity {}".format(_pgm, self.global_selectedImagePath, output, 5, 20)
        return args, output


    # 수채화 느낌
    def water_color_arguments(self, image_pos):
        # python3 Water_coloring.py --content=$1 --output=$2
        # python3 water_coloring.py --content "../../../images/mosaic.jpg" --output "../Data/mosaic_water_result.png"
        _pgm = os.path.join(directory, 'Effects', self.effects_data.list[image_pos].pgm)
        output = os.path.join(directory, 'Data', 'temp.png')
        args = " {} --content {} --output {}".format(_pgm, self.global_selectedImagePath, output)
        return args, output



    # effects 화면에서 다시 갤러리 화면으로 돌아갈때.
    def remove_effects_widgets(self):
        print('destroyed')
        self.effects_data.clear()

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
        layout = GridLayout(
            rows=1,
            row_force_default=True,
            row_default_height=90,
            size_hint_y=None,
            spacing=5,
            padding=5,
        )
        layout.bind(minimum_width=layout.setter("width"))
        for i in range(len(self.meta.list)):
            image_pos = i
            if self.meta.list[image_pos].pgm == 'neural_style.py':
                _path = 'Effects/fast_neural_style/saved_models'
            else:
                _path = 'Effects'
            img = EffectsImage(source=os.path.join(directory, _path,
                                                self.meta.list[image_pos].image),
                    image_pos=image_pos)
            layout.add_widget(img)

        scrollview = ScrollView(
            size_hint=(None, 1),
            size=(self.width, self.height),
            do_scroll_y=False,
        )
        scrollview.add_widget(layout)
        # self.id.view.add_widget(scrollview)
        # self.add_widget(scrollview)




# effectsbar 에 들어가는 effects들의 이미지버튼들 클래스
class EffectsImage(ButtonBehavior, Image):
    """ effectsbar images. The current one will always have full opacity, 
        otherwise only ones being hovered over will be full opacity. """

    def __init__(self, image_pos=0, **kwargs):
        self.image_pos = image_pos
        super().__init__(**kwargs)
        # self.opacity = 0.6
        self.width = 70
        self.size_hint = None, None

    def on_press(self):
            # image_pos : effects images 중 선택된 이미지효과의 순번 위치
        self.parent.parent.transform_to_image(self.image_pos)
            

    def on_hover(self):
        pass
        # self.opacity = 1.0

    def on_exit(self):
        pass
        # self.opacity = 0.6


# 파일탐색기로는 이미지이외의 것들이 보여져서 그닥임. 이미지만 보이는 앨범으로 만들어져야함. 지금은 사용안함.
# class AlbumView(GridLayout):  

#     def __int__(self, **kwargs):
#         super().__init__(**kwargs)
