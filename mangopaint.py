# mangopaint.py
# python3.5.3,   coding: utf-8
# Screen Manager P/G :  Controller
# ------------------------------------------------------------------------
# Notice:
#   - 프로젝트 레벨에서의 설정값들 확인하는 기능으로 역시 화면 없음.
#     메인화면인 StartScreen 은 베이스화면
#   - window size: Put the Config settings before all the other imports
#   - it's too late after importing Window
#   -

import os
import sys

from ast import literal_eval

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.logger import PY2
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.utils import get_hex_from_color, get_color_from_hex

from kivymd.theming import ThemeManager

from main import __version__

from Programs.startscreen import StartScreen

from Libs.translation import Translation
from Libs.lists import Lists
from Libs.dialogs import card
from Libs import settings as sets

# from Programs.choice import Choice: Choice
# from Programs.filter import Filter: CHoice.filter
# from Programs.settings import Settings: Settings
# from Programs.segment import Segment: Segment
# from Programs.mystuio import MyStudio: MyStudio
# from Programs.paint import Paint: Paint
# from Programs.purchase import Purchase: Purchase


# import시  메모리에 변수 할당 및 초기값 넣어주는 섹션
# mainscreen = ObjectProperty(None)
# screen = ObjectProperty(None)
class MangoPaint(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = 'Mango Paint'
    icon = 'Screens/resources/imgs/mango.jpg'
    screen = ObjectProperty(None)
    lang = StringProperty('en')

    # 해당 클래스가 객체화될때 구동되는 섹션으로 관련된 컴포넌트들을 활성화시켜서 실제 running 되기 직전까지 만들어놓음.
    def __init__(self, **kwargs):
        super(MangoPaint, self).__init__(**kwargs)
        Window.bind(on_keybord=self.events_program)
        Window.soft_input_mode = 'below_target'

        self.list_previous_screens = ['gallery']
        self.window = Window
        self.config = ConfigParser()
        self.manager = None
        self.window_language = None
        self.exit_interval = False
        self.name_program = sets.string_lang_title
        self.sets = sets

        self.dict_language = literal_eval(
            open(
                os.path.join(self.directory, 'Libs', 'locales', 'locales.txt')).read()
        )

        self.translation = Translation(
            self.lang, 'Ttest', os.path.join(self.directory, 'Libs', 'locales')
        )

    # application 레벨 설정값 정보 관리
    def get_application_config(self):
        return super(MangoPaint, self).get_application_config(
                        '{}/Libs/mangopaint.ini'.format(self.directory))

    def set_value_from_config(self):
        ''' mangopaint.ini 로 셋팅값 넣기 '''
        self.config.read(os.path.join(self.directory, 'Libs/mangopaint.ini'))
        self.lang = self.config.get('General', 'language')

    def build_config(self, config):
        ''' mangopaint.ini 기본 설정값 만들기 '''
        config.adddefaultsection('General')
        config.setdefault('General', 'language', 'English')

    # build 는 App 클래스에서는 App.run()으로 invoke 되며, 메인프로그램을 스타트 시킴.
    # 단, 일반 프로그램은 build 함수를 만들지 않는다.
    def build(self):
        # mangopaint.ini 의 저장된 설정값들을 셋팅하기
        self.set_value_from_config()
        self.title = sets.string_lang_title[:-1]
        self.icon = "Screens/resources/icons/logo.png"
        self.load_all_kv_files(os.path.join(self.directory, 'Screens'))
        # 메인 베이스가 되는 화면, 각 서브화면들은 screenmanager 로 switch 하면서 사용함
        self.start_screen = StartScreen(
            title_previous=self.name_program,
            events_callback=self.events_program,
            sets=sets
        )
        self.screen = self.start_screen
        self.manager = self.screen.ids.root_manager
        self.nav_drawer = self.screen.ids.nav_drawer
        return self.screen

    def load_all_kv_files(self, directory_kv_files):
        # i = 0
        print('kv-files: ', os.listdir(directory_kv_files))
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            # i = i+1
            # print('==========================================================')
            # print('kv-file: ', str(i), ': ', kv_file)
            if os.path.isfile(kv_file):
                with open(kv_file, encoding='utf-8') as kv:
                    _kv = kv.read()
                    Builder.load_string(_kv)
                    # print(_kv)  # kivy 파일들 syntax 오류 점검시 필요

    # 분기 프로그램 with events_callback로 함수를 파라미터로 전달하여 구동
    # 연계할 프로그램명을 호출하고 연이어 프로그램명.kv 까지 동작시킬 터널을 뚫은 후,
    # kv파일의 on-이벤트의 events_callback에 파리미터로 전달할 프로그램명을 기술하여
    # 최종 원하는 프로그램을 기동할수 있도록 하는 패턴함수임.
    def events_program(self, *args):
        '''프로그램 이벤트 처리'''
        print(args)
        if len(args) == 2:  # url 사용시
            event = args[1]
        else:   # 프로그램 버튼 클릭시
            try:
                _args = args[0]
                event = _args if isinstance(_args, str) else str(_args) if \
                    isinstance(_args, dict) else _args.id
            except AttributeError:
                event = args[1]

        # if PY2:
        #     if isinstance(event, unicode):
        #         event = event.encode('utf-8')

        if event == sets.string_lang_exit_key:
            self.exit_program()
        elif event == sets.string_lang_exit_key:
            self.exit_program()
        elif event == sets.string_lang_license:
            self.show_license()
        elif event == 'search_shop':
            self.search_shop()
        elif event == 'navigation_drawer':
            self.navigation_drawer.toggle_state()
        elif event in (1001, 27):
            self.back_screen(event=keyboard)
        return True

    def show_gallery(self, *args):
        print('show_gallery2')
        self.nav_drawer._toggle()
        self.manager.current = 'gallery'
        return self.screen

    def show_effect(self, *args):
        print('show_effect2')
        self.nav_drawer._toggle()
        self.manager.current = 'effects'
        return self.screen

    def show_mystudio(self, *args):
        print('show_mystudio2')
        pass

    def show_community(self, *args):
        print('show_community2')
        pass

    def show_purchase(self, *args):
        print('show_purchase2')
        pass

    def show_license(self, *args):
        if not PY2:
            self.screen.ids.license.ids.text_license.text = \
                self.translation._('%s') % open(
                    os.path.join(self.directory, 'LICENSE'), encoding='utf-8').read()
        else:
            self.screen.ids.license.ids.text_license.text = \
                self.translation._('%s') % open(
                    os.path.join(self.directory, 'LICENSE')).read()
        self.nav_drawer._toggle()
        self.manager.current = 'license'
        # self.screen.ids.action_bar.title = \
        #     self.translation._('MIT LICENSE')

    def show_about(self, *args):
        self.nav_drawer.toggle_nav_drawer()
        self.screen.ids.about.ids.label.text = \
            self.translation._(
                u'[size=20][b]MangoPaint[/b][/size]\n\n'
                u'[b]Version:[/b] {version}\n'
                u'[b]License:[/b] MIT License\n\n'
                u'[size=20][b]mangoPaint develop Team.[/b][/size]\n\n'
                u'[ref=www.miraelabs.com]'
                u'[color={link_color}]mango-saam, susan han, JM, \n Yoo Jung, Taeyoon Lee, 손정현 [/color][/ref]\n\n'
                u'[b]Source code:[/b] '
                u'[ref=REPO_PROJECT]'
                u'[color={link_color}]GitHub[/color][/ref]').format(
                version=__version__,
                link_color=get_hex_from_color(self.theme_cls.primary_color)
                )
        self.manager.current = 'about'

    def select_locale(self, *args):
        '''사용 가능한 언어 locale 이  있는 창을 표시합니다.
        응용 프로그램 언어 설정.'''

        def select_locale(name_locale):

            for locale in self.dict_language.keys():
                if name_locale == self.dict_language[locale]:
                    self.lang = locale
                    self.config.set('General', 'language', self.lang)
                    self.config.write()

        dict_info_locales = {}
        for locale in self.dict_language.keys():
            dict_info_locales[self.dict_language[locale]] = \
                ['locale', locale == self.lang]

        if not self.window_language:
            self.window_language = card(
                Lists(
                    dict_items=dict_info_locales,
                    events_callback=select_locale, flag='one_select_check'
                ),
                size=(.85, .55)
            )
        self.window_language.open()

    # 메인 화면에서 백 키 클릭시 사용
    def back_screen(self, event=None):
        if event in (1001, 27):
            if self.manager.current == 'gallery':
                self.dialog_exit()
                return
            try:
                self.manager.current = self.list_previous_screens.pop()
            except:
                self.manager.current = 'gallery'
            self.screen.ids.action_bar.title = self.title
            self.screen.ids.action_bar.left_action_items = \
                [['menu', lambda x: self.nav_drawer._toggle()]]

    def dialog_exit(self):
        def check_interval_press(interval):
            self.exit_interval += interval
            if self.exit_interval > 5:
                self.exit_interval = False
                Clock.unschedule(check_interval_press)
        if self.exit_interval:
            sys.exit(0)
        # Clock.schedule_interval(check_interval_press, 1)
        # toast(self.translation._('Press Back to Exit'))

    def on_lang(self, instance, lang):
        self.translation.switch_lang(lang)

    def on_pause(self):
        ''' 이렇게 하면 응용 프로그램이 '일시 중지'로 표시됩니다.
        그렇지 않으면 프로그램 시작 다시 '''
        return True

    def on_resume(self):
        print('on_resume')

    def on_stop(self):
        print('on_stop')

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
                text=sets.string_lang_exit.format(sets.theme_text_black_color),
                text_button_ok=sets.string_lang_yes,
                text_button_no=sets.string_lang_no, param='query',
                auto_dismiss=True
            )
            self.open_dialog = True
