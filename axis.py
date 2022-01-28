# -*- coding = utf-8 -*-
# @Time : 2022/1/19 14:35
# @Author : xzh
# @File : main.py
# @Software: PyCharm

import numpy as np
from math import pi, atan, cos, tan, sin
from rich import print
from rich.console import Console

# 实例化一个输出控制端
console = Console()


class Axis:
    def __init__(self, num, alpha, delta_1, d, phi_r, p, n, t):
        console.print('1、求输入轴上的功率P', num, '、转速n', num, '和转矩T', num, style="yellow")
        self.P = p
        self.n = n
        self.T = t
        self.d = d
        self.sigma_B = 640
        self.sigma_S = 355
        self.sigma__1 = 275
        self.sigma__1_agree = 60

        # console.print("1、求输入轴上的功率P1、转速n1和转矩T1", style="yellow")
        print('P_', num, '=', self.P,
              '，n_', num, '=', self.n,
              '，T_', num, '=', self.T)
        console.print("2、求作用在齿轮上的力", style="yellow")
        d_m1 = d * (1 - 0.5 * phi_r)
        self.F_t1 = (2 * self.T) / d_m1 * 1000
        self.F_r1 = self.F_t1 * tan(alpha * pi / 180) * cos(delta_1 * pi / 180)
        self.F_a1 = self.F_t1 * tan(alpha * pi / 180) * sin(delta_1 * pi / 180)
        print('因已知高速级小锥齿轮齿宽中点处的分度圆直径为d_m1=d_1*(1-0.5*φ_R)=', d_m1, 'mm ',
              '\n则F_t1 = (2*T_1)/d_m1 =', self.F_t1, 'N',
              '\nF_r1 = F_t1*tan(α)*cos(δ_1) =', self.F_r1, 'N',
              '\nF_a1 =F_t1*tan(α)*sin(δ_1) =', self.F_a1, 'N')
        console.print("3、初步确定轴的最小直径", style="yellow")
        self.A_0 = 115
        self.d = self.A_0 * np.cbrt(self.P / self.n)
        self.d_min = round(self.d * 1.15 / 5) * 5
        self.K_A = 1.5
        self.T_ca = self.K_A * self.T * 1000
        print('根据参考文献[2]表15-3，由于最小直径处只受扭矩作用,取A_0 =', self.A_0, '，根据P：370公式（15-2）于是得',
              '\nd ≥ ', self.d, 'mm',
              '考虑到这个轴上有两个键槽，设计值要加大15%；由图可知，轴最小直径处与联轴器相连，考虑到联轴器是标准件，故取',
              'd_min =', self.d_min, 'mm',
              '为了使联轴器的孔径与所选的轴直径d_(Ⅰ-Ⅱ)相适应，故需同时选取联轴器型号：'
              '\n联轴器的计算转矩T_ca=K_A*T_1，查参考文献[2]表１４－１，考虑到转矩变化很小，故取K_A =', self.K_A, '，则：T_ca=K_A*T_1=', self.T_ca, 'N⋅mm',
              '\n按照计算转矩T_ca应小于联轴器公称转矩的条件，并满足电动机要求，因处于高速级，小功率，选取弹性柱销联轴器，查参考文献[1]表8—5，'
              '选取LX2型弹性柱销联轴器，型号：LX2联轴器，其公称扭矩为T_n=560N⋅m。'
              '半联轴器的孔径 ，故取d_(Ⅰ-Ⅱ)=', self.d_min, 'mm，半联轴器长度L=38mm，半联轴器与轴配合的毂孔长度L_1=52mm（其余尺寸按表中取值）。')

        console.print("4、轴的结构设计", style="yellow")

        console.print("（1）拟订轴上零件的装配方案", style="yellow")
        console.print("（２）根据轴向定位要求确定轴的各段直径和长度", style="yellow")
        self.d_i_ii = self.d_min
        self.l_i_ii = 36
        self.l_ii_iii = 32
        print('选取原则：定位轴肩的高度h=(0.07~0.1)d ,非定位轴肩高度一般取1~2mm为了满足半联轴器的轴向定位要求，Ⅰ－Ⅱ轴段右端需制出一轴肩所以',
              '\n        d_I_II =', self.d_i_ii, 'L_I_II =', self.l_i_ii,
              '\n        d_II_III =', self.d_i_ii + 2, 'L_II_III =', self.l_ii_iii)
        console.print("5、轴上零件的周向固定", style="yellow")
        console.print("6、轴上倒角与圆角", style="yellow")


