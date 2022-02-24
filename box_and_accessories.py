# -*- coding = utf-8 -*-
# @Time : 2022/2/3 16:38
# @Author : xzh
# @File : box_and_accessories.py
# @Software: PyCharm
from rich.console import Console

# 实例化一个输出控制端
console = Console()


def bolt(d_f_float):
    d_f_list_preferred = (3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 30, 36)
    d_f_list = (3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 27, 30, 36)
    d_f = 0
    for i in d_f_list_preferred:
        if d_f_list_preferred[i] > d_f_float:
            if d_f_list_preferred[i] - d_f_float > d_f_float - d_f_list_preferred[i - 1]:
                d_f = d_f_list_preferred[i - 1]
                break
            else:
                d_f = d_f_list_preferred[i]
                break
    return d_f


def number_of_anchor_screws(a):
    if a <= 250:
        n = 4
    elif 500 > a > 250:
        n = 6
    else:
        n = 8
    return n


def structural_dimensions_of_bosses_and_flanges(d_1):
    table_11_2 = {'6': (12, 10),
                  '8': (13, 11),
                  '10': (16, 14),
                  '12': (18, 16),
                  '14': (20, 18),
                  '16': (22, 20),
                  '18': (24, 22),
                  '20': (26, 24),
                  '22': (30, 26),
                  '24': (34, 28),
                  '27': (36, 32),
                  '30': (40, 34)}
    return table_11_2[str(int(d_1))]


def hole_cover(a_sum):
    table_11_4 = [(140, 125, 120, 105, 7, 8, 4, 5),
                  (180, 165, 140, 125, 7, 8, 4, 5),
                  (220, 190, 160, 130, 11, 8, 4, 15),
                  (270, 240, 180, 150, 11, 8, 6, 15)]
    if a_sum <= 250:
        return table_11_4[0]
    elif 250 < a_sum <= 425:
        return table_11_4[1]
    elif 425 < a_sum <= 500:
        return table_11_4[2]
    elif 500 < a_sum <= 650:
        return table_11_4[3]
    else:
        pass


def vent_plug(d):
    table_11_5 = {'12': (18, 16.5, 14, 19, 10, 2, 4),
                  '16': (22, 19.6, 17, 23, 12, 2, 5),
                  '20': (30, 25.4, 22, 28, 15, 4, 6),
                  '22': (32, 25.4, 22, 29, 15, 4, 7),
                  '27': (38, 31.2, 27, 34, 18, 4, 8),
                  '30': (42, 36.9, 32, 36, 18, 4, 8),
                  '33': (45, 36.9, 32, 38, 20, 4, 8),
                  '36': (50, 41.6, 36, 46, 25, 5, 8)}
    return table_11_5[str(int(d))]


