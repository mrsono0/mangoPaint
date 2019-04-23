# settings.py
# python3.5.3,   coding: utf-8
# setting the  app configuration P/G : Screen setting

import os
import sys
import traceback

from kivy.config import ConfigParser

select_locale = {'Korean': 'korean', 'English': 'english'}

prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
_prog_path = os.path.abspath('.')


if not os.path.exists('{}/Data/mangpaint.ini'.format(_prog_path)) \
        or open('{}/Data/mangopaint.ini'.format(_prog_path)).read() == '':
    language = 'english'
    theme = 'default'
else:
    config = ConfigParser()
    config.read('{}/Data/mangopaint.ini'.format(_prog_path))
    theme = config.get('General', 'theme')
    language = select_locale[config.get('General', 'language')]

string_lang_title = 'mangopaint'


# dict_language = {
#     string_lang_on_korean: "korean",
#     string_lang_on_english: "english"
# }
# decorator = 'Data/Images/decorator.png'