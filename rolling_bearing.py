# -*- coding = utf-8 -*-
# @Time : 2022/1/19 14:40
# @Author : xzh
# @File : main.py
# @Software: PyCharm

from math import sqrt, e
from rich import print
from rich.console import Console

# 实例化一个输出控制端
console = Console()


def P(f_p, x, f_r, y, f_a):
    p = f_p * (x * f_r + y * f_a)
    p = round(p * 100) / 100
    return p


def Lh(n, c, p, epsilon):
    l_h = 10 ** 6 / (60 * n) * (c * 1000 / p) ** epsilon
    l_h = round(l_h * 100) / 100
    return l_h


def compare(num, F_a, F_r, e):
    if (F_a / F_r) < e:
        print('F_a', num, ' / F_r', num, ' =', F_a / F_r, '< e')
    elif F_a / F_r == e:
        print('F_a', num, ' / F_r', num, ' =', F_a / F_r, '= e')
    else:
        print('F_a', num, ' / F_r', num, ' =', F_a / F_r, '> e')


# 30205型圆锥滚子轴承
class RollingBearing_1:
    def __init__(self, F_r, n, t,
                 f_r1=1055.39, f_r2=257.50, F_a1=597.28):
        self.C = 32.2
        self.e = 0.37
        self.Y = 1.6
        # self.F_r1 = sqrt(F_CZ ** 2 + F_CY ** 2)
        # self.F_r2 = sqrt(F_AZ ** 2 + F_AY ** 2)
        self.F_r1 = f_r1
        self.F_r2 = f_r2
        self.F_ae = F_r
        self.F_d1 = f_r1 / (2 * self.Y)
        self.F_d2 = f_r2 / (2 * self.Y)
        self.F_a1 = self.F_d1
        self.F_a2 = self.F_d2 + self.F_ae

        print('由轴的设计计算可知高速轴滚动轴承选用30309型圆锥滚子轴承，'
              '根据参考文献[1]P：76表6-7查得C=', self.C,
              'kN   e=', self.e,
              '  Y=', self.Y,
              '\n   F_r1 = √([F_CZ]^2+[F_CY]^2) =', self.F_r1,
              'N\n   F_r2 = √([F_AZ]^2+[F_AY]^2) =', self.F_r2,
              'N\n   在设计高速轴的时候已经算得F_ae=F_r=', self.F_ae,
              'N\n   由参考文献[2]P：322表13-7得')
        if self.F_d2 + self.F_ae < self.F_d1:
            print('由图：Fd_2+Fae < Fd_1\n∴轴承2压紧，轴承1放松'
                  '\n∴F_a1 = F_d1 =', self.F_a1, 'N',
                  '\n  F_a2 = F_d2 + F_ae =', self.F_a2, 'N')

        compare(num=1, F_a=self.F_a1, F_r=self.F_r1, e=self.e)
        compare(num=2, F_a=self.F_a2, F_r=self.F_r2, e=self.e)
        self.X_1 = 1
        self.Y_1 = 0
        self.X_2 = 0.4
        self.Y_2 = 1.6
        self.f_p = 1.0
        self.P_1 = P(self.f_p, self.X_1, self.F_r1, self.Y_1, self.F_a2)
        self.P_2 = P(self.f_p, self.X_2, self.F_r2, self.Y_2, self.F_a2)
        print('由表查得：X_1 =', self.X_1, '，Y_1 =', self.Y_1,
              '\n         X_2 =', self.X_2, '，Y_2 =', self.Y_2,
              '轴承运转中有载荷稳定，按参考文献[2]书P：321表13-6查得，取 f_p = 1.0 滚动轴承当量动载荷P = f_p*(X*F_r+Y*F_a)',
              '\n所以P_1 =', self.P_1, 'N',
              '\n    P_2 =', self.P_2, 'N')
        self.epsilon = 10 / 3
        self.L_h = Lh(n, self.C, max(self.P_1, self.P_2), self.epsilon)
        if self.L_h > t:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', format(self.L_h, '.1E'),
                  'h > t\n由此可见，轴承满足寿命要求')
        else:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', format(self.L_h, '.1E'),
                  'h ≤ t\n由此可见，轴承不符合寿命要求!!!')


