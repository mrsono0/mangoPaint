# mangopaint.py
# python3.5.3,   coding: utf-8
# Screen Manager P/G : Screen Controller

import os
from random import choice
import traceback


from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.config import ConfigParser
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty
from kivy.utils import get_hex_from_color, get_color_from_hex

from Programs.startscreen import StartScreen

# from Libs.uix.mainmenu import MainMenuItem
# from Libs.uix.navigationmenu import NavigationMenu
from Libs import settings as sets
from Libs.uix.navigationdrawer import NavigationDrawer


# from programs.gallery import Gallery
# from programs.camera import Camera
# from programs.settings import Settings
# from programs.filter import Filter
# from programs.segment import Segment
# from programs.mystuio import MyStudio
# from programs.paint import Paint
# from programs.purchase import Purchase

# from kivy.utils import platform


root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()


class MangoPaint(App):
    main_screen = ObjectProperty(None)
    screen = ObjectProperty(None)
    window_text_size = NumericProperty(15)

    def __init__(self, **kwargs):
        super(MangoPaint, self).__init__(**kwargs)
        Window.bind(on_keybord=self.events_program)

        self.Screen = Screen
        self.Clock = Clock
        # self.mainmenu = MainMenuItem
        # self.choice = choice
        # self.get_color_from_hex = get_color_from_hex
        # self.get_hex_from_color = get_hex_from_color
        # self.sets = sets
        # self.name_program = settings.string_lang_title
        # self.navigation_drawer = NavigationDrawer(side_panel_width=230)
        # self.open_dialog = False

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'language', 'Korean')
        config.setdefault('General', 'theme', 'default')

    def build(self):
        # self.title = self.name_program
        # self.icon = 'Screens/resources/icons/logo.png'
        # self.use_kivy_sets = False

        # self.config = ConfigParser()
        # self.config.read('{}/mangopaint.ini'.format(sets.prog_path))
        # self.set_var_from_file_settings()

        self.start_screen = StartScreen(
            # color_action_bar=sets.color_action_bar,
            # color_body_program=sets.color_body_program,
            # color_tabbed_panel=sets.color_tabbed_panel,
            # tabbed_text=sets.string_lang_tabbed_menu.format(
            #     TEXT_SHOPS=sets.string_lang_tabbed_menu_shops,
            #     TEXT_LOCATIONS=sets.string_lang_tabbed_menu_locations,
            #     COLOR_TEXT_SHOPS=get_hex_from_color(sets.color_action_bar),
            #     COLOR_TEXT_LOCATIONS=sets.theme_text_color),
            # title_previous=self.name_program[1:],
            events_callback=self.events_program, sets=sets
        )

        # self.screen = self.start_screen
        # navigation_Panel = NavigationMenu(
        #     events_callback=self.events_program,
        #     items=sets.dict_navigation_items
        # )

        # Clock.schedule_interval(self.show_banners, 2)

        # self.navigation_drawer.add_widget(navigation_panel)
        # self.navigation_drawer.anim_type = 'slide_above_anim'
        # self.navigation_drawer.add_widget(self.start_screen)

        # return self.navigation_drawer

        # return self.screen


    def set_var_from_file_settings(self):
        self.language = sets.select_locale[
            self.config.get('General', 'language')
        ]


    def set_current_item_tabbed_panel(self, color_current_tab, color_tab):
        self.screen.ids.custom_tabbed.text = \
            sets.string_lang_tabbed_menu.format(
                TEXT_SHOPS=core.string_lang_tabbed_menu_shops,
                TEXT_LOCATIONS=core.string_lang_tabbed_menu_locations,
                COLOR_TEXT_SHOPS=color_tab,
                COLOR_TEXT_LOCATIONS=color_current_tab
            )


    def events_program(self, *args):
        print(args)

        if self.navigation_drawer.state == 'open':
            self.navigation_drawer.anim_to_state('closed')

        if len(args) == 2:
            event = args[1]
        else:
            try:
                _args = args[0]
                event = _args if isinstance(_args, str) else str(_args) if \
                    isinstance(_args, dict) else _args.id
            except AttributeError:
                event = args[1]

        if event == sets.string_lang_settings:
            pass
        elif evnet == sets.string_lang_exit_key:
            self.exit_program()
        elif event == sets.string_lang_license:
            self.show_license()
        elif event == 'navigation_drawer':
            self.navigation_drawer.toggle_state()
        elif event == sets.string_lang_tabbed_menu_locations:
            self.show_location()
        elif event == sets.string_lang_tabbed_menu_shops:
            self.back_screen()





    def exit_program(self, *args):

        def dismiss(*args):
            self.open_dialog = False

        def answer_callback(answer):
            if answer == sets.string_lang_yes:
                sys.exit(0)
            dismiss()

        if not self.open_dialog:
            KDialog(answer_callback=answer_callback, 
                    on_dismiss=dismiss,
                    separator_color=sets.separator_color,
                    title_color=get_color_from_hex(sets.theme_text_black_color),
                    title=self.name_program).show(
                text=sets.string_lang_exit.format(core.theme_text_black_color),
                text_button_ok=sets.string_lang_yes,
                text_button_no=sets.string_lang_no, param='query',
                auto_dismiss=True
            )
            self.open_dialog = True            


    def show_license(self):
        pass


    def show_location(self):
        pass

    def back_screen(self, event):
        if self.screen.ids.screenmanager.current == '':
            if event in (1001, 27):
                self.exit_program()
            return

        if len(self.screen.ids.screen_manager.screen) != 1:
            self.screen.ids.screen_manager.screen.pop()
        
        self.screen.ids.screen_manager.current = \
            self.screen.ids.screen_manager.screen_name[-1]

        # self.set_current_item_tabbed_panel(
        #     sets.theme_key_text_color, get_hex_from_color(sets.color_action_bar)
        # )

    def on_pause(self):
        return True


    def on_resume(self):
        print('on_resume')

    def on_stop(self):
        print('on_stop')