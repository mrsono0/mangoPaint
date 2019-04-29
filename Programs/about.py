# coding: utf-8
# python3.5.3
# about.py
# ------------------------------------------------------------------------
# Notice:
#   - 


import webbrowser

from kivy.uix.screenmanager import Screen


class About(Screen):
    def open_url(self, instance, url):
        webbrowser.open(url)