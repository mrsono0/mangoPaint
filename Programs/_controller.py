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

# ============================================================
#  kv strings
# ============================================================
# 이미지 갤러리 
grid = '''
#:import SmartTileWithStar kivymd.imagelists.SmartTileWithStar
#:import SmartTileWithLabel kivymd.imagelists.SmartTileWithLabel
<Grid@Screen>
    name: 'grid'
    on_enter:
        app.crop_image_for_tile(tile_1, tile_1.size, 'assets/beautiful-931152_1280_tile_crop.png')
        app.crop_image_for_tile(tile_2, tile_2.size, 'assets/african-lion-951778_1280_tile_crop.png')
        app.crop_image_for_tile(tile_3, tile_3.size, 'assets/guitar-1139397_1280_tile_crop.png')
        app.crop_image_for_tile(tile_4, tile_4.size, 'assets/robin-944887_1280_tile_crop.png')
        app.crop_image_for_tile(tile_5, tile_5.size, 'assets/kitten-1049129_1280_tile_crop.png')
        app.crop_image_for_tile(tile_6, tile_6.size, 'assets/light-bulb-1042480_1280_tile_crop.png')
        app.crop_image_for_tile(tile_7, tile_7.size, 'assets/tangerines-1111529_1280_tile_crop.png')
    ScrollView:
        do_scroll_x: False
        GridLayout:
            cols: 2
            row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
            row_force_default: True
            size_hint_y: None
            height: self.minimum_height
            padding: dp(4), dp(4)
            spacing: dp(4)
            SmartTileWithStar:
                id: tile_2
                mipmap: True
                stars: 3
            SmartTileWithStar:
                id: tile_3
                mipmap: True
                stars: 3
            SmartTileWithLabel:
                id: tile_1
                mipmap: True
                text: "Beautiful\\n[size=12]beautiful-931152_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_4
                mipmap: True
                text: "Robin\\n[size=12]robin-944887_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_5
                mipmap: True
                text: "Kitten\\n[size=12]kitten-1049129_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_6
                mipmap: True
                text: "Light-Bulb\\n[size=12]light-bulb-1042480_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_7
                mipmap: True
                text: "Tangerines\\n[size=12]tangerines-1111529_1280.png[/size]"
                font_style: 'Subtitle1'
'''

# Buttom Navigation
bottom_navigation = '''
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDLabel kivymd.label.MDLabel
<BottomNavigation@Screen>
    name: 'bottom navigation'
    MDBottomNavigation:
        id: bottom_navigation_demo
        MDBottomNavigationItem:
            name: 'banking'
            text: "Bank"
            icon: 'bank'
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                padding: dp(48)
                spacing: dp(10)
                MDTextField:
                    hint_text: "You can put any widgets here"
                    helper_text: "Hello :)"
                    helper_text_mode: "on_focus"
        MDBottomNavigationItem:
            name: 'bottom_navigation_desktop_1'
            text: "Hello"
            icon: 'alert'
            id: bottom_navigation_desktop_1
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                padding: dp(48)
                spacing: dp(10)
                MDTextField:
                    hint_text: "Hello again"
            MDBottomNavigationItem:
                name: 'bottom_navigation_desktop_2'
                text: "Food"
                icon: 'food'
                id: bottom_navigation_desktop_2
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "Cheese!"
                halign: 'center'
'''

# tabs
tabs = '''
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDLabel kivymd.label.MDLabel
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
<Tabs@Screen>
    name: 'tabs'
    MDTabbedPanel:
        id: tab_panel
        tab_display_mode: 'text'
        tab_width_mode: 'stacked'
        MDTab:
            name: 'music'
            text: "Music"
            icon: "playlist-play"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "Here is my music list :)"
                halign: 'center'
        MDTab:
            name: 'movies'
            text: 'Movies'
            icon: "movie"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "Show movies here :)"
                halign: 'center'
        MDTab:
            name: 'python'
            text: 'Python'
            icon: "language-python"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "I love Python language"
                halign: 'center'
        MDTab:
            name: 'cpp'
            text: 'C++'
            icon: "language-cpp"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "I love C++ language"
                halign: 'center'
        MDTab:
            name: 'php'
            text: 'PHP'
            icon: "language-php"
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "I love PHP language"
                halign: 'center'
    BoxLayout:
        size_hint_y: None
        height: dp(72)
        padding: dp(12)
        MDLabel:
            font_style: 'Body1'
            theme_text_color: 'Primary'
            text: "Use icons"
            size_hint_x:None
            width: dp(64)
        MDCheckbox:
            on_state:
                tab_panel.tab_display_mode = 'icons'\
                if tab_panel.tab_display_mode=='text' else 'text'
        MDLabel:
            font_style: 'Body1'
            theme_text_color: 'Primary'
            text: "Use fixed"
            size_hint_x:None
            width: dp(64)
        MDCheckbox:
            on_state:
                tab_panel.tab_width_mode = 'fixed'\
                if tab_panel.tab_width_mode =='stacked' else 'stacked'
        Widget:
'''

