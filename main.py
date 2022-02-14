# -*- coding = utf-8 -*-
# @Time : 2022/1/15 18:14
# @Author : xzh
# @File : main.py
# @Software: PyCharm
import math
# import numpy as np
from math import cos, pi, sqrt, tan, sin

import numpy as np
from rich import print
from rich.console import Console
from rich.table import Column, Table
# from prettytable import PrettyTable

import motor as mt
import gear_ratio as gr
import transmission_parameters as tp
import gear_drive as gd
import axis as ax

# 已知条件
from rolling_bearing import RollingBearing

F = 8
v = 0.37
d = 351
# 实例化一个输出控制端
console = Console()
console.print("一、设计任务：", style="red")
print('设计一个用于带式运输机上的圆锥圆柱齿轮减速器。已知条件如下：')
table_1 = Table(show_header=True, header_style='bold magenta')
table_1.add_column('组数')
table_1.add_column('输送链的牵引力F（KG）')
table_1.add_column('输送链的速度v(m/s)')
table_1.add_column('输送链链轮节圆直径d(mm)')
table_1.add_row('第六组', '8', '0.37', '351')
print(table_1)
# 计算工作寿命
print('注：1.链板式输送机工作时，运转方向不变，工作载荷稳定。'
      '\n    2.工作寿命15年，每年300个工作日，每日工作16小时。')
t = 15 * 300 * 16
print('工作寿命：t=15×300×16h=7.2×10^4 h')
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
# print('选YX3系列132S-4型号电动机，主要技术数据如下：'
#       '\n额定功率：5.5 kw'
#       '\n满载转速：1440r/min')
print('选Y112M-4型号电动机，主要技术数据如下：'
      '\n额定功率：4 kw'
      '\n满载转速：1440 r/min')

# 四、传动装置的总传动比及其分配
console.print("四、传动装置的总传动比及其分配", style="red")
# 1、系统总传动比i
i = gr.Total_Gear_Ratio(n)
# 2、分配传动比(圆锥齿轮传动i_1/圆柱齿轮传动i_2/链传动i_3)
i_1 = 3
i_2 = 5
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
print('（1）选用标准直齿锥齿轮传动，压力角取20°，轴交角∑=90°。',
      '\n（2）齿轮精度由上面三电机选择时确定为8级。',
      '\n（3）材料选择：选择小锥齿轮材料为45钢（调质），硬度为250HBS；大齿轮材料也为45钢（调质），硬度为220HBS，二者硬度差为30HBS。',
      '\n（4）初选小齿轮齿数Z1=20，大齿轮齿数Z2=uZ1=3x20=60。')
console.print("2、按齿面接触强度设计", style="yellow")
console.print("1)确定公式的各计算数值", style="green")
bevel_gear_D = gd.BevelGear.DesignAccordingToToothSurfaceContactStrength(i_1=i_1, T_1=T_1, n_1=n_1)
console.print("2)调整小齿轮分度圆直径", style="green")
R = bevel_gear_D.Tooth_Contact_Strength_Design(n_1=n_1)
console.print("3）计算载荷系数", style="green")
m_1, d_1 = bevel_gear_D.Load_Factor()

console.print("3、校核齿根弯曲强度", style='yellow')
console.print("1）确定公式的各计算数值", style="green")
bevel_gear_C = gd.BevelGear.CheckToothRootBendingStrength(Z_1=bevel_gear_D.Z_1, Z_2=bevel_gear_D.Z_2,
                                                          mu=bevel_gear_D.mu)
console.print("2）代入数值计算", style="green")
m_2 = bevel_gear_C.Substitution_Calculation_1(T_1=T_1, phi_R=1 / 3, d_1=d_1, m=m_1)
console.print("3）代入数值计算", style="green")
m = max(m_1, m_2)
d_m1, d_m2, d_1, d_2, B_1, B_2 = bevel_gear_C.Substitution_Calculation_2(m=m, phi_R=1 / 3)

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
table.add_row('分锥角', 'δ', str(bevel_gear_C.delta_1), str(bevel_gear_C.delta_2))
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
helical_spur_gear_D = gd.HelicalSpurGear.DesignAccordingToToothSurfaceContactStrength(i_2=i_2, T_2=T_2,
                                                                                      n_2=n_2)
