# start.py
# python3.5.3,   coding: utf-8
# Start Screen P/G : main scre

# import os
# import sys
# import inspect

# from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

# from kivymd.utils.cropimage import crop_image
# from kivy.uix.gridlayout import GridLayout

# from Programs.introduction import Introduction
# from Programs.addaccount import AddAccount
# from Programs.addaccountown import AddAccountOwn
# from Programs.createaccount import CreateAccount
# from Programs.gallery import Gallery
# from Programs.mystudio import MyStudio
# from Programs.purchase import Purchase


# root = os.path.split(__file__)[0]
# root = root if root != '' else os.getcwd()
# _root = os.path.abspath('.')
# main.py 에서 일괄적으로 /Screens 밑 kv 파일들을  읽어드리기 때문
# Builder.load_file('{}/Screens/startscreen.kv'.format(_root))


class StartScreen(BoxLayout):  # 메인화면 프레임과 스크린 메니저 화면 정의
    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.bind(on_keybord=self.events_callback)
        events_callback = self.events_callback
        sets = self.sets

    # def crop_image_for_tile(self, instance, size, path_to_crop_image):
    #     if not os.path.exists(
    #             os.path.join(self.directory, path_to_crop_image)):
    #         size = (int(size[0]), int(size[1]))
    #         path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
    #         crop_image(size, path_to_origin_image, path_to_crop_image)
    #     instance.source = path_to_crop_image