# toolbar
toolbars = '''
#:import MDToolbar kivymd.toolbar.MDToolbar
<Toolbars@Screen>
    name: 'toolbars'
    MDToolbar:
        title: "Simple toolbar"
        pos_hint: {'center_x': .5, 'center_y': .75}
        md_bg_color: get_color_from_hex(colors['Teal']['500'])
        background_palette: 'Teal'
        background_hue: '500'
    MDToolbar:
        title: "MDToolbar with right buttons"
        pos_hint: {'center_x': .5, 'center_y': .5}
        md_bg_color: get_color_from_hex(colors['Amber']['700'])
        background_palette: 'Amber'
        background_hue: '700'
        right_action_items: [['content-copy', lambda x: None]]
    MDToolbar:
        title: "MDToolbar with left and right buttons"
        pos_hint: {'center_x': .5, 'center_y': .25}
        md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
        background_palette: 'DeepPurple'
        background_hue: 'A400'
        left_action_items: [['arrow-left', lambda x: None]]
        right_action_items: [['lock', lambda x: None],\
            ['camera', lambda x: None],\
            ['play', lambda x: None]]
'''

# Dialog
dialogs = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
<Dialogs@Screen>
    name: 'dialogs'
    MDRaisedButton:
        text: "Open lengthy dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .8}
        opposite_colors: True
        on_release: app.show_example_long_dialog()
    MDRaisedButton:
        text: "Open input dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .6}
        opposite_colors: True
        on_release: app.show_example_input_dialog()
    MDRaisedButton:
        text: "Open Alert Dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .4}
        opposite_colors: True
        on_release: app.show_example_alert_dialog()
    MDRaisedButton:
        text: "Open Ok Cancel Dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .2}
        opposite_colors: True
        on_release: app.show_example_ok_cancel_dialog()
'''

# 
file_manager = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
<FileManager@Screen>
    name: 'file manager'
    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open files manager'
        opposite_colors: True
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.file_manager_open()
'''

# 
download_file = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import Clock kivy.clock.Clock
<DownloadFile@Screen>
    name: 'download file'
    FloatLayout:
        id: box_flt
        MDRaisedButton:
            text: "Download file"
            size_hint: None, None
            size: 3 * dp(48), dp(48)
            pos_hint: {'center_x': .5, 'center_y': .5}
            opposite_colors: True
            on_release:
                Clock.schedule_once(app.show_example_download_file, .1)
'''

# 
progress_bar = '''
#:import MDSlider kivymd.slider.MDSlider
#:import MDProgressBar kivymd.progressbar.MDProgressBar
<ProgressBars@Screen>
    name: 'progress bar'
    BoxLayout:
        orientation:'vertical'
        padding: '8dp'
        MDSlider:
            id: progress_slider
            min: 0
            max: 100
            value: 40
        MDProgressBar:
            value: progress_slider.value
        MDProgressBar:
            reversed: True
            value: progress_slider.value
        BoxLayout:
            MDProgressBar:
                orientation: "vertical"
                reversed: True
                value: progress_slider.value
            MDProgressBar:
                orientation: "vertical"
                value: progress_slider.value
'''

# 
progress = '''
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSpinner kivymd.spinner.MDSpinner
<Progress@Screen>
    name: 'progress'
    MDCheckbox:
        id: chkbox
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .4}
        active: True
    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True if chkbox.active else False
'''

# manager swiffer : myStudio 에서 작업한 이미지들 보여주는 방식 
manager_swiper = '''
#:import images_path kivymd.images_path
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDLabel kivymd.label.MDLabel
#:import MDSwiperManager kivymd.managerswiper.MDSwiperManager
<MyCard>
    orientation: 'vertical'
    size_hint_y: None
    height: dp(300)
    pos_hint: {'top': 1}
    Image:
        source:
            '{}/assets/guitar-1139397_1280_swiper_crop.png'.format(app.directory)
        size_hint: None, None
        size: root.width, dp(250)
        pos_hint: {'top': 1}
    MDLabel:
        theme_text_color: 'Custom'
        bold: True
        text_color: app.theme_cls.primary_color
        text: root.text
        size_hint_y: None
        height: dp(60)
        halign: 'center'
<MySwiperManager@Screen>
    name: 'manager swiper'
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 0, 0, 0, .2
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            id: box
            padding: dp(10)
            orientation: 'vertical'
            MDSwiperManager:
                id: swiper_manager
                Screen:
                    name: 'screen one'
                    MyCard:
                        text: 'Swipe to switch to screen one'.upper()
                Screen:
                    name: 'screen two'
                    MyCard:
                        text: 'Swipe to switch to screen two'.upper()
                Screen:
                    name: 'screen three'
                    MyCard:
                        text: 'Swipe to switch to screen three'.upper()
                Screen:
                    name: 'screen four'
                    MyCard:
                        text: 'Swipe to switch to screen four'.upper()
                Screen:
                    name: 'screen five'
                    MyCard:
                        text: 'Swipe to switch to screen five'.upper()
'''

md_icon_item = '''
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
<MDIconItem@OneLineIconListItem>
    icon: 'android'
    IconLeftSampleWidget:
        icon: root.icon
'''

md_icons = '''
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import images_path kivymd.images_path
#:import MDTextFieldRect kivymd.textfields.MDTextField
#:import MDIconButton kivymd.button.MDIconButton
<MDIconItemForMdIconsList@OneLineIconListItem>:
    icon: 'android'
    on_release: root.callback(root.icon)
    IconLeftSampleWidget:
        icon: root.icon
<MDIcons@Screen>
    name: 'md icons'
    on_enter: app.set_list_md_icons()
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            MDIconButton:
                icon: 'magnify'
            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: app.set_list_md_icons(self.text, True)
        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'
            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''

# ============================================================





class Controller(object):

    def show_gallery(self):
        print('show_gallery')

    def show_purchase(self):
        print('show_purchase')

    def show_mystudio(self):
        print('show_mystudio')