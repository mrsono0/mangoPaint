# coding: utf-8
# python3.5.3
# mangopaint.py
# ------------------------------------------------------------------------
# purpose:
#   메인화면에서 눌려진 각 화면 보여주기와 앱의 보여주기 기능

import os

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp

from kivymd.utils.cropimage import crop_image


class Screens(object):
    main_widget = None
    directory = None
    screen_shop_window = None
    screen_coffee_menu = None
    screen_fitness_club = None

    def show_gallery(self):
        from demo_apps.shopwindow import screen_shop_window, ShopWindow

        if not self.screen_shop_window:
            Builder.load_string(screen_shop_window)
            self.screen_shop_window = ShopWindow()
            self.main_widget.ids.scr_mngr.add_widget(self.screen_shop_window)

    def show_purchase(self):
        from demo_apps.coffeemenu import screen_coffee_menu, CoffeeMenu

        self.main_widget.ids.toolbar.height = 0
        if not self.screen_coffee_menu:
            Builder.load_string(screen_coffee_menu)
            self.screen_coffee_menu = CoffeeMenu()
            self.main_widget.ids.scr_mngr.add_widget(self.screen_coffee_menu)

    def show_mystudio(self):
        from demo_apps.fitnessclub import screen_fitness_club, FitnessClub

        self.main_widget.ids.toolbar.height = 0
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Gray'
        if not self.screen_fitness_club:
            Builder.load_string(screen_fitness_club)
            self.screen_fitness_club = FitnessClub()
            self.main_widget.ids.scr_mngr.add_widget(self.screen_fitness_club)    