import sys
sys.dont_write_bytecode = True

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from Libs.dialogs import dialog, dialog_progress, input_dialog

try:
    from kivymd.theming import ThemeManager
except ImportError:
    raise ImportError('Install package KivyMD…')


class Test(App):
    dialog_test = ObjectProperty(None)
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Lime'

    def build(self):
        box = BoxLayout()
        box.add_widget(Button(text='Dialog', on_release=self.show_dialog))
        box.add_widget(Button(text='Dialog progress', on_release=self.show_progress))
        box.add_widget(Button(text='Dialog input', on_release=self.show_input))
 
        return box

    def close_dialog(self, *args):
        self.dialog_test.dismiss()

    def show_dialog(self, *args):
        self.dialog_test = dialog(
            buttons=[
                ['Exit', lambda *x: sys.exit(0)],
                ['Close ', lambda *x: self.close_dialog()]
            ]
        )

    def show_progress(self, *args):
        self.dialog_test, string_spinner = dialog_progress(events_callback=self.close_dialog)

    def show_input(self, *args):
        self.dialog_test = input_dialog(events_callback=self.close_dialog)


Test().run()