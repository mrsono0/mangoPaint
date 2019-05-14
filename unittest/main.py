import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class MenuScreen(Screen):
    pass
class FirstScreen(Screen):
    first_screen = ObjectProperty()
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_two, 2)
    def screen_switch_two(self, dt):
        self.manager.current = 'second_screen'
class SecondScreen(Screen):
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_three, 4)
    def screen_switch_three(self, dt):
        self.manager.current = 'third_screen'
class ThirdScreen(Screen):
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_four, 6)
    def screen_switch_four(self, dt):
        self.manager.current = 'fourth_screen'
class FourthScreen(Screen):
    def starttimer(self):
        self.timer = Clock.schedule_once(self.screen_switch_one, 8)
    def screen_switch_one(self, dt):
        self.manager.get_screen('first_screen').first_screen.text = "Hi I'm The Fifth Screen"
        self.manager.current = 'first_screen'

class SwitchingScreenApp(App):

    def build(self):
        return Builder.load_file('screen.kv')

if __name__ == '__main__':
    SwitchingScreenApp().run()