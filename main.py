# coding: utf-8
# python3.5.3
# main.py

from kivy.app import App

from programs.mangopaint import MangoPaint


class MangoPaintApp(App):
    def build(self):
        print("%%%%%%%%%%%%%%%%%%%%%%%")
        return MangoPaint()


if __name__ == "__main__":
    MangoPaintApp().run()
