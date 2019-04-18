# coding: utf-8
# bugreport.py
# """
# """
# MIT LICENSE
# author : Jeongmin Kang
# email: asiason21@gmail.com
# version: 0.0.1

import os

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.app import App

import webbrowser
import six.moves.urllib


root = os.path.split(__file__)[0]
if root == '':
    root = os.getcwd()


class BugReport(FloatLayout):
    title = 'Bug Report'
    label_info = StringProperty("Soory, an error occured in the program.")
    info_text = StringProperty("You can report this bug using button bellow, \
        helping us to fix it.")
    info_report = StringProperty("")

    callback_clipboard = ObjectProperty(None)
    callback_report = ObjectProperty(None)

    report_readonly = BooleanProperty(False)

    icon_background = StringProperty('../Screens/icons/under-construction.png')

    button_clipboard = StringProperty('Copy Bug')
    button_report = StringProperty('Report Bug')
    button_close = StringProperty('Close')

    def __init__(self, **kwargs):

        super(BugReport, self).__init__(**kwargs)
        if not os.path.exists(self.icon_background):
            self.icon_background = '../Screens/icons/under-construction.png'

        info_buttons = {
            self.button_clipboard: self.callback_clipboard,
            self.button_report: self.callback_report
        }
        for info_button in info_buttons.key():
            if callable(info_buttons[info_button]):
                self.ids.box_layout.add_widget(
                    Button(text=info_button, on_press=info_buttons[info_button])
                )

    def on_close(self, *args):
        from kivy.app import App
        App.get_running_app().stop()


class ErrorReport(App):
    """
    """
    def callback_report(self, *args):
        try:
            text = six.moves.urllib.parse.quote( \
                self.win_report.txt_traceback.text.encode('utf-8'))
            url = 'https://github.com/jarvis0516/MangoPaint/issues/new?body=' \
                + text
            webbrowser.open(url)
        except Exception:
            sys.exit(1)

    def build(self):
        self.win_report = BugReport(
            callback_report = self.callback_report, 
            txt_report = text_error,
            icon_background ='../Screens/icons/under-construction.png'
        )
        return self.win_report      