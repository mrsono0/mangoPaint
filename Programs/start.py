# start.py
# python3.5.3,   coding: utf-8
# Screen P/G : Start Screen

import os

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from pathlib import Path

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()


class Start(Screen):
    Builder.load_file('{}/screens/start.kv'.format(Path(root).parent))

    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
