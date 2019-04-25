# settings.py
# python3.5.3,   coding: utf-8
# setting the  app configuration P/G : Screen setting

import os
import sys

from kivy.config import ConfigParser

select_locale = {'한글': 'korean', 'English': 'english'}

prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
# _prog_path = os.path.abspath('.')


if not os.path.exists('{}/Data/mangpaint.ini'.format(prog_path)) \
        or open('{}/Data/mangopaint.ini'.format(prog_path)).read() == '':
    language = 'english'
    theme = 'default'
else:
    config = ConfigParser()
    config.read('{}/Data/mangopaint.ini'.format(prog_path))
    theme = config.get('General', 'theme')
    language = select_locale[config.get('General', 'language')]

string_lang_title = 'mangopaint'
string_lang_exit_key = 'exit'
string_lang_yes = True

# dict_language = {
#     string_lang_on_korean: "korean",
#     string_lang_on_english: "english",
# }


decorator = 'Screens/resources/imgs/decorator.png'
