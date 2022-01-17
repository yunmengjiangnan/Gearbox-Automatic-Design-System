# -*- coding = utf-8 -*-
# @Time : 2022/1/17 11:09
# @Author : xzh
# @File : 优化.py
# @Software: PyCharm
from math import pi, cos, tan
from rich import print
# from rich.console import Console
import numpy as np


class HelicalSpurGear:
    class DesignAccordingToToothSurfaceContactStrength:
        def __init__(self, i_2, T_2, n_2):
            self.Z_1 = 20  # 小齿轮齿数
            self.mu = i_2  # 齿数比
            self.Z_2 = self.mu * self.Z_1  # 大齿轮齿数
            self.K_t = 1.6  # 载荷系数
            self.T_2 = T_2  # 斜齿圆柱齿轮的输入转矩T
            self.phi_d = 1.0  # 斜齿圆柱齿轮传动的齿宽系数
            self.epsilon_alpha1 = 0.76  # 端面重合度
            self.epsilon_alpha2 = 0.90  # 端面重合度
            self.epsilon_alpha = self.epsilon_alpha1 + self.epsilon_alpha2
            self.Z_E = 189.8  # 弹性影响系数
            self.Z_H = 2.433  # 区域系数
            self.sigma_Hlim1 = 580  # 小锥齿轮的接触疲劳强度极限
            self.sigma_Hlim2 = 540  # 大锥齿轮的接触疲劳强度极限
            self.N_1 = 60 * n_2 * 16 * 300 * 15  # 小锥齿轮的应力循环次数
            self.N_2 = self.N_1 / i_2  # 大锥齿轮的应力循环次数
            self.K_HN1 = 0.97  # 接触疲劳寿命系数
            self.K_HN2 = 0.98
            self.S = 1  # 安全系数
            self.sigma_H1 = (self.K_HN1 * self.sigma_Hlim1) / self.S  # 小锥齿轮的许用接触应力
            self.sigma_H2 = (self.K_HN2 * self.sigma_Hlim2) / self.S  # 大锥齿轮的许用接触应力
            self.sigma_H = max(self.sigma_H1, self.sigma_H2)  # 取两者许用接触应力较大值
            # 计算小齿轮的分度圆直径d_1t
            self.d_1t_min = np.cbrt(
                (2 * self.K_t * self.T_2) / (self.phi_d * self.epsilon_alpha) * (self.mu + 1) / self.mu * (
                            self.Z_H * self.Z_E / self.sigma_H))
            print('小齿轮分度圆直径：d_1t ≥', self.d_1t_min)
            self.v = (pi * self.d_1t_min * n_2) / 60 / 1000
            print('圆周速度v =', self.v)
            self.b = self.phi_d * self.d_1t_min
            self.beta = 14 * pi / 180
            self.m_nt = (self.d_1t_min * cos(self.beta)) / self.Z_1
            self.h = 2.25 * self.m_nt
            self.b_h = self.b / self.h
            self.epsilon_beta = 0.318 * self.phi_d * self.Z_1 * tan(self.beta)
            K_A = 1.00
            K_V = 1.08
            K_Halpha = K_Falpha = 1.2
            K_Hbeta = 1.417
            K_Fbeta = 1.28
            self.K = K_A * K_V * K_Hbeta * K_Halpha
            self.d_1 = self.d_1t_min * np.cbrt(self.K / self.K_t)
            self.m_n = (self.d_1 * cos(self.beta)) / self.Z_1

    # 3、按齿根弯曲强度设计
    class CheckToothRootBendingStrength:
        def __init__(self, i_2):
            self.Z_1 = 20  # 小齿轮齿数
            self.mu = i_2  # 齿数比
            self.Z_2 = self.mu * self.Z_1  # 大齿轮齿数
            self.beta = 14 * pi / 180
            self.K_A = 1.00
            self.K_v = 1.08
            self.K_Halpha = self.K_Falpha = 1.2
            self.K_Hbeta = 1.417
            self.K_Fbeta = 1.28
            self.K = self.K_A * self.K_v * self.K_Fbeta * self.K_Falpha
            self.sigma_FE1 = 400
            self.sigma_FE2 = 380
            self.K_FN1 = 0.88
            self.K_FN2 = 0.90
            self.S = 1.4
            self.sigma_F1 = (self.K_FN1 * self.sigma_FE1) / self.S
            self.sigma_F2 = (self.K_FN2 * self.sigma_FE2) / self.S
            self.Y_beta = 0.88
            self.Z_v1 = self.Z_1 / cos(self.beta) ** 3
            self.Z_v2 = self.Z_2 / cos(self.beta) ** 3
            Y_Fa1 = 2.72
            Y_Fa2 = 2.17
            Y_Sa1 = 1.57
            Y_Sa2 = 1.80
            self.YFa1YSa1_sigmaF1 = Y_Fa1 * Y_Sa1 / self.sigma_F1
            self.YFa2YSa2_sigmaF2 = Y_Fa2 * Y_Sa2 / self.sigma_F2
            print('YFa1YSa1_phiF1 =', self.YFa1YSa1_sigmaF1,
                  '\nYFa2YSa2_phiF2 =', self.YFa2YSa2_sigmaF2)
            if self.YFa1YSa1_sigmaF1 > self.YFa2YSa2_sigmaF2:
                # Y_Fa = Y_Fa1
                # Y_Sa = Y_Sa1
                # sigma_F = self.sigma_F1
                self.YFaYSa_sigmaF = self.YFa1YSa1_sigmaF1
                print('YFa1YSa1_phiF1 > YFa2YSa2_phiF2小齿轮数值较大')
            else:
                # Y_Fa = Y_Fa2
                # Y_Sa = Y_Sa2
                # sigma_F = self.sigma_F2
                self.YFaYSa_sigmaF = self.YFa2YSa2_sigmaF2
                print('YFa1YSa1_phiF1 ≤ YFa2YSa2_phiF2大齿轮数值较大')
