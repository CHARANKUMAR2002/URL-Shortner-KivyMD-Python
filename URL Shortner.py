from kivy.lang import Builder
from kivymd.app import MDApp
from pyshorteners import Shortener
from clipboard import copy
from time import sleep
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('URL Shortner.kv')

    def short(self):
        url = self.root.ids.url.text
        if len(url) == 0:
            self.root.ids.title.text = "URL Not Specified!"
        else:
            url = self.root.ids.url.text
            s = Shortener().clckru.short(url)
            self.root.ids.surl.text = s
            copy(s)
            self.root.ids.title.text = "URL SHORTERNED!"

    
    def clear(self):
        self.root.ids.title.text = "URL SHORTENER"
        self.root.ids.url.text = ""
        self.root.ids.surl.text = ""
        



MainApp().run()