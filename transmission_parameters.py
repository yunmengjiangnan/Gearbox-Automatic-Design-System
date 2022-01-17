# -*- coding = utf-8 -*-
# @Time : 2022/1/15 21:01
# @Author : xzh
# @File : transmission_parameters.py
# @Software: PyCharm
import motor as mt
from rich import print
# from rich.console import Console


# 1、各轴转速n（r/min）
def Shaft_Speed(I_1, I_2):
    n_1 = 1440
    n_2 = n_1 / I_1
    n_3 = n_2 / I_2
    print('n_1 =', n_1,
          '\nn_2 =', n_2,
          '\nn_3 =', n_3)
    return n_1, n_2, n_3


# 2、各轴输入功率P（kW）
def Input_Power(P_D):
    eta_1 = 0.96
    eta_2 = 0.98
    eta_4 = 0.99
    eta_5 = 0.98
    P_1 = P_D * eta_4 * eta_5
    P_2 = P_1 * eta_1 * eta_5
    P_3 = P_2 * eta_2 * eta_5
    print('P_1 =', P_1, 'kW'
                        '\nP_2 =', P_2, 'kW'
                                        '\nP_3 =', P_3, 'kW')
    return P_1, P_2, P_3


# 3、各轴输入转矩T（N•ｍ）
def Input_Torque(P_1, P_2, P_3, n_1, n_2, n_3):
    T_1 = 9550 * P_1 / n_1
    T_2 = 9550 * P_2 / n_2
    T_3 = 9550 * P_3 / n_3
    print('T_1 =', T_1, 'N·m',
          '\nT_2 =', T_2, 'N·m',
          '\nT_3 =', T_3, 'N·m')
    return T_1, T_2, T_3


if __name__ == '__main__':
    F = 5
    v = 0.8
    i_1 = 2
    i_2 = 6
    # 1、工作机输出功率P_W
    P_W = mt.Output_Power(F, v)
    # 3、传动效率η
    eta = mt.Transmission_Efficiency()
    P_d = mt.Input_Power(P_W, eta)
    # 1、各轴转速n（r/min）
    n_1, n_2, n_3 = Shaft_Speed(i_1, i_2)
    # 2、各轴输入功率P（kW）
    P_1, P_2, P_3 = Input_Power(P_d)
    # 3、各轴输入转矩T（N•ｍ）
    T_1, T_2, T_3 = Input_Torque(P_1, P_2, P_3, n_1, n_2, n_3)