console.print("3、按齿根弯曲强度设计", style="yellow")
helical_spur_gear_C = gd.HelicalSpurGear.CheckToothRootBendingStrength(i_2=i_2, T_2=T_2, d_1=helical_spur_gear_D.d_1)
m_n = None
if helical_spur_gear_D.m_n > helical_spur_gear_C.m_n_min:
    m_n = round(helical_spur_gear_D.m_n)
    print('对比计算结果，由齿面接触疲劳强度计算的法面模数m_n大于由齿根弯曲疲劳强度计算的法面模数，取m_n =', m_n,
          '已可满足弯曲强度。')
helical_spur_gear_D.Z_1 = helical_spur_gear_D.d_1 * cos(helical_spur_gear_D.beta) / m_n
helical_spur_gear_D.Z_1 = round(helical_spur_gear_D.Z_1)
helical_spur_gear_D.Z_2 = i_2 * helical_spur_gear_D.Z_1
print('但为同时满足接触疲劳强度，需按接触疲劳强度算得的分度圆直径d_1 =', helical_spur_gear_D.d_1,
      '\n于是有：Z_1 =', helical_spur_gear_D.Z_1,
      '\n则Z_2 =', helical_spur_gear_D.Z_2)
console.print("4、计算几何尺寸", style="yellow")
console.print("1）计算中心距", style="green")
a_float = ((helical_spur_gear_C.Z_1 + helical_spur_gear_C.Z_2) * m_n) / (
        2 * cos(helical_spur_gear_C.beta))
a = round(a_float)
print('a =', a_float, 'mm'
                      '将中心距圆整为', a, 'mm')
console.print("2）按圆整后的中心距修正螺旋角β", style="green")
beta = math.acos(((helical_spur_gear_C.Z_1 + helical_spur_gear_C.Z_2) * m_n) / (2 * a))
rate = (beta - helical_spur_gear_C.beta) / helical_spur_gear_C.beta
if rate < 0.05:
    print('β =', beta,
          '且β与原定义β差距在5%以内，螺旋角值β改变不多，故参数ε_α、K_β、Z_H等不必修正')
console.print("3）计算大、小齿轮分度圆直径", style="green")
d_1 = (m_n * helical_spur_gear_C.Z_1) / cos(beta)
d_2 = (m_n * helical_spur_gear_C.Z_2) / cos(beta)
console.print("4）计算齿轮宽度", style="green")
float_b = helical_spur_gear_D.phi_d * helical_spur_gear_D.d_1
b = round(float_b)
print('b=φ_d * d_1 =', float_b,
      '\n圆整后，取B_2 =', b, '，B_1 =', round(b * 1.1))
console.print("5、计算所得结果汇总如下表备用。", style="yellow")
m_n = m_n
m_t = m_n / cos(beta)
a_n = 20
h_a = 1 * m_n
h_f = 1.25 * m_n
d_a1 = helical_spur_gear_D.d_1 + 2 * h_a * cos(helical_spur_gear_C.beta)
d_a2 = helical_spur_gear_D.d_2 + 2 * h_a * cos(helical_spur_gear_C.beta)
d_f1 = helical_spur_gear_D.d_1 - 2 * h_f * cos(helical_spur_gear_C.beta)
d_f2 = helical_spur_gear_D.d_2 - 2 * h_f * cos(helical_spur_gear_C.beta)
B_2 = b
B_1 = round(b * 1.1)
table_2 = Table(show_header=True, header_style='bold magenta')
table_2.add_column('名称')
table_2.add_column('符号')
table_2.add_column('小齿轮')
table_2.add_column('大齿轮')
table_2.add_row('螺旋角', 'β', str(beta / pi * 180), str(beta / pi * 180))
table_2.add_row('法面模数', 'm_n', str(m_n), str(m_n))
table_2.add_row('端面模数', 'm_t', str(m_t), str(m_t))
table_2.add_row('法面压力角', 'α_n', str(a_n), str(a_n))
table_2.add_row('分度圆直径', 'd', str(helical_spur_gear_D.d_1), str(helical_spur_gear_D.d_2))
table_2.add_row('齿顶高', 'h_a', str(h_a), str(h_a))
table_2.add_row('齿根高', 'h_f', str(h_f), str(h_f))
table_2.add_row('齿顶圆直径', 'd_a', str(d_a1), str(d_a2))
table_2.add_row('齿根圆直径', 'd_f', str(d_f1), str(d_f2))
table_2.add_row('齿宽', 'B', str(B_1), str(B_2))
print(table_2)

console.print("七、链传动设计", style="red")
eta_3 = 0.96
P_4 = (F * v) / (1000 * eta_3)
print('链传动传递功率：P_4 =', P_4, 'KW',
      '\n传动比i_3 =', i_3)
