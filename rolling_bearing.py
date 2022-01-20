# -*- coding = utf-8 -*-
# @Time : 2022/1/19 14:40
# @Author : xzh
# @File : main.py
# @Software: PyCharm

import numpy as np
from math import pi, atan, cos, tan, sqrt, e
from rich import print
from rich.console import Console

# 实例化一个输出控制端
console = Console()


def P(f_p, x, f_r, y, f_a):
    p = f_p * (x * f_r + y * f_a)
    return p


def Lh(n, c, p, epsilon):
    l_h = 10 ** 6 / (60 * n) * (c / p) ** epsilon
    return l_h


# 30205型圆锥滚子轴承
class RollingBearing:
    def __init__(self, f_r1=2389.11, f_r2=700.43, F_ae=700.75, F_a1=597.28, n=1440, t=7.2*10**4):
        self.C = 32.2
        self.e = 0.37
        self.Y = 1.6
        self.F_r1 = sqrt(F_AZ ** 2 + F_AY ** 2)
        self.F_r2 = sqrt(F_BZ ** 2 + F_BY ** 2)
        self.F_ae = F_r = 108.49
        self.F_d1 = f_r1 / (2 * self.Y)
        self.F_d2 = f_r2 / (2 * self.Y)
        self.F_a1 = self.F_d1
        self.F_a2 = self.F_d2 + self.F_ae

        if self.F_d2 + self.F_ae < self.F_d1:
            print('∴轴承2压紧，轴承1放松'
                  '\n∴F_a1 = F_d1 =', self.F_a1, 'N',
                  '\n  F_a2 = F_d2 + F_ae =', self.F_a2, 'N')
        if self.F_a1 / self.F_r1 < e:
            print('F_a1 / F_r1 =', self.F_a1 / self.F_r1, '< e')
        elif self.F_a1 / self.F_r1 == e:
            print('F_a1 / F_r1 =', self.F_a1 / self.F_r1, '= e')
        else:
            print('F_a1 / F_r1 =', self.F_a1 / self.F_r1, '> e')
        self.X_1 = 1
        self.Y_1 = 0
        self.X_2 = 0.4
        self.Y_2 = 1.6
        self.f_p = 1.0
        self.P_1 = P(self.f_p, self.X_1, self.F_r1, self.Y_1, self.F_a1)
        self.P_2 = P(self.f_p, self.X_2, self.F_r2, self.Y_2, self.F_a2)
        print('由表查得：X_1 =', self.X_1, '，Y_1 =', self.Y_1, '，X_2 =', self.X_2, '，Y_2 =', self.Y_2,
              '轴承运转中有载荷稳定，按参考文献[2]书P：321表13-6查得，取 f_p = 1.0 滚动轴承当量动载荷P = f_p*(X*F_r+Y*F_a)',
              '\n所以P_1 =', self.P_1, 'N',
              '\n    P_2 =', self.P_2, 'N')
        self.epsilon = 10 / 3
        self.L_h = Lh(n, self.C, max(self.P_1, self.P_2), self.epsilon)
        if self.L_h > t:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', self.L_h, 'h > t'
                  '\n由此可见，轴承满足寿命要求')
        else:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', self.L_h, 'h ≤ t'
                  '\n由此可见，轴承不符合寿命要求!!!')


if __name__ == '__init__':
    rolling_bearing = RollingBearing
