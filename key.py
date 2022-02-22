# -*- coding = utf-8 -*-
# @Time : 2022/2/3 13:35
# @Author : xzh
# @File : key.py
# @Software: PyCharm
from rich.console import Console

__sigma_P__ = 115  # 键的许用挤压应力
# 实例化一个输出控制端
console = Console()


def CheckKeyConnectionStrength(part, L, b, h, l, T, d):
    l_ = l - b
    k = 0.5 * h
    sigma_P = (2 * T * 10 ** 3) / (k * l_ * d)
    print('轴的d = d_', part, ' =', d, 'mm，L =', L, 'mm'
          '\n按参考文献表6-2由轴的设计计算可知所选平键为'
          '\nb × h × l =', b, 'mm ×', h, 'mm ×', l, 'mm'
          '\n按参考文献公式6-1校核键连接强度的公式:σ_P = (2 * T * 10**3) / (kld)'
          '\n其中k=0.5h；l=L-b')
    if sigma_P < __sigma_P__:
        print('σ_P = (2 * T_1 * 10**3) / (kld) =',
              '(2 ×', T, '× 10**3) / (', k, '×', l, '×', d, ') =', sigma_P, 'MPa < [σ_P]'
              '\n强度满足，该键合理。')
    else:
        print('强度不满足，该键不合理，请重新选择平键参数')


class high_speed_key:
    def __init__(self, part_1, d_1, L_1, b_1, h_1, l_1, T_1,
                 part_2, d_2, L_2, b_2, h_2, l_2):
        self.T_1 = T_1

        console.print("1、与联轴器相连处的普通圆头平键：", style='yellow')
        self.part_1 = part_1
        self.d_1 = d_1
        self.L_1 = L_1
        self.b_1 = b_1
        self.h_1 = h_1
        self.l_1 = l_1
        CheckKeyConnectionStrength(part=self.part_1, L=self.L_1, b=self.b_1, h=self.h_1, l=self.l_1, T=self.T_1, d=self.d_1)

        console.print("2、与小锥齿轮相连处的普通圆头平键：", style='yellow')
        self.part_2 = part_2
        self.d_2 = d_2
        self.L_2 = L_2
        self.b_2 = b_2
        self.h_2 = h_2
        self.l_2 = l_2
        CheckKeyConnectionStrength(part=self.part_2, L=self.L_2, b=self.b_2, h=self.h_2, l=self.l_2, T=self.T_1, d=self.d_2)


class medium_speed_key:
    def __init__(self, part, d, L, b, h, l, T_2):
        self.T_2 = T_2
        self.part = part
        self.d = d
        self.L = L
        self.b = b
        self.h = h
        self.l = l
        console.print("1、与大锥齿轮相连处的普通圆头平键：", style='yellow')
        CheckKeyConnectionStrength(part=self.part, L=self.L, d=self.d, b=self.b, h=self.h, l=self.l, T=self.T_2)


class low_speed_key:
    def __init__(self, part_1, d_1, L_1, b_1, h_1, l_1, T_3,
                 part_2, d_2, L_2, b_2, h_2, l_2):
        self.T_3 = T_3

        console.print("1、与大斜齿轮相连处的普通圆头平键：", style='yellow')
        self.part_1 = part_1
        self.d_1 = d_1
        self.L_1 = L_1
        self.b_1 = b_1
        self.h_1 = h_1
        self.l_1 = l_1
        CheckKeyConnectionStrength(part=self.part_1, L=self.L_1, b=self.b_1, h=self.h_1, l=self.l_1, T=self.T_3,
                                   d=self.d_1)

        console.print("2、与链轮相连处的普通圆头平键：", style='yellow')
        self.part_2 = part_2
        self.d_2 = d_2
        self.L_2 = L_2
        self.b_2 = b_2
        self.h_2 = h_2
        self.l_2 = l_2
        CheckKeyConnectionStrength(part=self.part_2, L=self.L_2, b=self.b_2, h=self.h_2, l=self.l_2, T=self.T_3,
                                   d=self.d_2)


if __name__ == '__main__':
    # high_speed_key = ky.high_speed_key(part_1="I_II", d_1=axis_1.d_i_ii, L_1=axis_1.l_i_ii, b_1=6, h_1=6, l_1=28,
    # T_1=axis_1.T, part_2="VII_VIII", d_2=axis_1.d_vii_viii, L_2=axis_1.l_vii_viii, b_2=6, h_2=6, l_2=22)
    # 懒得写test
    pass