Z_1 = 17
Z_2 = round(i_3 * 17)
print('（1）选择链传动齿数，取Z_1=17根据传动比Z_2=', i_3, '×17≈', Z_2)
K_A = 1.0
K_Z = 1.52
P_ca = K_A * K_Z * P_4 * 1000
print('（2）确定计算功率'
      '\n     K_A =', K_A,
      '，K_Z =', K_Z,
      '，初选为单排链传动。'
      '\n     P_ca =K_A*K_Z*P_4 =', P_ca)
P = 31.75
print('（3）选择链条节数和中心距'
      '\n     根据P_ca =K_A*K_Z*P_4 =', P_ca, 'kw及n_3 =', n_3, 'r/min',
      '查得可选20A—1，链节距P =', P, '㎜')
a_0_min = 30 * P
a_0_max = 50 * P

# 需要手动选取
a_0 = 1000

L_P0 = 2 * a_0 / P + (Z_1 + Z_2) / 2 + ((Z_2 - Z_1) / 2 / pi) ** 2 * P / a_0
L_P = round(L_P0)
f_I = 0.23737  # 查表，并用差值法求得
float_a = f_I * P * (2 * L_P - (Z_1 + Z_2))
a = round(float_a)
print('（4）计算链节数和中心距'
      '\n      初选中心距a_0=(30-50)p=', a_0_min, ' ~ ', a_0_max, 'mm,取a_0 =', a_0, 'mm'
                                                                               '\n      相应的链长节数L_P0 =', L_P0, 'mm'
                                                                                                              '\n      取链长节数L_P=',
      L_P,
      ' (L_P-Z_1)/(Z_2-Z_1 )=', (L_P - Z_1) / (Z_2 - Z_1),
      '\n      查表,并用差值法得中心距系数f_I=', f_I,
      '\n      a=f_I * P[2L_P-(Z_1+Z_2 )]=', float_a, 'mm',
      '\n      取整a =', a, 'mm')

v = (n_3 * Z_1 * P) / 60 / 1000
print('(5)计算链速，确定润滑方式，v=(n_3 z_1 p)/(60×1000)=', v, 'm/s'
                                                    '\n       由v=', v, 'm/s和链号20A—1 查参考文献[2]图9-4 采用滴油润滑')
F_e = 1000 * P_4 * 1000 / v
K_FP = 1.15
F_P = K_FP * F_e
print('(6)计算轴向力，有效圆周力为：F_e = 1000 * P_4 / v =', F_e, 'N'
                                                     '\n        链轮水平布置时轴力系数K_FP =', K_FP, '则周向力为F_p ≈', F_P, 'N')

console.print("八、轴的设计计算", style="red")
print('(在本次设计中为减轻设计负担，只进行低速轴的强度校核)',
      '\n查表15-1选取轴的材料为45钢调质处理，硬度217~255HBs，'
      '抗拉强度极限σ_B = 640MPa'
      '，屈服极限σ_S = 355MPa'
      '，弯曲疲劳极限σ_-1 = 275MPa'
      '，许用弯曲应力[σ_-1] = 60MPa')
console.print("（一）高速轴的设计计算", style='#FF6100')
axis_1 = ax.HighSpeedShaft(num=1, d=d_m1, phi_r=1/3, p=P_1, n=n_1, t=T_1, bearing_D=52, bearing_T=16.25)

console.print("（二）中速轴的设计计算", style='#FF6100')
axis_2 = ax.MediumSpeedShaft(num=2, delta_1=bevel_gear_C.delta_1, beta=beta, d_1=d_m2, d_2=helical_spur_gear_D.d_1, p=P_2, n=n_2, t=T_2, bearing_D=62, bearing_T=18.25)

console.print("（三）低速轴的设计计算", style='#FF6100')
axis_3 = ax.LowSpeedShaft(num=3, d=helical_spur_gear_D.d_2, phi_r=1/3, p=P_3, n=n_3, t=T_3, bearing_D=100, bearing_T=27.25)

console.print("九、滚动轴承的校核", style="red")
console.print("（一）高速轴上的轴承", style='#FF6100')
# rolling_bearing_1 = RollingBearing()

console.print("十、键的选择及强度校核", style="red")
print('键、轴、轮毂材料都是钢，由参考文献[2]表6-2查得许用挤压应力 ，取[σ_p] = 100MPa ~ 120MPa，取[σ_p] = 115MPa。'
      '\n说明：本次全部选择圆头普通平键，由于键是标准件，其宽和高是按轴的直径来取的。键的长度一般比连接的轮毂略小，自行取定。')
console.print("(一)高速轴上的键联接", style='#FF6100')