# 30305型圆锥滚子轴承
class RollingBearing_2:
    def __init__(self, F_r, n, t,
                 f_r1=2389.11, f_r2=700.43, F_a1=597.28):
        self.C = 46.8
        self.e = 0.3
        self.Y = 2
        # self.F_r1 = sqrt(F_CZ ** 2 + F_CY ** 2)
        # self.F_r2 = sqrt(F_AZ ** 2 + F_AY ** 2)
        self.F_r1 = f_r1
        self.F_r2 = f_r2
        self.F_ae = F_r
        self.F_d1 = f_r1 / (2 * self.Y)
        self.F_d2 = f_r2 / (2 * self.Y)
        self.F_a1 = self.F_d1
        self.F_a2 = self.F_d1 + self.F_ae

        print('由轴的设计计算可知高速轴滚动轴承选用30309型圆锥滚子轴承，'
              '根据参考文献[1]P：76表6-7查得C=', self.C,
              'kN   e=', self.e,
              '  Y=', self.Y,
              '\n   F_r1 = √([F_CZ]^2+[F_CY]^2) =', self.F_r1,
              'N\n   F_r2 = √([F_AZ]^2+[F_AY]^2) =', self.F_r2,
              'N\n   在设计高速轴的时候已经算得F_ae=F_r=', self.F_ae,
              'N\n   由参考文献[2]P：322表13-7得')
        if self.F_d2 + self.F_ae < self.F_d1:
            print('由图：Fd_2+Fae < Fd_1\n∴轴承2压紧，轴承1放松'
                  '\n∴F_a1 = F_d1 =', self.F_a1, 'N',
                  '\n  F_a2 = F_d2 + F_ae =', self.F_a2, 'N')

        compare(num=1, F_a=self.F_a1, F_r=self.F_r1, e=self.e)
        compare(num=2, F_a=self.F_a2, F_r=self.F_r2, e=self.e)
        self.X_1 = 1
        self.Y_1 = 0
        self.X_2 = 0.4
        self.Y_2 = 2
        self.f_p = 1.0
        self.P_1 = P(self.f_p, self.X_1, self.F_a1, self.Y_1, self.F_a2)
        self.P_2 = P(self.f_p, self.X_2, self.F_a1, self.Y_2, self.F_a2)
        print('由表查得：X_1 =', self.X_1, '，Y_1 =', self.Y_1,
              '\n         X_2 =', self.X_2, '，Y_2 =', self.Y_2,
              '轴承运转中有载荷稳定，按参考文献[2]书P：321表13-6查得，取 f_p = 1.0 滚动轴承当量动载荷P = f_p*(X*F_r+Y*F_a)',
              '\n所以P_1 =', self.P_1, 'N',
              '\n    P_2 =', self.P_2, 'N')
        self.epsilon = 10 / 3
        self.L_h = Lh(n, self.C, max(self.P_1, self.P_2), self.epsilon)
        if self.L_h > t:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', format(self.L_h, '.1E'),
                  'h > t\n由此可见，轴承满足寿命要求')
        else:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', format(self.L_h, '.1E'),
                  'h ≤ t\n由此可见，轴承不符合寿命要求!!!')


# 30309型圆锥滚子轴承
class RollingBearing_3:
    def __init__(self, F_AZ, F_AY, F_CZ, F_CY, F_r, n,
                 f_r1=6438.44, f_r2=1951.42, F_a1=597.28, t=7.2 * 10 ** 4):
        self.C = 108
        self.e = 0.35
        self.Y = 1.7
        # self.F_r1 = sqrt(F_CZ ** 2 + F_CY ** 2)
        # self.F_r2 = sqrt(F_AZ ** 2 + F_AY ** 2)
        self.F_r1 = f_r1
        self.F_r2 = f_r2
        self.F_ae = F_r
        self.F_d1 = f_r1 / (2 * self.Y)
        self.F_d2 = f_r2 / (2 * self.Y)
        self.F_a1 = self.F_d1
        self.F_a2 = self.F_d1 - self.F_ae

        print('由轴的设计计算可知高速轴滚动轴承选用30309型圆锥滚子轴承，'
              '根据参考文献[1]P：76表6-7查得C=', self.C,
              'kN   e=', self.e,
              '  Y=', self.Y,
              '\n   F_r1 = √([F_CZ]^2+[F_CY]^2) =', self.F_r1,
              'N\n   F_r2 = √([F_AZ]^2+[F_AY]^2) =', self.F_r2, 'N')
        if self.F_d2 + self.F_ae < self.F_d1:
            print('由图：Fd_2+Fae < Fd_1\n∴轴承2压紧，轴承1放松'
                  '\n∴F_a1 = F_d1 =', self.F_a1, 'N',
                  '\n  F_a2 = F_d2 + F_ae =', self.F_a2, 'N')

        compare(num=1, F_a=self.F_a1, F_r=self.F_r1, e=self.e)
        compare(num=2, F_a=self.F_a2, F_r=self.F_r2, e=self.e)
        self.X_1 = 1
        self.Y_1 = 0
        self.X_2 = 0.4
        self.Y_2 = 1.7
        self.f_p = 1.0
        self.P_1 = P(self.f_p, self.X_1, self.F_r1, self.Y_1, self.F_r2)
        self.P_2 = P(self.f_p, self.X_2, self.F_r1, self.Y_2, self.F_r2)
        print('由表查得：X_1 =', self.X_1, '，Y_1 =', self.Y_1,
              '\n         X_2 =', self.X_2, '，Y_2 =', self.Y_2,
              '轴承运转中有载荷稳定，按参考文献[2]书P：321表13-6查得，取 f_p = 1.0 滚动轴承当量动载荷P = f_p*(X*F_r+Y*F_a)',
              '\n所以P_1 =', self.P_1, 'N',
              '\n    P_2 =', self.P_2, 'N')
        self.epsilon = 10 / 3
        self.L_h = Lh(n, self.C, max(self.P_1, self.P_2), self.epsilon)
        if self.L_h > t:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', format(self.L_h, '.1E'),
                  'h > t\n由此可见，轴承满足寿命要求')
        else:
            print('计算轴承寿命：对于圆锥滚子轴承ε =', self.epsilon,
                  '\n只需校核受力大的轴承，所以 L_h =', format(self.L_h, '.1E'),
                  'h ≤ t\n由此可见，轴承不符合寿命要求!!!')


if __name__ == '__main__':
    console = Console()
    console.print("九、滚动轴承的校核", style="red")
    console.print("（一）高速轴上的轴承", style='#FF6100')
    rolling_bearing_1 = RollingBearing_1(F_r=108.49, n=1440, t=36000)
    console.print("（二）中速轴上的轴承", style='#FF6100')
    rolling_bearing_2 = RollingBearing_2(F_r=700.75, n=480, t=36000)
    console.print("（三）低速轴上的轴承", style='#FF6100')
    rolling_bearing_3 = RollingBearing_3(n=96, F_AZ=199.6, F_AY=-1382.6, F_CZ=55.8, F_CY=6438.2,
                                         F_r=648.71)
