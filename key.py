# -*- coding = utf-8 -*-
# @Time : 2022/2/3 13:35
# @Author : xzh
# @File : key.py
# @Software: PyCharm
from rich.console import Console

# 实例化一个输出控制端
console = Console()


def CheckKeyConnectionStrength(part, b, h, l, T, d, __sigma_P__):
    l_ = l - b
    k = 0.5 * h
    sigma_P = (2 * T * 10 ** 3) / (k * l_ * d)
    print('轴的d = d_', part, ' =', d,
          '\n按参考文献表6-2由轴的设计计算可知所选平键为'
          '\nb × h × l =', b, 'mm ×', h, 'mm ×', l, 'mm'
          '\n按参考文献公式6-1校核键连接强度的公式:σ_P = (2 * T * 10**3) / (kld)'
          '\n其中k=0.5h；l=L-b')
    if sigma_P < __sigma_P__:
        print('\nσ_P = (2 * T_1 * 10**3) / (kld) =', sigma_P, 'MPa < [σ_P]'
              '\n强度满足，该键合理。')
    else:
        print('强度不满足，该键不合理，请重新选择平键参数')


class high_speed_key:
    def __init__(self, part_1, d_1, L_1, b_1, h_1, l_1, T_1,
                 part_2, d_2, L_2, b_2, h_2, l_2):
        console.print("1、与联轴器相连处的普通圆头平键：", style='yellow')
        self.part = part_1
        self.__sigma_P__ = 115
        self.d = d_1
        self.L = L_1
        self.b = b_1
        self.h = h_1
        self.l = l_1
        self.T_1 = T_1
        CheckKeyConnectionStrength(part=self.part, b=self.b, h=self.h, l=self.l, T=self.T_1, d=self.d, __sigma_P__=self.__sigma_P__)

        console.print("2、与小锥齿轮相连处的普通圆头平键：", style='yellow')
        CheckKeyConnectionStrength(part=)


if __name__ == '__main__':
    high_speed_key = high_speed_key(part_1='I_II', d_1=20, L_1=36, b_1=6, h_1=6, T_1=23.68, l_1=28)
