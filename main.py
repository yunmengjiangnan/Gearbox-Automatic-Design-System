# -*- coding = utf-8 -*-
# @Time : 2022/1/15 18:14
# @Author : xzh
# @File : main.py
# @Software: PyCharm
import math
# import numpy as np
from math import cos, pi, sqrt
from rich import print
from rich.console import Console
from rich.table import Column, Table
# from prettytable import PrettyTable

import motor as mt
import gear_ratio as gr
import transmission_parameters as tp
import gear_drive as gd

# 已知条件
F = 5
v = 0.8
d = 390
# 实例化一个输出控制端
console = Console()
console.print("一、设计任务：", style="red")
print('设计一个用于带式运输机上的圆锥圆柱齿轮减速器。已知条件如下：')
table_1 = Table(show_header=True, header_style='bold magenta')
table_1.add_column('组数')
table_1.add_column('输送链的牵引力F（KG）')
table_1.add_column('输送链的速度v(m/s)')
table_1.add_column('输送链链轮节圆直径d(mm)')
table_1.add_row('第六组', '5', '0.8', '390')
print(table_1)
# 计算工作寿命
print('注：1.链板式输送机工作时，运转方向不变，工作载荷稳定。'
      '\n    2.工作寿命10年，每年300个工作日，每日工作12小时。')
t = 10 * 300 * 12
print('工作寿命：t=10×300×12h=3.6×10^4 h')
console.print("二、传动方案的拟定及说明", style="red")
print('如上图课程设计任务书上布置简图所示，传动方案采用圆锥圆柱齿轮减速箱：'
      '\n圆锥齿轮置于高速极，以免使圆锥齿轮尺寸过大加工困难；'
      '\n第二级采用斜齿轮减速只是为了增加设计难度；'
      '\n链传动的制造与安装精度要求较低适合远距离传动，但只适用在平行轴间低速重载传动，故用在低速级。')
# 三、电动机的选择
console.print("三、电动机的选择", style="red")
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
console.print("四、传动装置的总传动比及其分配", style="red")
# 1、系统总传动比i
i = gr.Total_Gear_Ratio(n)
# 2、分配传动比(圆锥齿轮传动i_1/圆柱齿轮传动i_2/链传动i_3)
i_1 = 2
i_2 = 6
i_3 = gr.Transmission_Ratio_Assignment(i, i_1, i_2)

# 五、计算传动装置的运动和动力参数
console.print("五、计算传动装置的运动和动力参数", style="red")
# 1、各轴转速n（r/min）
console.print("1、各轴转速n（r/min）", style='#FF6100')
n_1, n_2, n_3 = tp.Shaft_Speed(i_1, i_2)
# 2、各轴输入功率P（kW）
console.print("2、各轴输入功率P（kW）", style='#FF6100')
P_1, P_2, P_3 = tp.Input_Power(P_d)
# 3、各轴输入转矩T（N•ｍ）
console.print("3、各轴输入转矩T（N•ｍ）", style='#FF6100')
T_1, T_2, T_3 = tp.Input_Torque(P_1, P_2, P_3, n_1, n_2, n_3)

console.print("六、齿轮传动的设计计算", style="red")
console.print("(一)高速级锥齿轮传动：", style='#FF6100')
console.print("1、选定齿轮类型、精度等级、材料及齿数（略）", style="yellow")
console.print("2、按齿面接触强度设计", style="yellow")
console.print("1)确定公式的各计算数值", style="green")
bevel_gear_D = gd.BevelGear.DesignAccordingToToothSurfaceContactStrength(i_1=2, T_1=30.595749463944532, n_1=1440)
console.print("2)调整小齿轮分度圆直径", style="green")
R = bevel_gear_D.Tooth_Contact_Strength_Design(n_1=1440)
console.print("3）计算载荷系数", style="green")
m_1, d_1 = bevel_gear_D.Load_Factor()

console.print("3、校核齿根弯曲强度", style='yellow')
console.print("1）确定公式的各计算数值", style="green")
bevel_gear_C = gd.BevelGear.CheckToothRootBendingStrength(Z_1=16, Z_2=48, mu=2)
console.print("2）代入数值计算", style="green")
m_2 = bevel_gear_C.Substitution_Calculation_1(T_1=30.595749463944532, phi_R=1 / 3, d_1=32.0042098044378, m=2)
console.print("3）代入数值计算", style="green")
m = max(m_1, m_2)
d_m1, d_m2, d_2, B_1, B_2 = bevel_gear_C.Substitution_Calculation_2(m=2, phi_R=1 / 3)
console.print("4.计算各主要几何尺寸列表备用", style='yellow')

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
table = Table(show_header=True, header_style='bold magenta')
table.add_column('名称')
table.add_column('代号')
table.add_column('小锥齿轮')
table.add_column('大锥齿轮')
table.add_row('分锥角', 'δ', str(bevel_gear_C.delta_2), str(bevel_gear_C.delta_2))
table.add_row('齿顶高', 'h_a', str(h_a), str(h_a))
table.add_row('齿根高', 'h_f', str(1.2 * m), str(1.2 * m))
table.add_row('分度圆直径', 'd', str(d_1), str(d_2))
table.add_row('平均分度圆直径', 'd_m', str(d_m1), str(d_m2))
table.add_row('齿顶圆直径', 'd_a', str(d_a1), str(d_a2))
table.add_row('齿根圆直径', 'd_f', str(d_f1), str(d_f2))
table.add_row('锥距', 'R', str(R), str(R))
table.add_row('齿根角', 'θ_f', str(theta_f), str(theta_f))
table.add_row('顶锥角', 'δ_a', str(delta_a1), str(delta_a2))
table.add_row('根锥角', 'δ_f', str(delta_f1), str(delta_f2))
table.add_row('顶隙', 'c', str(c), str(c))
table.add_row('分度圆齿厚', 's', str(s), str(s))
table.add_row('当量齿数', 'Z_v', str(Z_v1), str(Z_v2))
table.add_row('齿宽', 'B', str(B_1), str(B_2))
print(table)

