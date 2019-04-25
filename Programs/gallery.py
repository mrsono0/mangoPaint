# coding: utf-8
# python3.5.3
# gallery.py
# ------------------------------------------------------------------------
# purpose:
#   메인화면 프레임에 갤러리 화면을 얹어 구동시킴.

import os

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp


class Gallery(object):
    manager_swiper = None
    main_widget = None
    directory = None

    