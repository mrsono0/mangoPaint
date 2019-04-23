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

string_lang_title = 'mangopaint'


# dict_language = {
#     string_lang_on_korean: "korean",
#     string_lang_on_english: "english"
# }

# decorator = 'Data/Images/decorator.png'