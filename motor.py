# -*- coding = utf-8 -*-
# @Time : 2022/1/15 18:32
# @Author : xzh
# @File : motor.py.py
# @Software: PyCharm
from math import pi
from rich import print


# 三、电动机的选择
# 1、工作机输出功率P_W
def Output_Power(F, v):
    P_W = (F * 1000 * v) / 1000
    print('工作机输出功率：P_W =', P_W, 'KW')
    return P_W


# 2、输送链小链轮转速 n
def Sprocket_Speed(d, v):
    c = pi * d
    n = (v * 1000) / c * 60
    print('输送链链轮节圆周长：c =', c)
    print('∴转速 n=(', v, '×1000) / c × 60r/min=', n, 'r/min')
    return n


# 3、传动效率η
def Transmission_Efficiency():
    eta_1 = 0.96  # ⑴锥齿轮传动：8级精度的一般齿轮传动(稀油润滑)
    eta_2 = 0.98  # ⑵斜齿轮传动：7级精度的一般齿轮传动(稀油润滑)
    eta_3 = 0.96  # ⑶链传动：滚子链
    eta_4 = 0.99  # ⑷联轴器：初选弹性联轴器
    eta_5 = 0.98  # ⑸滚动轴承：滚子轴承（稀油润滑）
    # eta_w = 0.96
    eta = eta_1 * eta_2 * eta_3 * eta_4 * eta_5**3
    print('总传动效率η =', eta, 'KW')
    return eta


# 4、电动机输入功率P_d
def Input_Power(P_W, eta):
    P_d = P_W / eta
    print('P_d=P_w/η =', P_d, 'KW')
    return P_d


# 5、电动机的选择
# print('选YX3系列132S-4型号电动机，主要技术数据如下：'
#       '\n额定功率：5.5 kw'
#       '\n满载转速：1440r/min')


if __name__ == '__main__':
    F = 5
    v = 0.8
    d = 390
    # 1、工作机输出功率P_W
    P_W = Output_Power(F, v)
    # 2、输送链小链轮转速 n
    Sprocket_Speed(d, v)
    # 3、传动效率η
    eta = Transmission_Efficiency()
    # 4、电动机输入功率P_d
    Input_Power(P_W, eta)
    # 5、电动机的选择
    print('选YX3系列132S-4型号电动机，主要技术数据如下：'
          '\n额定功率：5.5 kw'
          '\n满载转速：1440r/min')
