from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase

from math import *
import sympy

class MainScreen(Screen):
    rtinput = ObjectProperty(None)
    lvinput = ObjectProperty(None)
    accoutput = ObjectProperty(None)
    calc_ = ObjectProperty(None)
            
    def rt2acc(self):
        try:
            rt = float(self.rtinput.text)
            lv = float(self.lvinput.text)
        except ValueError:
            self.accoutput.text = 'Err:请不要瞎输一些奇怪的东西!'
        else:
            x = sympy.symbols("x")
            a = sympy.solve([x - 280 * pow(rt, 2) / pow(lv,2)],[x])
            if lv < rt:
                self.accoutput.text = '无解'
            else:
                if a[x] >= 70:
                    a = sympy.solve([(100 - x) / 3 - pow(10,3.5 - (5 * rt / lv))],[x])
                    if a[x] >= 97:
                        a = sympy.solve([100 - x - 3 * pow(10,(35 - 50 * rt / lv) / 8)],[x])
                        if a[x] >= 99.7:
                            a = sympy.solve([100 - x - 3 * pow(10,(39 - 50 * rt / lv) / 4)],[x])
                            if a[x] >= 99.97:
                                a = sympy.solve([(2 * x - 199) * lv - rt],[x])
                try:
                    self.accoutput.text = str(a[x])
                except TypeError:
                    self.accoutput.text = str(a[0][0])

class AnotherScreen(Screen):
    accinput = ObjectProperty(None)
    lvinput = ObjectProperty(None)
    rtoutput = ObjectProperty(None)
    calc_ = ObjectProperty(None)
    
    def acc2rt(self):
        try:
            acc = float(self.accinput.text)
            lv = float(self.lvinput.text)
        except ValueError:
            self.rtoutput.text = 'Err:请输入数字!111'
        else:
            rt = 0
            if acc > 0 and acc < 70:
                rt = sqrt(acc / 70) * 0.5 * lv
            elif acc >= 70 and acc < 97:
                rt = (0.7 - 0.2 * log((100 - acc) / 3, 10)) * lv
            elif acc >= 97 and acc < 99.7:
                rt = (0.7 - 0.16 * log((100 - acc) / 3, 10)) * lv
            elif acc >= 99.7 and acc < 99.97:
                rt = (0.78 - 0.08 * log((100 - acc) / 3, 10)) * lv
            elif acc >= 99.97 and acc <= 100:
                rt = (2 * acc - 199) * lv
            else:
                self.rtoutput.text = 'Err:你家acc有这样的?(半恼'
                return
            self.rtoutput.text = str(rt)

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("screen.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()
