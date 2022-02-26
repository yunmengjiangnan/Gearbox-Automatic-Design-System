# -*- coding = utf-8 -*-
# @Time : 2022/2/23 20:23
# @Author : xzh
# @File : end_cap.py
# @Software: PyCharm
from rich.console import Console

# 实例化一个输出控制端
console = Console()


# 轴承外径对应螺钉直径和个数
def screw(D):
    table_11_10 = [(6, 4),
                   (8, 4),
                   (10, 6)]
    if 45 <= D <= 65:
        return table_11_10[0]
    elif 70 <= D <= 100:
        return table_11_10[1]
    elif 110 <= D <= 140:
        return table_11_10[2]
    elif 150 <= D <= 230:
        console.print('轴承外径范围在150~230，请酌情从12~16中任取一个螺钉直径，螺钉数为6', style='red')
        d_3 = input('请输入选取直径（12~16）：')
        return d_3, 6
    else:
        return None


# 轴承盖设计
class BearingCap:
    def __init__(self, D):
        self.D = D
        self.d_3, self.screw_num = screw(self.D)
        self.e = 1.2 * self.d_3
        self.d_0 = self.d_3 + 1
        self.D_0 = self.D + 2.5 * self.d_3
        self.D_2 = self.D_0 + 2.5 * self.d_3
        self.D_4 = self.D - 10
        self.D_6 = self.D - 3
        self.e_1 = self.e
        self.D_5 = self.D_0 - 3 * self.d_3
        self.m = 9


# 套杯设计
class Cup:
    def __init__(self, D_a, D, d_3):
        self.s_4 = 10
        self.s_3 = 10
        self.e_4 = 10
        self.D_1 = D_a
        self.D_0 = D + 2 * self.s_3 + 2.5 * d_3
        self.D_2 = self.D_0 + 2.5 * d_3
        self.D_5 = self.D_0 - 3 * d_3


class HighSpeedEndCap:
    def __init__(self, D, D_a):
        self.bearing_cap = BearingCap(D)
        print('由于轴承外径D=', self.bearing_cap.D,
              'mm\n螺钉直径d_3=', self.bearing_cap.d_3,
              'mm螺钉数为', self.bearing_cap.screw_num,
              '，轴承盖凸缘厚度e=1.2*d_3=', self.bearing_cap.e,
              'mm\n螺钉孔直径d_0=d_3+1=', self.bearing_cap.d_0,
              'mm，螺钉分布圆直径\nD_0=D+2.5*d_3=', self.bearing_cap.D_0,
              'mm\n轴承盖凸缘直径D_2=D_0+2.5d_3=', self.bearing_cap.D_2,
              'mm，D_4=D-10=', self.bearing_cap.D_4,
              'mm\nD_6=D-3=', self.bearing_cap.D_6,
              'mm，e_1=e=', self.bearing_cap.e_1,
              'mm，D_5=D_0-3*d_3=', self.bearing_cap.D_5,
              'mm\nm=', self.bearing_cap.m, 'mm')
        self.cup = Cup(D_a=D_a, d_3=self.bearing_cap.d_3, D=D_a)  # D=D_a还有点疑问，等debug
        console.print('套杯：', style='green')
        print('参照参考文献P172表11—12，并根据轴的几何尺寸，取如下参数，\n套杯内缘厚S_4=', self.cup.s_4,
              'mm，壁厚S_3=', self.cup.s_3,
              'mm，外缘厚e_4=', self.cup.e_4,
              'mm，\n根据轴承轴向定位要求，取D_1=', self.cup.D_1,
              'mm，\n螺钉分布圆直径D_0=D+2S_3+2.5d_3=', self.cup.D_0,
              'mm，\n轴承盖凸缘直径D_2=D_0+2.5d_3=', self.cup.D_2,
              'mm，\nD_5=D_0-3d_3=', self.cup.D_5, 'mm。')


class MediumSpeedEndCap:
    def __init__(self, D):
        self.bearing_cap = BearingCap(D)
        print('由于轴承外径D=', self.bearing_cap.D,
              'mm\n螺钉直径d_3=', self.bearing_cap.d_3,
              'mm螺钉数为', self.bearing_cap.screw_num,
              '，轴承盖凸缘厚度e=1.2*d_3=', self.bearing_cap.e,
              'mm\n螺钉孔直径d_0=d_3+1=', self.bearing_cap.d_0,
              'mm，螺钉分布圆直径\nD_0=D+2.5*d_3=', self.bearing_cap.D_0,
              'mm\n轴承盖凸缘直径D_2=D_0+2.5d_3=', self.bearing_cap.D_2,
              'mm，D_4=D-10=', self.bearing_cap.D_4,
              'mm\nD_6=D-3=', self.bearing_cap.D_6,
              'mm，e_1=e=', self.bearing_cap.e_1,
              'mm，D_5=D_0-3*d_3=', self.bearing_cap.D_5,
              'mm\n从任务书设计简图中可以看出左右两个轴承盖都应该设计成闷盖。左边的轴承盖取b=5,h=5,右边的轴承盖b=5,h=10。')


class LowSpeedEndCap:
    def __init__(self, D):
        self.bearing_cap = BearingCap(D)
        print('由于轴承外径D=', self.bearing_cap.D,
              'mm\n螺钉直径d_3=', self.bearing_cap.d_3,
              'mm螺钉数为', self.bearing_cap.screw_num,
              '，轴承盖凸缘厚度e=1.2*d_3=', self.bearing_cap.e,
              'mm\n螺钉孔直径d_0=d_3+1=', self.bearing_cap.d_0,
              'mm，螺钉分布圆直径\nD_0=D+2.5*d_3=', self.bearing_cap.D_0,
              'mm\n轴承盖凸缘直径D_2=D_0+2.5d_3=', self.bearing_cap.D_2,
              'mm，D_4=D-10=', self.bearing_cap.D_4,
              'mm\nD_6=D-3=', self.bearing_cap.D_6,
              'mm，e_1=e=', self.bearing_cap.e_1,
              'mm，D_5=D_0-3*d_3=', self.bearing_cap.D_5,
              'mm\n从任务书设计简图中可以看出左右两个轴承盖都应该设计成闷盖。\n左边的轴承盖取b=5,h=5,右边的轴承盖b=5,h=10。')
