# import cProfile

# from app.main_ui import EntryPoint
from kaki.app import App
from kivy.factory import Factory
# from kivy.lang.builder import Builder
from kivymd.app import MDApp

# Builder.load_file("app/kivy_lang.kv")
class HotReload(App,MDApp):
    CLASSES={'EntryPoint':'app.main_ui'}
    KV_FILES=['app/kivy_lang.kv']
    AUTORELOADER_PATHS=[('.',{'recursive':True})]
    def build_app(self):
        self.theme_cls.theme_style='Light'
        self.theme_cls.primary_palette="Cyan"
        self.theme_cls.primary_hue="700"
        self.title='Python Calculator'
        return Factory.EntryPoint()
    
    # def on_start(self):
    #     self.profile=cProfile.Profile()
    #     self.profile.enable()
    # def on_stop(self):
    #     self.profile.disable()
    #     self.profile.dump_stats("hotrealod.profile")
    # def build(self):
    #     self.theme_cls.theme_style='Light'
    #     self.theme_cls.primary_palette="Cyan"
    #     self.theme_cls.primary_hue="700"
    #     self.title='Python Calculator'
    #     return EntryPoint()
    
    def change_theme(self):
        self.theme_cls.theme_style=(
            "Dark" if self.theme_cls.theme_style=='Light' else "Light"
        )
        self.theme_cls.primary_palette=(
            "Cyan" if self.theme_cls.primary_palette=='Indigo' else 'Indigo'
        )

if __name__=='__main__':
    HotReload().run()
