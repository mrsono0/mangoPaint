import os
import sys

from kivy.app import App


class Gallery(object):
    def __init__(self):
        pass


# coding: utf-8
# main.py

import os
import sys
import traceback


directory = os.path.split(os.path.abspath(sys.argv[0]))[0]
try:
    import kivy
    from kivy.app import App
    from kivy.uix.screenmanager import Screen, SwapTransition
    from kivy.config import Config
    from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
    from kivy.lang import Builder
    from kivy.utils import platform
    from libs.bugreport import BugReport, ErrorReport
except Exception:
    BugReport().run()
    ErrorReport()
    traceback.print_exc(file=open('{}/logs/error.log'.format(directory), 'w'))
    sys.exit(1)

kivy.require('1.10.1')
__version__ = "0.0.1"

# if platform == 'android':
#     Config.set('kivy', 'keyboard_mode', 'system')
#     Config.set('graphics', 'width', '400')
#     Config.set('graphics', 'height', '700')
#     Config.set('graphics', 'resize', '0')

Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', '0')

root = os.path.split(__file__)[0]
Builder.load_file(
    '{}/mangopaint.kv'.format(root if root != '' else os.getcwd())
)


# declare screens
class Gallery(Screen):
    pass

class Camera(Screen):
    pass

class Process(Screen):
    pass

class Segment(Screen):
    pass

class Paint(Screen):
    pass

class MyStudio(Screen):
    pass

class Purchase(Screen):
    pass

# 

class MangoPaintApp(App):
    """
    doc string
    """
    try:
        Gallery()
    except Exception:
        text_error = traceback.format_exc()
        open('{}/logs/error.log'.format(directory), 'w').write(text_error)
        print(text_error)

        if App:
            pass
            # App.start_screen.clear_widgets()
        
        ErrorReport()


if __name__ == "__main__":
    MangoPaintApp().run()
