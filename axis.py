# -*- coding = utf-8 -*-
# @Time : 2022/1/19 14:35
# @Author : xzh
# @File : main.py
# @Software: PyCharm
import math

import numpy as np
from math import pi, atan, cos, tan, sin
from rich import print
from rich.console import Console

# 实例化一个输出控制端
from rich.table import Table

console = Console()


def the_force_acting_on_the_bevel_gear(d, T, alpha=20, delta_1=18.3354):
    F_t1 = (2 * T) / d * 1000
    F_r1 = F_t1 * tan(alpha * pi / 180) * cos(delta_1 * pi / 180)
    F_a1 = F_t1 * tan(alpha * pi / 180) * sin(delta_1 * pi / 180)
    return F_t1, F_r1, F_a1


def the_force_acting_on_the_helical_gear(d, T, alpha=20, delta_1=14.15):
    F_t = (2 * T) / d * 1000
    F_r = F_t * tan(alpha * pi / 180) / cos(delta_1 * pi / 180)
    F_a = F_t * tan(delta_1 * pi / 180)
    return F_t, F_r, F_a


class HighSpeedShaft:
    def __init__(self, num, d, phi_r, p, n, t, bearing_D, bearing_T):
        console.print('1、求输入轴上的功率P', num, '、转速n', num, '和转矩T', num, style="yellow")
        self.P = p
        self.n = n
        self.T = t
        self.d = d
        self.sigma_B = 640
        self.sigma_S = 355
        self.sigma__1 = 275
        self.sigma__1_agree = 60
        self.d_m1 = d * (1 - 0.5 * phi_r)
        self.F_t1 = None
        self.F_r1 = None
        self.F_a1 = None
        print('P_', num, '=', self.P,
              '，n_', num, '=', self.n,
              '，T_', num, '=', self.T)
        console.print("2、求作用在齿轮上的力", style="yellow")
        self.F_t1, self.F_r1, self.F_a1 = the_force_acting_on_the_bevel_gear(self.d_m1, T=self.T)
        print('因已知高速级小锥齿轮齿宽中点处的分度圆直径为d_m1=d_1*(1-0.5*φ_R)=', self.d_m1, 'mm ',
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
        self.d_ii_iii = self.d_i_ii + 2
        self.d_iii_iv = math.ceil(self.d_ii_iii / 5) * 5
        self.d_iv_v = self.d_iii_iv + 5
        self.d_v_vi = self.d_iii_iv
        self.d_vi_vii = self.d_v_vi - 2
        self.d_vii_viii = self.d_i_ii

        self.bearing_d = self.d_iii_iv
        self.bearing_D = bearing_D
        self.bearing_T = bearing_T

        self.l_i_ii = 36
        self.l_ii_iii = 32
        self.l_iii_iv = 19
        self.l_iv_v = 60
        self.l_v_vi = 19
        self.l_vi_vii = 18
        self.l_vii_viii = 32
        # 长度真不知道咋算的

        self.D = 52
        print('选取原则：定位轴肩的高度h=(0.07~0.1)d ,非定位轴肩高度一般取1~2mm为了满足半联轴器的轴向定位要求，Ⅰ－Ⅱ轴段右端需制出一轴肩所以',
              '\n        d_I_II =', self.d_i_ii, 'L_I_II =', self.l_i_ii,
              '\n        d_II_III =', self.d_ii_iii, 'L_II_III =', self.l_ii_iii,
              '\n        Ⅲ~Ⅳ处与滚动轴承配合，考虑到滚动轴承是标准件，内径为5的倍数，故取',
              '\n        d_III_IV =', self.d_iii_iv,
              '\n        选取相应的轴承，因轴承同时受有径向力和轴向力的作用，故选用单列圆锥滚子轴承。参考工作要求，并根据',
              'd_III_IV =', self.d_iii_iv, '，查参考文献P：79表6－７，取０基本游隙组、标准精度级的单列圆锥滚子轴承30205，其尺寸为',
              '\n        d × D × T =', self.d_iii_iv, 'mm ×', self.bearing_D, 'mm × ', self.bearing_T, 'mm',
              '\n        因此取L_III_IV =', self.l_iii_iv, 'mm',
              '\n        同理，d_V_VI =', self.d_v_vi, 'mm   L_V_VI =', self.l_v_vi, 'mm',
              '\n        取   d_IV_V =', self.d_iv_v, 'mm   L_IV_V =', self.l_iv_v, 'mm',
              '\n             d_VI_VII =', self.d_vi_vii, 'mm    L_VI_VII =', self.l_vi_vii, 'mm',
              '\n             d_VII_VIII =', self.d_vii_viii, 'mm   L_VII_VIII =', self.l_vii_viii, 'mm')
        console.print("5、轴上零件的周向固定", style="yellow")
        console.print("1)齿轮与轴的周向定位采用平键联接。", style="green")
        self.i_ii_b = 6
        self.i_ii_h = 6
        self.i_ii_l = 28
        self.vii_viii_b = 6
        self.vii_viii_h = 6
        self.vii_viii_l = 22
        print('I-II段平键，按d_I_II =', self.d_i_ii, ',由参考文献表4-1查得平键的截面'
              '\nb =', self.i_ii_b, 'mm，h =', self.i_ii_h, 'mm，由该轴段长度取L =', self.i_ii_l, 'mm 。'
              '\nVII-VIII段平键，按d_I_II =', self.d_vii_viii, '，由参考文献表4-1查得平键的'
              '\n截面b =', self.vii_viii_b, 'mm，h =', self.vii_viii_h, 'mm，由该轴段长度取L =', self.vii_viii_l, 'mm。'
              '\n同时为了保证齿轮与轴配合得有良好得对中性，故选择齿轮轮毂与轴的配合选H7/n6。')
        console.print("2)滚动轴承与轴的周向定位，是借过渡配合来保证的，此处选轴的尺寸公差为m6。", style="green")
        console.print("6、轴上倒角与圆角", style="yellow")
        print('根据参考文献表，取轴端倒角C1，各轴肩处的圆角半径取C0.5。')


class MediumSpeedShaft:
    def __init__(self, num, d_1, d_2, p, n, t, delta_1, beta, bearing_D, bearing_T):
        console.print('1、求输入轴上的功率P', num, '、转速n', num, '和转矩T', num, style="yellow")
        self.P = p
        self.n = n
        self.T = t
        self.d_1 = d_1
        self.d_2 = d_2
        self.sigma_B = 640
        self.sigma_S = 355
        self.sigma__1 = 275
        self.sigma__1_agree = 60
        self.delta_1 = delta_1
        print('P_', num, '=', self.P,
              '，n_', num, '=', self.n,
              '，T_', num, '=', self.T)
        console.print("2、求作用在齿轮上的力", style="yellow")
        self.F_t1, self.F_r1, self.F_a1 = the_force_acting_on_the_bevel_gear(self.d_1, T=self.T, delta_1=self.delta_1)
        self.F_t2, self.F_r2, self.F_a2 = the_force_acting_on_the_helical_gear(self.d_2, T=self.T, delta_1=beta*180/pi)
        table_2 = Table(show_header=True, header_style='bold magenta')
        table_2.add_column()
        table_2.add_column('大锥齿轮d^,=d_m2=150mm')
        table_2.add_column('小斜齿轮d^(,,)=48.75mm')
        table_2.add_row('F_t=2T_2/d', str(self.F_t1), str(self.F_t2))
        table_2.add_row('F_r=Ft*', str(self.F_r1), str(self.F_r2))
        table_2.add_row('F_t=2T_2/d', str(self.F_a1), str(self.F_a2))
        print(table_2)
        console.print("3、初步确定轴的最小直径", style="yellow")
        self.A_0 = 110
        self.d = self.A_0 * np.cbrt(self.P / self.n)
        self.d_min = round(self.d * 1.15 / 5) * 5
        self.K_A = 1.5
        self.T_ca = self.K_A * self.T * 1000
        print('因为选取轴的材料为45钢调质处理，根据参考文献[2]表15-3，取A_0 =', self.A_0, '于是得',
              'd_min = A_0 * cbrt(P / n) =', self.d, 'mm'
              '\n考虑到这根轴有一个键，设计值加大10%，又因为最小直径处为两端，因为与轴承相连，所以取d_min =', self.d_min, 'mm。')

        console.print("4、轴的结构设计", style="yellow")
        console.print("(1)拟订轴上零件的装配方案", style="green")
        console.print("(2)根据轴向定位要求确定轴的各段直径和长度", style="green")
        self.d_i_ii = self.d_min
        self.d_ii_iii = self.d_i_ii + 5
        self.d_iii_iv = 47.3  # 搞不懂怎么算的
        self.d_iv_v = 34  # 不会
        self.d_v_vi = 28  # 不会
        self.d_vi_vii = 48  # 不会

        self.bearing_d = self.d_i_ii
        self.bearing_D = bearing_D
        self.bearing_T = bearing_T

        self.l_i_ii = 20
        self.l_ii_iii = 30
        self.l_iii_iv = 35
        self.l_iv_v = 20
        self.l_v_vi = 40
        self.l_vi_vii = 48
        print('   d_I_II = d_VI_VII', self.d_i_ii, 'L_I_II =', self.l_i_ii, 'mm， L_VI_VII =', self.l_vi_vii, 'mm',
              '\n   同时选取相应的轴承，因轴承同时受有径向力和轴向力的作用，故选用单'
              '\n   列圆锥滚子轴承。参考文献表6－７，取０基本游隙组、标准精度级'
              '\n   的单列圆锥滚子轴承30305，其尺寸为'
              '\n   d × D × T =', self.d_i_ii, 'mm ×', self.bearing_D, 'mm × ', self.bearing_T, 'mm'
              '\n   d_II_III =', self.d_ii_iii, 'mm     L_II_III =', self.l_ii_iii, 'mm（要考虑轴的整体布置）'
              '\n   d_III_IV =', self.d_iii_iv, 'mm   L_III_IV =', self.l_iii_iv, 'mm（小斜齿轮部分数据）'
              '\n   d_IV_V =', self.d_iv_v, 'mm       L_IV_V =', self.l_iv_v, 'mm'
              '\n   d_V_VI =', self.d_v_vi, 'mm       L_V_VI =', self.l_v_vi, 'mm')

        self.V_VI_b = 8
        self.V_VI_h = 7
        self.V_VI_l = 32

        console.print("5、轴上零件的周向固定", style="yellow")
        console.print("1)齿轮与轴的周向定位采用平键联接。", style="green")
        print('V-VI段采用普通平键联接，按d_V_VI =', self.d_v_vi, 'mm,由参考文献表4-1查得'
              '\n平键的截面，b=', self.V_VI_b, 'mm，h=', self.V_VI_h, 'mm，由该轴段长度取L =', self.V_VI_l, 'mm。'
              '\n同时为了保证齿轮与轴配合得有良好得对中性，固选择齿轮轮毂与轴得配合选H7/n6。')
        console.print("6、轴上倒角与圆角", style="yellow")
        print('根据参考文献表，取轴端倒角C1，各轴肩处的圆角半径取C0.5。')


class LowSpeedShaft:
    def __init__(self, num, d, phi_r, p, n, t, bearing_D, bearing_T):
        console.print('1、求输入轴上的功率P', num, '、转速n', num, '和转矩T', num, style="yellow")
        self.P = p
        self.n = n
        self.T = t
        self.d = d
        self.sigma_B = 640
        self.sigma_S = 355
        self.sigma__1 = 275
        self.sigma__1_agree = 60

        self.F_t1 = None
        self.F_r1 = None
        self.F_a1 = None
        print('P_', num, '=', self.P,
              '，n_', num, '=', self.n,
              '，T_', num, '=', self.T)
        console.print("2、求作用在齿轮上的力", style="yellow")
        self.F_t, self.F_r, self.F_a = the_force_acting_on_the_bevel_gear(self.d, T=self.T)
        print('因已知中速轴小斜齿轮的力已算出，则大斜齿轮上的力',
              '\n则F_t = (2*T_3)/d_3 =', self.F_t, 'N',
              '\nF_r1 = F_t1*tan(α)/cos(δ_1) =', self.F_r, 'N',
              '\nF_a1 =F_t1*tan(α)*sin(δ_1) =', self.F_a, 'N')
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
        self.d_ii_iii = self.d_i_ii + 2
        self.d_iii_iv = math.ceil(self.d_ii_iii / 5) * 5
        self.d_iv_v = self.d_iii_iv + 5
        self.d_v_vi = self.d_iii_iv
        self.d_vi_vii = self.d_v_vi - 2
        self.d_vii_viii = self.d_i_ii

        self.bearing_d = self.d_iii_iv
        self.bearing_D = bearing_D
        self.bearing_T = bearing_T

        self.l_i_ii = 36
        self.l_ii_iii = 32
        self.l_iii_iv = 19
        self.l_iv_v = 60
        self.l_v_vi = 19
        self.l_vi_vii = 18
        self.l_vii_viii = 32
        # 长度真不知道咋算的

        self.D = 52
        print('选取原则：定位轴肩的高度h=(0.07~0.1)d ,非定位轴肩高度一般取1~2mm为了满足半联轴器的轴向定位要求，Ⅰ－Ⅱ轴段右端需制出一轴肩所以',
              '\n        d_I_II =', self.d_i_ii, 'L_I_II =', self.l_i_ii,
              '\n        d_II_III =', self.d_ii_iii, 'L_II_III =', self.l_ii_iii,
              '\n        Ⅲ~Ⅳ处与滚动轴承配合，考虑到滚动轴承是标准件，内径为5的倍数，故取',
              '\n        d_III_IV =', self.d_iii_iv,
              '\n        选取相应的轴承，因轴承同时受有径向力和轴向力的作用，故选用单列圆锥滚子轴承。参考工作要求，并根据',
              'd_III_IV =', self.d_iii_iv, '，查参考文献P：79表6－７，取０基本游隙组、标准精度级的单列圆锥滚子轴承30205，其尺寸为',
              '\n        d × D × T =', self.d_iii_iv, 'mm ×', self.bearing_D, 'mm × ', self.bearing_T, 'mm',
              '\n        因此取L_III_IV =', self.l_iii_iv, 'mm',
              '\n        同理，d_V_VI =', self.d_v_vi, 'mm   L_V_VI =', self.l_v_vi, 'mm',
              '\n        取   d_IV_V =', self.d_iv_v, 'mm   L_IV_V =', self.l_iv_v, 'mm',
              '\n             d_VI_VII =', self.d_vi_vii, 'mm    L_VI_VII =', self.l_vi_vii, 'mm',
              '\n             d_VII_VIII =', self.d_vii_viii, 'mm   L_VII_VIII =', self.l_vii_viii, 'mm')
        console.print("5、求轴上的载荷", style="yellow")

        console.print("6、按弯扭合成应力校核轴的强度", style="yellow")

        console.print("7、轴上零件的周向固定", style="yellow")
        console.print("   1)齿轮与轴的周向定位采用平键联接。", style="green")

        self.ii_iii_b = 16
        self.ii_iii_h = 10
        self.ii_iii_l = 40
        self.vi_vii_b = 12
        self.vi_vii_h = 8
        self.vi_vii_l = 45

        print('   II-III段采用普通平键联接，按d_II_III =', self.d_ii_iii, ',由参考文献表4-1查得平键的截面'
              '\n   b =', self.ii_iii_b, 'mm，h =', self.ii_iii_h, 'mm，由该轴段长度取L =', self.ii_iii_l, 'mm 。'
              '\n   VI-VII段采用普通平键联接，按d_VI_VII =', self.d_vi_vii, '，由参考文献表4-1查得平键的'
              '\n   截面b =', self.vi_vii_b, 'mm，h =', self.vi_vii_h, 'mm，由该轴段长度取L =', self.vi_vii_l, 'mm。'
              '\n   同时为了保证齿轮与轴配合得有良好得对中性，故选择齿轮轮毂与轴的配合选H7/n6。')
        console.print("   2)滚动轴承与轴的周向定位，是借过渡配合来保证的，此处选轴的尺寸公差为m6。", style="green")
        console.print("8、轴上倒角与圆角", style="yellow")
        print('根据参考文献表，取轴端倒角C1，各轴肩处的圆角半径取C0.5。')


if __name__ == '__main__':
    print('(在本次设计中为减轻设计负担，只进行低速轴的强度校核)',
          '\n查表15-1选取轴的材料为45钢调质处理，硬度217~255HBs，'
          '抗拉强度极限σ_B = 640MPa'
          '，屈服极限σ_S = 355MPa'
          '，弯曲疲劳极限σ_-1 = 275MPa'
          '，许用弯曲应力[σ_-1] = 60MPa')
    console.print("（一）高速轴的设计计算", style='#FF6100')
    axis_1 = HighSpeedShaft(num=1, d=58.5, phi_r=1 / 3, p=3.50, n=1440, t=22.97)

    console.print("（二）中速轴的设计计算", style='#FF6100')
    # axis_2 = MediumSpeedShaft(num=2, alpha=20, delta_1=18.44, d=)

    console.print("（三）低速轴的设计计算", style='#FF6100')
    # axis_3 = AxisAndStrengthCheck(num=1, alpha=20, delta_1=18.44, d=)
