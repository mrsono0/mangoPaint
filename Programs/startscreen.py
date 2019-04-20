# start.py
# python3.5.3,   coding: utf-8
# Screen P/G : Start Screen

import os

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivy.properties import ObjectProperty, ListProperty, StringProperty

# from Libs.uix.custombutton import CustomButton

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()


class StartScreen(Screen):
    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    color_action_bar = ListProperty(
        [0.4, 0.11764705882352941, 0.2901960784313726, 0.5607843137254902]
    )
    color_body_program = ListProperty(
        [0.15294117647058825, 0.0392156862745098, 0.11764705882352941, 1]
    )
    color_tabbed_panel = ListProperty(
        [0.15294117647058825, 0.0392156862745098, 0.11764705882352941, 1]
    )
    title_previous = StringProperty('')
    tabbed_text = StringProperty('')

    _root = os.path.abspath('.')
    Builder.load_file('{}/Screens/startscreen.kv'.format(_root))

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.ids.custom_tabbed.bind(on_ref_press=self.events_callback)
        for name_shop in self.core.dict_shops.keys():
            self.ids.shops_list.add_widget(
                CustomButton(
                    text=self.core.dict_shops[name_shop],
                    icon='Data/Images/shops/{}.png'.format(name_shop),
                    icon_people='Data/Images/people.png',
                    icon_map='Data/Images/mapmarker.png',
                    events_callback=self.events_callback,
                )
            )