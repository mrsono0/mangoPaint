# start.py
# python3.5.3,   coding: utf-8
# Start Screen P/G : main scre

import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.utils.cropimage import crop_image


root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
_root = os.path.abspath('.')
Builder.load_file('{}/Screens/startscreen.kv'.format(_root))

class StartScreen(BoxLayout):

    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        Window.bind(on_keybord=self.events_program)
        self.events_callback = self.self.events_callback
        self.sets = sets       
     

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image
