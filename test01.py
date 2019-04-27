import os

from kivy.app import App
from kivy.lang import Builder

from kivymd.theming import ThemeManager
from kivymd.utils.cropimage import crop_image

kv = """
#:import Toolbar kivymd.toolbar.MDToolbar
#:import SmartTileWithLabel kivymd.imagelists.SmartTileWithLabel
#:import SmartTileWithStar kivymd.imagelists.SmartTileWithStar


<MySmartTileWithLabel@SmartTileWithLabel>:
    mipmap: True
    font_style: 'Subhead'


BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: app.title
        elevation: 10
        left_action_items: [['menu', lambda x: x]]
        md_bg_color: app.theme_cls.primary_color

    ScreenManager:
        id: manager

        Screen:
            name: 'one'
            
            MDRaisedButton:
                pos_hint: {'center_x': .5, 'center_y': .55}
                on_release: manager.current = 'two'
                text: 'Open Grid'

        Screen:
            name: 'two'
            on_enter:
                app.crop_image_for_tile(tile_1, tile_1.size, 'Screens/resources/imgs/mango.jpg')
                app.crop_image_for_tile(tile_2, tile_2.size, 'Screens/resources/imgs/mango.jpg')
                app.crop_image_for_tile(tile_3, tile_3.size, 'Screens/resources/imgs/mango.jpg')
                app.crop_image_for_tile(tile_4, tile_4.size, 'Screens/resources/imgs/mango.jpg')
                app.crop_image_for_tile(tile_5, tile_5.size, 'Screens/resources/imgs/mango.jpg')
                app.crop_image_for_tile(tile_6, tile_6.size, 'Screens/resources/imgs/mango.jpg')
                app.crop_image_for_tile(tile_7, tile_7.size, 'Screens/resources/imgs/mango.jpg')

            ScrollView:
                do_scroll_x: False

                GridLayout:
                    cols: 2
                    row_default_height:
                        (self.width - self.cols*self.spacing[0])/self.cols
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
                        text:
                            "Beautiful\\n[size=12]beautiful-931152_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_4
                        text:
                            "Robin\\n[size=12]robin-944887_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_5
                        text:
                            "Kitten\\n[size=12]kitten-1049129_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_6
                        text:
                            "Light-Bulb\\n[size=12]light-bulb-1042480_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_7
                        text:
                            "Tangerines\\n[size=12]tangerines-1111529_1280.jpg[/size]"
"""


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = 'Example Smart Tile'
    md_app_bar = None

    def build(self):
        root = Builder.load_string(kv)
        return root

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image


MyApp().run()