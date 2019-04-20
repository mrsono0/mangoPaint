

from kivy.uix.gridlayout import GridLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty, ListProperty

from Libs.uix.custombutton import CustomButton


class NavigationMenu(GridLayout):
    events_callback = ObjectProperty(None)
    '''Функция обработки событий.
    :attr: `events_callback` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to None.
    '''

    background_color = ListProperty([1.0, 1.0, 1.0, 1.0])
    '''Цвет фона меню.
    :attr: `background_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to [1.0, 1.0, 1.0, 1.0].
    '''

    items = ListProperty([])
    '''Список опций.
    :attr: `items` is a :class:`~kivy.properties.ListProperty`
    and defaults to [].
    '''

    def __init__(self, **kwargs):
        super(NavigationMenu, self).__init__(cols=1, spacing=1, **kwargs)

        for list_item_menu in self.items:
            self.add_widget(
                CustomButton(
                    text=list_item_menu[0], icon=list_item_menu[1],
                    icon_map='Data/Images/none.png',
                    icon_people='Data/Images/none.png',
                    events_callback=self.events_callback,
                )
            )

        with self.canvas.before:
            Color(rgba=self.background_color)
            canvas_navigation = \
                Rectangle(pos=(0, 0), size=(self.width, self.height))

            def on_navigation_pos(instance, value):
                canvas_navigation.pos = value

            def on_navigation_size(instance, value):
                canvas_navigation.size = value

            self.bind(size=on_navigation_size, pos=on_navigation_pos)