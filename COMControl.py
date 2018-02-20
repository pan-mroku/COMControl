#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

#https://kivy.org/docs/guide/lang.html
class COMControl(FloatLayout):
    label_wid = ObjectProperty()
    info = StringProperty()
    
    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'

class MyApp(App):
    def build(self):
        #return Label(text='Hello world')
        #return COMControl(info='Hello')
        self.root = Builder.load_file('window.kv')
        return self.root

if __name__ == '__main__':
    MyApp().run()

#https://stackoverflow.com/questions/44491912/kivy-python-right-click