class box:
    def __init__(self, a):
        console.print("参考参考文献[1]表11－１（铸铁减速器箱体结构尺寸），初步取如下尺寸：", style='#FF6100')
        if 0.025 * a + 3 < 8:
            self.delta = 8
        else:
            self.delta = 0.025 * a + 3
        if 0.02 * a + 3 < 8:
            self.delta_1 = 8
        else:
            self.delta_1 = 0.02 * a + 3
        self.b = 1.5 * self.delta
        self.b_1 = 1.5 * self.delta
        self.b_2 = 2.5 * self.delta
        self.m = 0.85 * self.delta
        self.m_1 = 0.85 * self.delta
        self.d_f_float = 0.036 * a + 12
        self.d_f = bolt(self.d_f_float)
        self.n = number_of_anchor_screws(a)
        self.d_1 = 0.75 * self.d_f
        self.d_2 = round(0.55 * self.d_f)
        self.l = (150, 200)
        self.d_3 = round(0.45 * self.d_f)
        self.d_4 = round(0.35 * self.d_f)
        self.d = round(0.75 * self.d_2)
        self.C_1, self.C_2 = structural_dimensions_of_bosses_and_flanges(self.d_1)

        console.print('箱座壁厚:', style='yellow')
        print('δ ≥ ', self.delta, 'mm，取δ ≥ ', self.delta, 'mm')
        console.print('箱盖壁厚：', style='yellow')
        print('δ_1 ≥ ', self.delta_1, 'mm，取δ_1 =', self.delta_1, 'mm')
        console.print('箱体凸缘厚度：', style='yellow')
        print('箱座b = 1.5δ =', self.b, 'mm，箱盖b_1 = 1.5δ =', self.b_1, 'mm，箱底座b_2 = 2.5δ =', self.b_2, 'mm')
        console.print('加强肋厚度：', style='yellow')
        print('箱座m = 0.85 δ = ', self.m, 'mm，箱盖m_1=0.85δ_1=', self.m_1, 'mm')
        console.print('地脚螺钉直径：', style='yellow')
        print('𝑑_𝑓=0.036a+12=', self.d_f_float,
              'mm，取𝑑_𝑓=', self.d_f,
              '𝑚𝑚，\n型号为：螺栓GB5782－86 M', self.d_f,
              '×60     采用标准弹簧垫圈，型号：垫圈GB93－87 18')
        console.print('地脚螺钉数目：', style='yellow')
        print('因a≤250mm，取n=', self.n, 'mm')
        console.print('轴承旁联接螺栓直径：', style='yellow')
        print('d_1=0.75d_f=', self.d_1,
              'mm\n型号为：螺栓GB5782－86 M', self.d_1,
              '×115   采用标准弹簧垫圈，型号：垫圈GB93－87 14')
        console.print('箱盖，箱座联接螺栓直径：', style='yellow')
        print('d_2=0.5d_f=', self.d_2,
              'mm\n型号为：螺栓GB5782－86 M', self.d_2,
              '×40    采用标准弹簧垫圈，型号：垫圈GB93－87 10')
        console.print('螺栓间距:', style='yellow')
        print('L≤150~200mm')
        console.print('观察孔盖螺钉直径:', style='yellow')
        print('d_4=', self.d_4, 'mm')


class accessories:
    def __init__(self, delta, delta_1, C_1, C_2, a, d):
        self.d = self.b = round(2.15 * delta_1)
        self.R = round(1.1 * self.d)
        self.e = round(0.9 * self.d)

        self.K = C_1 + C_2
        self.H = 0.8 * self.K
        self.h = 0.5 * self.H
        self.r = self.K / 6
        self.b = 2.15 * delta
        console.print('起重吊耳:', style='yellow')
        print('采用吊耳环，见参考文献P167表11-3'
              '\n取尺寸d=b=', self.d, 'mm，R=', self.R, 'mm，e=', self.e, 'mm')
        console.print('吊钩：', style='yellow')
        print('取尺寸K=', self.K,
              'mm,H=', self.H,
              'mm,h=', self.h,
              'mm,r=', self.r,
              'mm,b=', self.b,
              'mm\n其余尺寸参见装配图。')

        self.delta_1 = round(1.2 * delta)
        self.delta_2 = round(delta)
        console.print('参照参考文献[1]P89表7-9取油标管式游标。', style='yellow')
        console.print('齿轮顶圆至箱体内壁的距离：', style='yellow')
        print('△_1≥1.2δ，取△_1=', self.delta_1, 'mm,')
        console.print('齿轮端面至箱体内壁的距离：', style='yellow')
        print('△_2≥δ，取△_2=', self.delta_2, 'mm')
        console.print('窥视孔及视孔盖，参照参考文献P:167表11-4', style='yellow')
        self.hole_cover = hole_cover(a_sum=a)
        print('取l_1=', self.hole_cover[0],
              'mm,l_2=', self.hole_cover[1],
              'mm,b_1=', self.hole_cover[2],
              'mm,b_2=', self.hole_cover[3],
              'mm,δ=', self.hole_cover[6],
              'mm,R=', self.hole_cover[7], 'mm ')

        console.print('通气器用通气塞，查参考文献[1]表11－5，得以下数据：', style='yellow')
        self.vent_plug = vent_plug(d=d)
        print('取M', d,
              '，D =', self.vent_plug[0],
              'mm，D_1=', self.vent_plug[1],
              'mm，s=', self.vent_plug[2],
              '，L=', self.vent_plug[3],
              '，l=', self.vent_plug[4],
              '，a=', self.vent_plug[5],
              ' ，d1=', self.vent_plug[6], '。')
        console.print('启盖螺钉：', style='yellow')
        print('型号为：螺栓GB5782－86 M6×20')


