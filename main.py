# coding: utf-8
# python3.5.3
# main.py
# ------------------------------------------------------------------------
# Notice:
#   - window size: Put the Config settings before all the other imports
#   - it's too late after importing Window

import os
import sys
import traceback

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.utils import get_hex_from_color

Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', 0)

from kivy.core.window import Window

from kivymd.theming import ThemeManager
from kivymd.utils.cropimage import crop_image
from kivymd.icon_definitions import md_icons
# from kivymd.material_resources import DEVICE_TYPE

from Programs.gallery import Gallery

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()

try:
    import kivy
    kivy.require('1.9.1')

except Exception:
    directory = os.path.split(os.path.abspath(sys.argv[0]))[0]
    traceback.print_exc(file=open('{}/error.log'.format(directory), 'w'))

__version__ = "0.0.1"


def toast(text):
    # FIXME: crush with Python3.
    try:
        from kivymd.toast import toast
    except TypeError:
        from kivymd.toast.kivytoast import toast
    toast(text)


class MangoPaint(App):

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGray'
    theme_cls.accent_palette = 'Gray'
    title = "MangoPaint"
    theme_cls.theme_style = 'Dark'
    main_widget = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Window = Window
        self.manager = None
        self.md_app_bar = None
        self.instance_menu_demo_apps = None
        self.md_theme_picker = None
        self.long_dialog = None
        self.input_dialog = None
        self.alert_dialog = None
        self.ok_cancel_dialog = None
        self.long_dialog = None
        self.dialog = None
        self.manager_open = False
        self.cards_created = False
        self.user_card = None
        self.bs_menu_1 = None
        self.bs_menu_2 = None
        self.my_snackbar = None
        self._interval = 0
        self.tick = 0
        self.create_stack_floating_buttons = False
        self.previous_text = \
            "Welcome to the application [b][color={COLOR}]Kitchen Sink" \
            "[/color][/b].\nTo see [b][color={COLOR}]KivyMD[/color][/b] " \
            "examples, open the menu and select from the list the desired " \
            "example or".format(COLOR=get_hex_from_color(
                self.theme_cls.primary_color))
        self.previous_text_end = \
            "for show example apps\n\n" \
            "Author - [b][color={COLOR}]Andrés Rodríguez[/color][/b]\n" \
            "[u][b][color={COLOR}]andres.rodriguez@lithersoft.com[/color]" \
            "[/b][/u]\n\n" \
            "Author this Fork - [b][color={COLOR}]Ivanov Yuri[/color][/b]\n" \
            "[u][b][color={COLOR}]kivydevelopment@gmail.com[/color]" \
            "[/b][u]".format(COLOR=get_hex_from_color(
                self.theme_cls.primary_color))
        self.names_contacts = (
            'Alexandr Taylor', 'Yuri Ivanov', 'Robert Patric', 'Bob Marley',
            'Magnus Carlsen', 'Jon Romero', 'Anna Bell', 'Maxim Kramerer',
            'Sasha Gray', 'Vladimir Ivanenko')
        self.demo_apps_list = [
            'Shop Window', 'Coffee Menu', 'Fitness Club', 'Registration']
        self.menu_for_demo_apps = []
        Window.bind(on_keyboard=self.events)

        crop_image((Window.width, int(dp(Window.height * 35 // 100))),
                   '{}/Screens/resources/imgs/mango.jpg'.format(
                       self.directory),
                   '{}/Screens/resources/imgs/mango.jpg'.format(
                       self.directory))

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        """Crop images for Grid screen."""

        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image

    def file_manager_open(self):
        from kivymd.filemanager import MDFileManager
        from kivymd.dialog import MDDialog

        def open_file_manager(text_item, dialog):
            previous = False if text_item == 'List' else True
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                              select_path=self.select_path,
                                              previous=previous)
            self.manager.add_widget(self.file_manager)
            self.file_manager.show(self.user_data_dir)
            self.manager_open = True
            self.manager.open()

        MDDialog(
            title='Title', size_hint=(.8, .4), text_button_ok='List',
            text="Open manager with 'list' or 'previous' mode?",
            text_button_cancel='Previous',
            events_callback=open_file_manager).open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;
        """

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager.dismiss()
        self.manager_open = False
        self.set_chevron_menu()

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def build(self):
        self.main_widget = Builder.load_file('{}/Screens/main.kv'.format(root))
        return self.main_widget

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            from kivymd.dialog import MDDialog

            self.alert_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Alert dialog",
                events_callback=self.callback_for_menu_items)
        self.alert_dialog.open()

    def show_example_ok_cancel_dialog(self):
        if not self.ok_cancel_dialog:
            from kivymd.dialog import MDDialog

            self.ok_cancel_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Ok Cancel dialog", text_button_cancel='Cancel',
                events_callback=self.callback_for_menu_items)
        self.ok_cancel_dialog.open()

    def show_example_long_dialog(self):
        if not self.long_dialog:
            from kivymd.dialog import MDDialog

            self.long_dialog = MDDialog(
                text="Lorem ipsum dolor sit amet, consectetur adipiscing "
                     "elit, sed do eiusmod tempor incididunt ut labore et "
                     "dolore magna aliqua. Ut enim ad minim veniam, quis "
                     "nostrud exercitation ullamco laboris nisi ut aliquip "
                     "ex ea commodo consequat. Duis aute irure dolor in "
                     "reprehenderit in voluptate velit esse cillum dolore eu "
                     "fugiat nulla pariatur. Excepteur sint occaecat "
                     "cupidatat non proident, sunt in culpa qui officia "
                     "deserunt mollit anim id est laborum.",
                title='Title', size_hint=(.8, .4), text_button_ok='Yes',
                events_callback=self.callback_for_menu_items)
        self.long_dialog.open()

    def set_title_toolbar(self, title):
        """Set string title in MDToolbar for the whole application."""

        self.main_widget.ids.toolbar.title = title

    def set_error_message(self, *args):
        """Checks text of TextField with type "on_error"
        for the screen TextFields."""

        text_field_error = args[0]
        if len(text_field_error.text) == 2:
            text_field_error.error = True
        else:
            text_field_error.error = False

    def set_list_md_icons(self, text='', search=False):
        """Builds a list of icons for the screen MDIcons."""

        def add_icon_item(name_icon):
            self.main_widget.ids.scr_mngr.get_screen(
                'md icons').ids.rv.data.append(
                {
                    'viewclass': 'MDIconItemForMdIconsList',
                    'icon': name_icon,
                    'text': name_icon,
                    'callback': self.callback_for_menu_items
                }
            )


        self.main_widget.ids.scr_mngr.get_screen('md icons').ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

    def set_menu_for_demo_apps(self):
        if not len(self.menu_for_demo_apps):
            for name_item in self.demo_apps_list:
                self.menu_for_demo_apps.append(
                    {'viewclass': 'OneLineListItem',
                     'text': name_item,
                     'on_release': lambda x=name_item: self.show_demo_apps(x)})

    def show_demo_apps(self, name_item):
        name_item = name_item.lower()
        {
            'coffee menu': self.show_coffee_menu,
            'shop window': self.show_shop_window,
            'registration': self.show_registration_form_one,
            'fitness club': self.show_fitness_club}[name_item]()
        self.main_widget.ids.scr_mngr.current = name_item
        self.instance_menu_demo_apps.dismiss()


    def on_pause(self):
        return True

    def on_stop(self):
        pass

    def open_settings(self, *args):
        return False


if __name__ == ('__main__'):
    MangoPaint().run()