console.print("（二）低速级圆柱斜齿轮传动", style='#FF6100')
console.print("1、选定齿轮类型、旋向、精度等级、材料及齿数（略）", style="yellow")
console.print("2、按齿面接触强度设计", style="yellow")
helical_spur_gear_D = gd.HelicalSpurGear.DesignAccordingToToothSurfaceContactStrength(i_2=6, T_2=57.56896219135802,
                                                                                      n_2=720)
console.print("3、按齿根弯曲强度设计", style="yellow")
helical_spur_gear_C = gd.HelicalSpurGear.CheckToothRootBendingStrength(i_2=6, T_2=57569, d_1=32.0042098044378)
console.print("4、计算几何尺寸", style="yellow")
console.print("1）计算中心距", style="green")
a_float = ((helical_spur_gear_C.Z_1 + helical_spur_gear_C.Z_2) * helical_spur_gear_C.m_n) / (
        2 * cos(helical_spur_gear_C.beta))
a = round(a_float)
print('a =', a_float, 'mm'
                      '将中心距圆整为', a, 'mm')
console.print("2）按圆整后的中心距修正螺旋角β", style="green")
beta = math.acos(((helical_spur_gear_C.Z_1 + helical_spur_gear_C.Z_2) * helical_spur_gear_C.m_n) / (2 * a))
rate = (beta - helical_spur_gear_C.beta) / helical_spur_gear_C.beta
if rate < 0.05:
    print('β =', beta,
          '且β与原定义β差距在5%以内，螺旋角值β改变不多，故参数ε_α、K_β、Z_H等不必修正')
console.print("3）计算大、小齿轮分度圆直径", style="green")
d_1 = (helical_spur_gear_C.m_n * helical_spur_gear_C.Z_1) / cos(beta)
d_2 = (helical_spur_gear_C.m_n * helical_spur_gear_C.Z_2) / cos(beta)
console.print("4）计算齿轮宽度", style="green")
float_b = helical_spur_gear_D.phi_d * d_1
b = round(float_b)
print('b=φ_d * d_1 =', float_b,
      '\n圆整后，取B_2 =', b, '，B_1 =', round(b * 1.1))
console.print("5、计算所得结果汇总如下表备用。", style="yellow")
m_n = helical_spur_gear_C.m_n
m_t = helical_spur_gear_C.m_n / cos(beta)
a_n = 20
h_a = 1 * m_n
h_f = 1.25 * m_n
d_a1 = d_1 + 2 * h_a * cos(helical_spur_gear_C.beta)
d_a2 = d_2 + 2 * h_a * cos(helical_spur_gear_C.beta)
d_f1 = d_1 - 2 * h_f * cos(helical_spur_gear_C.beta)
d_f2 = d_2 - 2 * h_f * cos(helical_spur_gear_C.beta)
B_2 = b
B_1 = round(b * 1.1)
table_2 = Table(show_header=True, header_style='bold magenta')
table_2.add_column('名称')
table_2.add_column('符号')
table_2.add_column('小齿轮')
table_2.add_column('大齿轮')
table_2.add_row('螺旋角', 'β', str(beta), str(beta))
table_2.add_row('法面模数', 'm_n', str(m_n), str(m_n))
table_2.add_row('端面模数', 'm_t', str(m_t), str(m_t))
table_2.add_row('法面压力角', 'α_n', str(a_n), str(a_n))
table_2.add_row('分度圆直径', 'd', str(d_1), str(d_2))
table_2.add_row('齿顶高', 'h_a', str(h_a), str(h_a))
table_2.add_row('齿根高', 'h_f', str(h_f), str(h_f))
table_2.add_row('齿顶圆直径', 'd_a', str(d_a1), str(d_a2))
table_2.add_row('齿根圆直径', 'd_f', str(d_f1), str(d_f2))
table_2.add_row('齿宽', 'B', str(B_1), str(B_2))
print(table_2)

console.print("七、链传动设计", style="red")
P_4 = (F * V) / (1000 * eta_3)