class AxisAndStrengthCheck:
    def __init__(self, num, alpha, delta_1, d, phi_r, p, n, t):
        console.print('1、求输入轴上的功率P', num, '、转速n', num, '和转矩T', num, style="yellow")
        self.P = p
        self.n = n
        self.T = t
        self.d = d
        self.sigma_B = 640
        self.sigma_S = 355
        self.sigma__1 = 275
        self.sigma__1_agree = 60

        print('(在本次设计中为减轻设计负担，只进行低速轴的强度校核)',
              '\n查表15-1选取轴的材料为45钢调质处理，硬度217~255HBs，'
              '抗拉强度极限σ_B =', self.sigma_B,
              '，屈服极限σ_S =', self.sigma_S,
              '，弯曲疲劳极限σ_-1 =', self.sigma__1,
              '，许用弯曲应力[σ_-1] =', self.sigma__1_agree, 'MPa')
        console.print("1、求输入轴上的功率P1、转速n1和转矩T1", style="yellow")
        print('P_1 =', self.P,
              '，n_1 =', self.n,
              '，T_1 =', self.T)
        console.print("2、求作用在齿轮上的力", style="yellow")
        d_m1 = d * (1 - 0.5 * phi_r)
        self.F_t1 = (2 * self.T) / d_m1 * 1000
        self.F_r1 = self.F_t1 * tan(alpha * pi / 180) * cos(delta_1 * pi / 180)
        self.F_a1 = self.F_t1 * tan(alpha * pi / 180) * sin(delta_1 * pi / 180)
        print('因已知高速级小锥齿轮齿宽中点处的分度圆直径为d_m1=d_1*(1-0.5*φ_R)=', d_m1, 'mm ',
              '\n则F_t1 = (2*T_1)/d_m1 =', self.F_t1, 'N',
              '\nF_r1 = F_t1*tan(α)*cos(δ_1) =', self.F_r1, 'N',
              '\nF_a1 =F_t1*tan(α)*sin(δ_1) =', self.F_a1, 'N')
        console.print("3、初步确定轴的最小直径", style="yellow")
        self.A_0 = 100
        self.d = self.A_0 * np.cbrt(self.P / self.n)
        self.d_min = round(d / 10) * 10
        self.K_A = 1.5
        self.T_ca = self.K_A * self.T
        print('根据参考文献[2]表15-3，由于最小直径处只受扭矩作用,取A_0 =', self.A_0, '，根据P：370公式（15-2）于是得',
              '\nd ≥ ', self.d, 'mm',
              '考虑到这个轴上有两个键槽，设计值要加大15%；由图可知，轴最小直径处与联轴器相连，考虑到联轴器是标准件，故取',
              'd_min =', self.d_min, 'mm',
              '为了使联轴器的孔径与所选的轴直径d_(Ⅰ-Ⅱ)相适应，故需同时选取联轴器型号：'
              '\n联轴器的计算转矩T_ca=K_A*T_1，查参考文献[2]表１４－１，考虑到转矩变化很小，故取K_A =', self.K_A, '，则：T_ca=K_A*T_1=', self.T_ca, 'N⋅mm',
              '\n按照计算转矩T_ca应小于联轴器公称转矩的条件，并满足电动机要求，因处于高速级，小功率，选取弹性柱销联轴器，查参考文献[1]表8—5，'
              '选取LX2型弹性柱销联轴器，型号：LX2联轴器，其公称扭矩为T_n=560N⋅m。'
              '半联轴器的孔径 ，故取d_(Ⅰ-Ⅱ)=', self.d_min, 'mm，半联轴器长度L=38mm，半联轴器与轴配合的毂孔长度L_1=52mm（其余尺寸按表中取值）。')

        console.print("4、轴的结构设计", style="yellow")
        console.print("（1）拟订轴上零件的装配方案", style="yellow")
        print('小圆锥齿轮采用悬臂结构，轴装于套杯内，一对圆锥滚子轴承支撑（正装）。')
        console.print("（２）根据轴向定位要求确定轴的各段直径和长度", style="yellow")
        self.d_i_ii = self.d_min
        self.l_i_ii = 36
        self.l_ii_iii = 32
        print('选取原则：定位轴肩的高度h=(0.07~0.1)d ,非定位轴肩高度一般取1~2mm为了满足半联轴器的轴向定位要求，Ⅰ－Ⅱ轴段右端需制出一轴肩所以',
              '\n        d_I_II =', self.d_i_ii, 'L_I_II =', self.l_i_ii,
              '\n        d_II_III =', self.d_i_ii + 2, 'L_II_III =', self.l_ii_iii)
        console.print("5、求轴上的载荷", style="yellow")
        console.print("6、按弯扭合成应力校核轴的强度", style="yellow")
        console.print("7、轴上零件的周向固定", style="yellow")
        console.print("8、轴上倒角与圆角", style="yellow")


if __name__ == '__main__':
    print('(在本次设计中为减轻设计负担，只进行低速轴的强度校核)',
          '\n查表15-1选取轴的材料为45钢调质处理，硬度217~255HBs，'
          '抗拉强度极限σ_B = 640MPa'
          '，屈服极限σ_S = 355MPa'
          '，弯曲疲劳极限σ_-1 = 275MPa'
          '，许用弯曲应力[σ_-1] = 60MPa')
    console.print("（一）高速轴的设计计算", style='#FF6100')
    axis_1 = Axis(num=1, alpha=20, delta_1=18.44, d=58.5, phi_r=1 / 3, p=3.50, n=1440, t=22.97)

    console.print("（二）中速轴的设计计算", style='#FF6100')
    # axis_2 = Axis(num=2, alpha=20, delta_1=18.44, d=)

    console.print("（三）低速轴的设计计算", style='#FF6100')
    # axis_3 = AxisAndStrengthCheck(num=1, alpha=20, delta_1=18.44, d=)
