from math import *
import os
import sympy

x = sympy.symbols("x")

def rt2acc():
    rt = float(input('输入rt(例:11.45):'))
    for i in range(1,17):
        a = sympy.solve([x - 280 * pow(rt, 2) / pow(i,2)],[x])
        if i < rt:
            print(str(i) + ':无解')
            continue
        else:
            if a[x] >= 70:
                a = sympy.solve([(100 - x) / 3 - pow(10,3.5 - (5 * rt / i))],[x])
                if a[x] >= 97:
                    a = sympy.solve([100 - x - 3 * pow(10,(35 - 50 * rt / i) / 8)],[x])
                    if a[x] >= 99.7:
                        a = sympy.solve([100 - x - 3 * pow(10,(39 - 50 * rt / i) / 4)],[x])
                        if a[x] >= 99.97:
                            a = sympy.solve([(2 * x - 199) * i - rt],[x])
        try:
            print(str(i) + ':' + str(a[x]))
        except TypeError:
            print(str(i) + ':' + str(a[0][0]))
        
def acc2rt():
    try:
        acc = float(input('输入acc(例:99.17):'))
        lv = int(input('输入谱面难度(15+ == 16)(例:15):'))
    except ValueError:
        print('Err:请输入数字!111')
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
        print('Err:输入值小于等于0或大于100.')
    print('rt = ' + str(rt))
    
print('欢迎来到Cytoid单曲rt计算器,请选择计算模式.(by 千里扯淡)(计算精度:15位有效数字)(不提供整体rt计算功能(要是Tix给我api我就做(((')
try:
    mode = int(input('(0:rt=>acc, 1:acc=>rt):'))
except ValueError:
    print('Err:你别瞎输其它东西啊喂!1!11  踢了！')
else:
    if mode == 0:
        rt2acc()
    elif mode == 1:
        acc2rt()
    else:
        print('Err:你别瞎输其它东西啊喂!1!11  踢了！')
    
os.system('pause')