# -*- coding = utf-8 -*-
# @Time : 2022/1/15 20:11
# @Author : xzh
# @File : gear_ratio.py
# @Software: PyCharm

# 1、系统总传动比i
def Total_Gear_Ratio(N):
    i = 1440 / N
    print('系统总传动比i: ', i)
    return i


# 2、分配传动比(圆锥齿轮传动i_1/圆柱齿轮传动i_2/链传动i_3)
def Transmission_Ratio_Assignment(I, I_1, I_2):
    i_3 = I / I_1 / I_2
    print('圆锥齿轮传动i_1 =', I_1,
          '\n圆柱齿轮传动i_2 =', I_2,
          '\n链传动i_3 = ', i_3)
    return i_3


if __name__ == '__main__':
    n = 91.89158511750144
    # 1、系统总传动比i
    i = Total_Gear_Ratio(n)
    # 2、分配传动比(圆锥齿轮传动i_1/圆柱齿轮传动i_2/链传动i_3)
    i_3 = Transmission_Ratio_Assignment(i, 2, 6)
