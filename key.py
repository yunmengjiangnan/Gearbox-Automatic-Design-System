# -*- coding = utf-8 -*-
# @Time : 2022/2/3 13:35
# @Author : xzh
# @File : key.py
# @Software: PyCharm
from rich.console import Console

# 实例化一个输出控制端
console = Console()


class high_speed_key:
    def __init__(self, d, b, h, l, T_1, k):
        console.print("1、与联轴器相连处的普通圆头平键：", style='yellow')
        self.d = d
        self.b = b
        self.h = h
        self.l = l
        self.k = k
        self.T_1 = T_1
        self.sigma_P = (2 * self.T_1 * 10 ** 3) / (self.k * self.l * self.d)
        print('轴的d = d_I_II =', self.d,
              '\n按参考文献表6-2由轴的设计计算可知所选平键为'
              '\nb × h × l =', self.b, 'mm ×', self.h, 'mm ×', self.l, 'mm'
              '\n按参考文献公式6-1校核键连接强度的公式:σ_P = (2 * T * 10**3) / (kld)'
              '\n其中k=0.5h；l=L-b')
        if self.sigma_P < self.sigma_P:
            print('\nσ_P = (2 * T_1 * 10**3) / (kld) =', self.sigma_P, 'MPa < [σ_P]'
                  '\n强度满足，该键合理。')
        else:
            print('强度不满足，该键不合理，请重新选择平键参数')


if __name__ == '__main__':
    high_speed_key = high_speed_key()
