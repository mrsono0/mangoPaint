# programdata.py
# python3.5.3,   coding: utf-8
# program ini-file setting P/G : set

import os
import sys
import traceback

from kivy.config import ConfigParser
from kivy.logger import PY2


select_locale = {'Korean': 'korean', 'English': 'english'}
prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]

if not os.path.exists('{}/program.ini'.format(prog_path)) \
        or open('{}/program.ini'.format(prog_path)).read() == '':
    language = 'korean'
    theme = 'default'
else:
    config = ConfigParser()
    config.read('{}/program.ini'.format(prog_path))
    theme = config.get('General', 'theme')
    language = select_locale[config.get('General', 'language')]

config_theme = ConfigParser()
config_theme.read("{}/Data/Themes/{theme}/{theme}.ini".format(
    prog_path, theme=theme))

color_action_bar = eval(config_theme.get("color", "color_action_bar"))
color_body_program = eval(config_theme.get("color", "color_body_program"))
color_tabbed_panel = eval(config_theme.get("color", "color_tabbed_panel"))
separator_color = eval(config_theme.get("color", "separator_color"))
background_locations = eval(config_theme.get("color", "background_locations"))
theme_text_color = config_theme.get("color", "text_color")
theme_text_black_color = config_theme.get("color", "text_black_color")
theme_key_text_color = config_theme.get("color", "key_text_color")
theme_link_color = config_theme.get("color", "link_color")

try:
    if not PY2:
        exec(
            open('{}/Data/Language/{}.txt'.format(
                prog_path, language), encoding='utf-8-sig').read()
        )
    else:
        exec(
            open('{}/Data/Language/{}.txt'.format(prog_path, language)).read()
        )
except Exception:
    raise Exception(traceback.format_exc())

dict_language = {
    string_lang_on_korean: "korean",
    string_lang_on_english: "english"
}

dict_locations = {
    'bed_room': string_lang_bed_room,
    'bath_room': string_lang_bath_room,
    'kitchen': string_lang_kitchen,
    'garden': string_lang_garden,
    'living_room': string_lang_living_room,
    'facade': string_lang_facade,
    'garage': string_lang_garage,
    'roof': string_lang_roof
}

dict_shops = {
    'british': string_lang_dasc_british,
    'epizenter': string_lang_dasc_epizenter,
    'lidl': string_lang_dasc_lidl,
    'merlin': string_lang_dasc_merlin,
    'obi':string_lang_dasc_obi
}

dict_navigation_items = [
    [string_lang_my_cabinet, 'Data/Images/cabinet.png'],
    [string_lang_my_shelves, 'Data/Images/shelves.png'],
    [string_lang_settings, 'Data/Images/settings.png']
]

image_buttons = {
    0: 'Data/Images/button.png',
    1: 'Data/Images/button.png',
    2: 'Data/Images/button.png'
}

image_shadows = {
    0: 'Data/Images/button_down.png',
    1: 'Data/Images/button_down.png',
    2: 'Data/Images/button_down.png'
}
decorator = 'Data/Images/decorator.png'