import math
import re
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFillRoundFlatIconButton, MDIconButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen

# constants
ICON_DICT={
    "alpha-c":'c',
    "division":'\u00F7',
    "close":'x',
    'chevron-left':'cancel',
    'numeric-7':7,
    'numeric-8':8,
    'numeric-9':9,
    'minus':"-",
    'numeric-4':4,
    'numeric-5':5,
    'numeric-6':6,
    'plus':'+',
    'numeric-1':1,
    'numeric-2':2,
    'numeric-3':3,
    'percent':"%",
    'numeric-0':0,
    "circle-small":".",
    "exclamation": "!",
}
class EntryPoint(MDScreen):
    grid_lt=ObjectProperty()
    text_label=ObjectProperty()
    text_field=ObjectProperty()
    def __init__(self, *args, **kwargs):
        super(EntryPoint,self).__init__(*args, **kwargs)
        for key in ICON_DICT.keys():
            btn_nest=BtnNest()
            btn=Btn(self.text_field,self.text_label,icon=key)
            btn_nest.add_widget(btn)
            self.grid_lt.add_widget(btn_nest)
        eq_nest=BtnNest()
        eq_btn=EqBtn(self.text_field,self.text_label,icon='equal',text='Equals')
        eq_nest.add_widget(eq_btn)
        self.grid_lt.add_widget(eq_nest)

class BtnNest(MDRelativeLayout):
    pass
class Btn(MDIconButton):
    icon_size=dp(45)
    pos_hint={'center_x':.5,'center_y':.5}
    def __init__(self,text_field,text_label, *args, **kwargs):
        super(Btn,self).__init__(*args, **kwargs)
        self.text_field=text_field
        self.text_label=text_label
    def on_release(self):
        cursor=self.text_field.cursor_index()
        txt=str(ICON_DICT[self.icon])
        if self.icon=="chevron-left":
            if not self.text_field.text:
                return
            elif cursor==len(self.text_field.text):
                self.text_field.text=self.text_field.text[:-1]
            else:
                lst=list(self.text_field.text)
                if cursor>0:
                    lst.pop(cursor-1)
                elif cursor==0:
                    lst.pop(cursor)
                self.text_field.text="".join(lst)
                self.text_field.cursor=(cursor-1,0)
        elif self.icon=='alpha-c':
            self.text_field.text=""
            self.text_label.text=""
        else:
            if not self.text_field.text:
                self.text_field.text+=txt
            else:
                lst=list(self.text_field.text)
                lst.insert(cursor,txt)
                self.text_field.text="".join(lst)
                self.text_field.cursor=(cursor+1,0)
        return super().on_release()

class EqBtn(MDFillRoundFlatIconButton):
    pos_hint={'center_x':.5,'center_y':.5}
    def __init__(self,text_field,text_label, *args, **kwargs):
        super(EqBtn,self).__init__(*args, **kwargs)
        self.text_field=text_field
        self.text_label=text_label
    def on_release(self):
        txt_copy=self.text_field.text.strip()
        result=""
        if not self.text_field.text:
            self.text_label.text=result
            self.text_field.cursor=(0,0)
            return
        if 'x' in txt_copy:
            txt_copy=txt_copy.replace('x','*')
        if '\u00F7' in txt_copy:
            txt_copy=txt_copy.replace(chr(247),'/')
        if '!' in txt_copy:
            splt=re.split(r"[-*/+%]",string=txt_copy)
            print(splt)
            replace=self.replace_f(splt)
            print(replace)
            for i in range(len(replace)):
                txt_copy=re.sub(f"{replace[i]}",string=txt_copy,repl="math.factorial({})".format(replace[i].split("!")[0]))
        try:
            result=str(eval(txt_copy))
        except Exception as e:
            result=str(e.with_traceback).split()[4] 
        self.text_label.text=result
    
    @staticmethod
    def replace_f(lst:list)->str:
        result=[]
        for i in lst:
            if "!" in i:
                result.append(i)
        return result
