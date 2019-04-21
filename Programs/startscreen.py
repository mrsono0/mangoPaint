# start.py
# python3.5.3,   coding: utf-8
# Start Screen P/G : main scre

import os

# from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty, StringProperty

# from kivymd.theming import ThemeManager
from kivymd.utils.cropimage import crop_image

# from kivymd.toolbar import MDToolbar
# from kivymd.imagelists import SmartTileWithLabel
# from kivymd.imagelists import SmartTileWithStar
# from kivymd.imagelists import SmartTile

# from Libs.uix.custombutton import CustomButton

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()


class StartScreen(BoxLayout):

    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)

    _root = os.path.abspath('.')
    Builder.load_file('{}/Screens/startscreen.kv'.format(_root))

    def __init__(self, **kvargs):
        super(StartScreen, self).__init__(**kvargs)
        events_callback = self.events_callback



    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image
