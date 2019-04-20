# coding: utf-8
# python3.5.3
# main.py

from kivy.app import App
from mangopaint import MangoPaint


class MangoPaintApp(App):
    def build(self):
        return MangoPaint()



if __name__ in ('__main__', '__android__'):
    MangoPaintApp().run()