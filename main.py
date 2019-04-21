# coding: utf-8
# python3.5.3
# main.py


import os
import sys
import traceback

from kivy.app import App
from kivy.config import Config
from mangopaint import MangoPaint

directory = os.path.split(os.path.abspath(sys.argv[0]))[0]

Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', 0)

try:
    # import kivy
    # kivy.require('1.9.1')
    # from Libs.bugreport import BugReport
    pass
except Exception:
    traceback.print_exc(file=open('{}/error.log'.format(directory), 'w'))


__version__ = "0.0.1"


class main():
    app = None
    app = MangoPaint()
    # laod_ads(app)
    app.run()


if __name__ in ('__main__', '__android__'):
    main()
