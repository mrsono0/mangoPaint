# coding: utf-8
# python3.5.3
# effects.py
# ------------------------------------------------------------------------
# purpose:
#   선택한 이미지 사진에 각종 필터들을 적용하여 보여주는 기능
#   필터의 대상들은 mangopaint.ini 에서 설정

import os
import sys

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

from kivymd.imagelists import SmartTile
from kivymd.utils.cropimage import crop_image



class Effects(Screen):
    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바

    def __init__(self, **kwargs):
        super(Effects, self).__init__(**kwargs)

    def create_effects(self, selectedImagePath):
        self.ids.myimage.source = selectedImagePath




# class EffectsBar(BoxLayout):
#     """ Dynamic amount of effects images that can be selected"""

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.height = 100
#         self.size_hint = (1, None)
#         self.pos = (0, 0)
#         self.images = 10
#         self.update()

#     # def update(self):
#     #     self.clear_widgets()
#     #     for i in range(self.meta.pos - int(math.floor(self.images/2)),
#     #                    self.meta.pos + int(math.ceil(self.images/2))):
#     #         image_pos = i
#     #         if image_pos < 0:
#     #             image_pos = len(self.meta.list) + image_pos
#     #         if image_pos >= len(self.meta.list):
#     #             image_pos = image_pos - len(self.meta.list)
#     #         img = MenuImage(source=os.path.join(self.meta.base,
#     #                                             self.meta.list[image_pos].image),
#     #                         image_pos=image_pos,
#     #                         selected=True if image_pos == self.meta.pos else False)
#     #         self.add_widget(img)


# class EffectsImage(ButtonBehavior, Image):
#     """ Preview image. The current one will always have full opacity, 
#         otherwise only ones being hovered over will be full opacity. """

#     def __init__(self, image_pos=0, selected=False, **kwargs):
#         self.image_pos = image_pos
#         self.selected = selected
#         super().__init__(**kwargs)
#         self.width = 100
#         if not self.selected:
#             self.opacity = 0.6
#         self.size_hint = None, None

#     def on_press(self):
#         if not self.selected:
#             self.parent.parent.change_to_image(self.image_pos)



# class MyImage(Image):

#     def __init__(self, meta=None, preview_bar=None, **kwargs):
#         self.meta = meta
#         if not preview_bar:
#             raise PyViewError("Preview_bar must be provided")
#         self.preview_bar = preview_bar
#         super().__init__(source=self.gen_image(), **kwargs)
#         self.pos = (0, 100)
#         self.size_hint_x = 1
#         self.size_hint_y = None








# class MainViewer(FloatLayout): # Effects 화면 전체

#     def __init__(self, base_dir=r"/home/james/Pictures",
#                  delete_dir=r"/home/james/delete", **kwargs):
#         super().__init__(**kwargs)


#         # effects_view: 하단의 각종 effects 를 선택할수 있는 scroll
#         self.effects_bar = EffectsBar(meta=self.image_data)
#         self.image = Image(meta=self.image_data, effects_bar=self.preview) # meta data에서 읽어오는 방식인데 바꿔야함


#         self.add_widget(self.image, index=2)
#         self.add_widget(self.effects_bar, index=0)

#     def update_effects_bar(self):
#         self.effects_bar.update()



# 파일탐색기로는 이미지이외의 것들이 보여져서 그닥임. 이미지만 보이는 앨범으로 만들어져야함. 지금은 사용안함.
# class AlbumView(GridLayout):  

#     def __int__(self, **kwargs):
#         super().__init__(**kwargs)
