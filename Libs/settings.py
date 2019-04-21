# settings.py
# python3.5.3,   coding: utf-8
# setting the  app configuration P/G : Screen setting

import os, sys
import traceback

from kivy.config import ConfigParser

select_locale = {'Korean': 'korean', 'English': 'english'}

prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]

if not os.path.exists('{}/mangpaint.ini'.format(prog_path)) \
        or open('{}/mangopaint.ini'.format(prog_path)).read() == '':
    language = 'english'
    theme = 'default'
else:
    config = ConfigParser()
    config.read('{}/mangopaint.ini'.format(prog_path))
    theme = config.get('General', 'theme')
    language = select_locale[config.get('General', 'language')]

# main screen settings
# config_theme = ConfigParser()
# config_theme.read("{}/Data/Themes/{theme}/{theme}.ini".format(
#     prog_path, theme=theme))

# color_action_bar = eval(config_theme.get("color", "color_action_bar"))
# color_body_program = eval(config_theme.get("color", "color_body_program"))
# color_tabbed_panel = eval(config_theme.get("color", "color_tabbed_panel"))
# separator_color = eval(config_theme.get("color", "separator_color"))
# background_locations = eval(config_theme.get("color", "background_locations"))
# theme_text_color = config_theme.get("color", "text_color")
# theme_text_black_color = config_theme.get("color", "text_black_color")
# theme_key_text_color = config_theme.get("color", "key_text_color")
# theme_link_color = config_theme.get("color", "link_color")

# exec(open('{}/Data/Language/{}.txt'.format(prog_path, language), encoding='utf-8-sig').read())

