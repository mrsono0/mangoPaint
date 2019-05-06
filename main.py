# coding: utf-8
# python3.5.3
# main.py
# ------------------------------------------------------------------------
# Notice:
#   - 앱 레벨에서의 설정값들 확인하는 기능으로 화면 없음.
#   - window size: Put the Config settings before all the other imports
#   - it's too late after importing Window

import os
import sys
import traceback

from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', 0)


from kivymd.theming import ThemeManager
from kivymd.utils.cropimage import crop_image
from kivymd.icon_definitions import md_icons
# from kivymd.material_resources import DEVICE_TYPE

from Libs import settings as sets

directory = os.path.split(os.path.abspath(sys.argv[0]))[0]

try:
    import webbrowser
    try:
        import six.moves.urllib
    except ImportError:
        pass

    import kivy
    kivy.require('1.10.0')

    from kivymd.theming import ThemeManager
    from Libs.bugreporter import BugReporter
except Exception:
    traceback.print_exc(file=open(os.path.join(directory, 'error.log'), 'w'))
    print(traceback.print_exc())
    sys.exit(1)

__version__ = "0.0.2"


def main():

    def create_error_monitor():
        class _App(App):
            theme_cls = ThemeManager()
            theme_cls.primary_palette = 'Orange'

            def build(self):
                box = BoxLayout()
                box.add_widget(report)
                return box
        app = _App()
        app.run()

    app = None

    try:
        from mangopaint import MangoPaint

        app = MangoPaint()
        app.run()
    except Exception:
        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout

        text_error = traceback.format_exc()
        traceback.print_exc(file=open(os.path.join(directory, 'logs/error.log'), 'w'))

        if app:
            try:
                app.stop()
            except AttributeError:
                app = None

        def callback_report(*args):
            '''  '''

            try:
                txt = six.moves.urllib.parse.quote(
                    report.txt_traceback.text.encode('utf-8')
                )
                url = 'https://github.com/%s/issues/new?body=' % 'jarvis0516/mangoPaint' + txt
                webbrowser.open(url)
            except Exception:
                sys.exit(1)
        report = BugReporter(
            callback_report=callback_report, 
            txt_report=text_error,
            icon_background=os.path.join('Screens', 'resources', 'imgs', 'mango.jpg') # easy 아이콘 디렉토리 찾아 수정할 것
        )

        if app:
            try:
                app.screen.clear_widgets()
                app.screen.add_widget(report)
            except AttributeError:
            	create_error_monitor()
        else:
            create_error_monitor()




if __name__ == ('__main__'):
    main()
