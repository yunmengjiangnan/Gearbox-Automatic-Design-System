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


# 30205型圆锥滚子轴承
class RollingBearing:
    def __init__(self, f_r1=2389.11, f_r2=700.43, F_ae=700.75, F_a1=597.28):
        self.C = 32.2
        self.e = 0.37
        self.Y = 1.6
        self.F_r1 = sqrt(F_AZ**2 + F_AY**2)
        self.F_r2 = sqrt(F_BZ**2 + F_BY**2)
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
            print()


