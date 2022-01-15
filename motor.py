# -*- coding = utf-8 -*-
# @Time : 2022/1/15 18:32
# @Author : xzh
# @File : motor.py.py
# @Software: PyCharm
from math import pi


# 三、电动机的选择
# 1、工作机输出功率P_W
def Output_Power(F, V):
    P_W = (F * 1000 * V) / 1000
    print('工作机输出功率：P_W =', P_W, 'KW')
    return P_W


# 2、输送链小链轮转速 n
def Sprocket_Speed(D, V):
    c = pi * D
    n = (c * 60) / (V * 1000)
    print('输送链链轮节圆周长：c =', c)
    print('∴转速 n=(c×60)/(', V, '×1000)r/min=', n, 'r/min')


# 3、传动效率η
def Transmission_Efficiency():
    eta_1 = 0.96
    eta_2 = 0.98
    eta_3 = 0.96
    eta_4 = 0.99
    eta_5 = 0.98
    eta_w = 0.96
    ETA = eta_1 * eta_2 * eta_3 * eta_4 * eta_5 * eta_w
    print('总传动效率η =', ETA, 'KW')
    return ETA


# 4、电动机输入功率P_d
def Input_Power(P_W, ETA):
    P_d = P_W / ETA
    print('P_d=P_w/η =', P_d, 'KW')


# 5、电动机的选择
# print('选YX3系列132S-4型号电动机，主要技术数据如下：'
#       '\n额定功率：5.5 kw'
#       '\n满载转速：1440r/min')


if __name__ == '__main__':
    F = 5
    v = 0.8
    d = 390
    P_W = Output_Power(F, v)
    Sprocket_Speed(d, v)
    eta = Transmission_Efficiency()
    Input_Power(P_W, eta)
    print('选YX3系列132S-4型号电动机，主要技术数据如下：'
          '\n额定功率：5.5 kw'
          '\n满载转速：1440r/min')
