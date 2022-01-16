# -*- coding = utf-8 -*-
# @Time : 2022/1/15 18:14
# @Author : xzh
# @File : main.py
# @Software: PyCharm
import math
import numpy as np
from math import cos, pi, sqrt

from prettytable import PrettyTable

import motor as mt
import gear_ratio as gr
import transmission_parameters as tp
import gear_drive as gd
# 已知条件
F = 5
v = 0.8
d = 390
# 计算工作寿命
print('注：1.链板式输送机工作时，运转方向不变，工作载荷稳定。'
      '\n   2.工作寿命10年，每年300个工作日，每日工作12小时。')
t = 10 * 300 * 12
print('工作寿命：t=10×300×12h=3.6×10^4 h')
# 三、电动机的选择
# 1、工作机输出功率P_W
P_W = mt.Output_Power(F, v)
# 2、输送链小链轮转速 n
n = mt.Sprocket_Speed(d, v)
# 3、传动效率η
eta = mt.Transmission_Efficiency()
# 4、电动机输入功率P_d
P_d = mt.Input_Power(P_W, eta)
# 5、电动机的选择
print('选YX3系列132S-4型号电动机，主要技术数据如下：'
      '\n额定功率：5.5 kw'
      '\n满载转速：1440r/min')

# 四、传动装置的总传动比及其分配
# 1、系统总传动比i
i = gr.Total_Gear_Ratio(n)
# 2、分配传动比(圆锥齿轮传动i_1/圆柱齿轮传动i_2/链传动i_3)
i_1 = 2
i_2 = 6
i_3 = gr.Transmission_Ratio_Assignment(i, i_1, i_2)

# 五、计算传动装置的运动和动力参数
# 1、各轴转速n（r/min）
n_1, n_2, n_3 = tp.Shaft_Speed(i_1, i_2)
# 2、各轴输入功率P（kW）
P_1, P_2, P_3 = tp.Input_Power(P_d)
# 3、各轴输入转矩T（N•ｍ）
T_1, T_2, T_3 = tp.Input_Torque(P_1, P_2, P_3, n_1, n_2, n_3)

# 六、齿轮传动的设计计算
print('#########六、齿轮传动的设计计算#########')
# 一、高速级锥齿轮传动：
# 1、选定齿轮类型、精度等级、材料及齿数(略)
# 2、按齿面接触强度设计
print('######(一)高速级锥齿轮传动：########'
      '\n#####1)确定公式的各计算数值#####')
bevel_gear_D = gd.BevelGear.DesignAccordingToToothSurfaceContactStrength(i_1=2, T_1=30.595749463944532, n_1=1440)
# 2)调整小齿轮分度圆直径
print('#####2)调整小齿轮分度圆直径#####')
R = bevel_gear_D.Tooth_Contact_Strength_Design(n_1=1440)
# 3）计算载荷系数
print('########3）计算载荷系数########')
m_1, d_1 = bevel_gear_D.Load_Factor()
# 3、校核齿根弯曲强度
print('##########3、校核齿根弯曲强度########')
# 1）确定公式中各计算数值
print('#####1）确定公式中各计算数值#####')
bevel_gear_C = gd.BevelGear.CheckToothRootBendingStrength(Z_1=16, Z_2=48, mu=2)
# 2）代入数值计算
m_2 = bevel_gear_C.Substitution_Calculation_1(T_1=30.595749463944532, phi_R=1 / 3, d_1=32.0042098044378, m=2)
# ３）代入数值计算
m = max(m_1, m_2)
d_m1, d_m2, d_2, B_1, B_2 = bevel_gear_C.Substitution_Calculation_2(m=2, phi_R=1 / 3)
# 4.计算各主要几何尺寸列表备用
h_a = 1 * m
h_f = 1.2 * m
d_a1 = d_1 + 2 * h_a * cos(bevel_gear_C.delta_1)
d_a2 = d_2 + 2 * h_a * cos(bevel_gear_C.delta_2)
d_f1 = d_1 - 2 * h_f * cos(bevel_gear_C.delta_1)
d_f2 = d_2 - 2 * h_f * cos(bevel_gear_C.delta_2)
theta_f = math.atan(h_f / R) * 180 / pi
delta_a1 = bevel_gear_C.delta_1 + theta_f
delta_a2 = bevel_gear_C.delta_2 + theta_f
delta_f1 = bevel_gear_C.delta_1 - theta_f
delta_f2 = bevel_gear_C.delta_2 - theta_f
c = 0.2 * m
s = pi * m / 2
Z_v1 = bevel_gear_C.Z_1 / cos(bevel_gear_C.delta_1 * pi / 180)
Z_v2 = bevel_gear_C.Z_2 / cos(bevel_gear_C.delta_2 * pi / 180)
table = PrettyTable(['名称', '代号', '小锥齿轮', '大锥齿轮'])
table.add_row(['分锥角', 'δ', bevel_gear_C.delta_1, bevel_gear_C.delta_2])
table.add_row(['齿顶高', 'h_a', h_a, h_a])
table.add_row(['齿根高', 'h_f', 1.2 * m, 1.2 * m])
table.add_row(['分度圆直径', 'd', d_1, d_2])
table.add_row(['平均分度圆直径', 'd_m', d_m1, d_m2])
table.add_row(['齿顶圆直径', 'd_a', d_a1, d_a2])
table.add_row(['齿根圆直径', 'd_f', d_f1, d_f2])
table.add_row(['锥距', 'R', R, R])
table.add_row(['齿根角', 'θ_f', theta_f, theta_f])
table.add_row(['顶锥角', 'δ_a', delta_a1, delta_a2])
table.add_row(['根锥角', 'δ_f', delta_f1, delta_f2])
table.add_row(['顶隙', 'c', c, c])
table.add_row(['分度圆齿厚', 's', s, s])
table.add_row(['当量齿数', 'Z_v', Z_v1, Z_v2])
table.add_row(['齿宽', 'B', B_1, B_2])
print(table)
# 二、低速级斜齿圆柱齿轮传动
# 1、选定齿轮类型、旋向、精度等级、材料及齿数
