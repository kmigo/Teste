#: -*- coding: utf-8 -*-

__autor__ = 'Patrick Soares'


#import libs
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.core.window import Window

from kivymd.theming import ThemeManager
Window.softinput_mode='below_target'

#libs externas na pasta screens
from screens import Screens


class HortifrutiHome(BoxLayout,Screens):
	pass


class Home(Screen):
	pass


class Fundo(BoxLayout):
	field_name = StringProperty('')


class HortifrutiApp(App):
	theme_cls=ThemeManager()
	page_before=['home','home']
	def build(self):
		aplicativo = HortifrutiHome()
		return aplicativo


if __name__ == '__main__':
	HortifrutiApp().run()
