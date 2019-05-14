# settings.py
# python3.5.3,   coding: utf-8
# setting the  app configuration P/G : Screen setting

import os
import sys

from kivy.config import ConfigParser

select_locale = {'한글': 'korean', 'English': 'english'}

prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
# _prog_path = os.path.abspath('.')


if not os.path.exists('{}/Libs/mangopaint.ini'.format(prog_path)) \
        or open('{}/Libs/mangopaint.ini'.format(prog_path)).read() == '':
    language = 'english'
    theme = 'default'
else:
    config = ConfigParser()
    config.read('{}/Libs/mangopaint.ini'.format(prog_path))
    theme = config.get('General', 'theme')
    language = select_locale[config.get('General', 'language')]

string_lang_title = 'mangopaint'
string_lang_exit_key = 'exit'
string_lang_yes = True
text_color = 'Black'
string_lang_own_provider = 'add_account_own_provider'
string_lang_create_account = 'create_account'
string_lang_introduction = 'introduction'
string_lang_next = 'Next'
string_lang_enter_user_name = 'enter_user_name'
background = [0.3,0.3,0.3,0.3]
rectangle = [1,1,1,1]
list_color = [0.5, 0.5,0.5,0.5]
string_lang_cancel = 'Cancel'


# dict_language = {
#     string_lang_on_korean: "korean",
#     string_lang_on_english: "english",
# }


decorator = 'Screens/resources/imgs/decorator.png'
