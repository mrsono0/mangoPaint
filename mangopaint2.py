# mangopaint.py
# python3.5.3,   coding: utf-8
# Screen Manager P/G :  Controller

import os
import sys
from random import choice
# import traceback

from kivy.app import App
from kivy.uix.screenmanager import Screen

# from kivy.config import ConfigParser
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
# from kivy.utils import platform

from Programs.startscreen import StartScreen



from Libs import settings as sets
# from Libs.bugreport import BugReport

# from Programs.mainscreen import MainScreen: MainScreen
# from Programs.camera import Camera: MainScreen.Camera
# from Programs.bottom import Buttom: ManinScreen.Buttom

# from Programs.choice import Choice: Choice
# from Programs.filter import Filter: CHoice.filter

# from Programs.settings import Settings: Settings

# from Programs.segment import Segment: Segment

# from Programs.mystuio import MyStudio: MyStudio
# from Programs.paint import Paint: Paint
# from Programs.purchase import Purchase: Purchase

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()


class MangoPaint__(App):

    # import시  메모리 할당 및 초기값 넣어주는 섹션
    mainscreen = ObjectProperty(None)
    screen = ObjectProperty(None)

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = 'Mango Paint'

# 해당 클래스가 객체화될때 구동되는 섹션으로 관련된 컴포넌트들을 활성화시켜서 실제 running 되기 직전까지 만들어놓음.
    def __init__(self, **kwargs):
        super(MangoPaint, self).__init__(**kwargs)
        Window.bind(on_keybord=self.events_program)

        self.Screen = Screen
        self.Clock = Clock
        self.choice = choice
        self.sets = sets
        self.name_program = sets.string_lang_title

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'language', 'Korean')
        config.setdefault('General', 'theme', 'default')

# build 는 App 클래스에서는 App.run()으로 invoke 되며, 메인프로그램을 스타트 시킴.
# 단, 일반 프로그램은 build 함수를 만들지 않는다.
    def build(self):

        self.title = self.name_program
        self.icon = 'Screens/resources/imgs/mango.jpg'
        self.use_kivy_sets = False

# calling 과  called 함수의 파라미터 인자와 초기화까지 일치해야함. 아니면  
# 'typeerror object() takes no parameters' 
        self.start_screen = StartScreen(
            # title_previous=self.name_program,
            events_callback=self.events_program,
            sets=self.sets
        )

        self.screen = self.start_screen
        # Clock.schedule_interval(self.show_banners, 2)

        return self.screen
 
# 분기 프로그램 with events_callback로 함수를 파라미터로 전달하여 구동
# 연계할 프로그램명을 호출하고 연이어 프로그램명.kv 까지 동작시킬 터널을 뚫은 후,
# kv파일의 on-이벤트의 events_callback에 파리미터로 전달할 프로그램명을 기술하여
# 최종 원하는 프로그램을 기동할수 있도록 하는 패턴함수임.
    def events_program(self, *args):

        print(args)
        if len(args) == 2:
            event = args[1]
        else:
            try:
                _args = args[0]
                event = _args if isinstance(_args, str) else str(_args) if \
                    isinstance(_args, dict) else _args.id
            except AttributeError:
                event = args[1]
        if event == sets.string_lang_exit_key:
            self.exit_program()
        elif event in (1001, 27):
            self.back_screen(event)
        return True

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

    def back_screen(self, event):
        if self.screen.ids.screenmanager.current == '':
            if event in (1001, 27):
                self.exit_program()
            return

        if len(self.screen.ids.screen_manager.screen) != 1:
            self.screen.ids.screen_manager.screen.pop()
        
        self.screen.ids.screen_manager.current = \
            self.screen.ids.screen_manager.screen_name[-1]

    def on_pause(self):
        return True

    def on_resume(self):
        print('on_resume')

    def on_stop(self):
        print('on_stop')