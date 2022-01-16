# -*- coding = utf-8 -*-
# @Time : 2022/1/15 21:26
# @Author : xzh
# @File : gear_drive.py
# @Software: PyCharm
import numpy as np
from math import pi, atan, cos, tan
import sys
from prettytable import PrettyTable


# reload(sys)
# sys.setdefaultencoding('utf8')


# 六、齿轮传动的设计计算
class BevelGear:
    # 1、选定齿轮类型、精度等级、材料及齿数(略)
    # 2、按齿面接触强度设计
    class DesignAccordingToToothSurfaceContactStrength:
        # 1）确定公式中各计算数值
        def __init__(self, i_1, T_1, n_1):
            self.Z_1 = 20  # 小齿轮齿数
            self.mu = i_1  # 齿数比
            self.Z_2 = self.mu * self.Z_1  # 大齿轮齿数
            self.K_t = 2.06  # 载荷系数
            self.T_1 = T_1  # 锥齿轮的输入转矩T
            self.phi_R = 1 / 3  # 圆锥齿轮传动的齿宽系数
            self.Z_E = 189.8  # 弹性影响系数
            self.sigma_Hlim1 = 580  # 小锥齿轮的接触疲劳强度极限
            self.sigma_Hlim2 = 540  # 大锥齿轮的接触疲劳强度极限
            self.N_1 = 60 * n_1 * 1 * 16 * 300 * 15  # 小锥齿轮的应力循环次数
            self.N_2 = self.N_1 / i_1  # 大锥齿轮的应力循环次数
            self.K_HN1 = 0.90  # 接触疲劳寿命系数
            self.K_HN2 = 0.95
            self.S = 1.0  # 安全系数
            self.sigma_H1 = (self.K_HN1 * self.sigma_Hlim1) / self.S  # 小锥齿轮的许用接触应力
            self.sigma_H2 = (self.K_HN2 * self.sigma_Hlim2) / self.S  # 大锥齿轮的许用接触应力
            self.sigma_H = max(self.sigma_H1, self.sigma_H2)  # 取两者许用接触应力较大值
            # 求小锥齿轮分度圆直径
            self.d_1t_min = 2.93 ** 2 * np.sqrt(
                (self.Z_E / self.sigma_H) ** 2 * (self.K_t * T_1) / (
                        self.phi_R * (1 - 0.5 * self.phi_R) ** 2 * self.mu))
            print('小齿轮分度圆直径：d_1t ≥', self.d_1t_min)

        # 2)调整小齿轮分度圆直径
        def Tooth_Contact_Strength_Design(self, n_1):
            d_m1 = self.d_1t_min * (1 - 0.5 * self.phi_R)
            print('d_m1 =', d_m1)
            v_m1 = (pi * d_m1 * n_1) / (60 * 1000)
            print('圆周速度：v_m1 =', v_m1)
            u = 3
            R = self.d_1t_min * (u ** 2 + 1) ** 0.5 / 2
            print('锥距：R =', R)
            b = R * self.phi_R
            print('齿宽：b =', b)
            d_m = d_m1
            phi_d = b / d_m
            print('当量齿轮的齿宽系数：φ_d', phi_d)
            return R

        # 3）计算载荷系数
        def Load_Factor(self):
            K_A = 1.00
            # v_m1 = 4.02
            K_V = 1.12
            K_Halpha = 1
            K_Hbeta = 1.248
            K = K_A * K_V * K_Hbeta * K_Halpha
            print('载荷系数：K =', K)
            d_1 = self.d_1t_min * np.cbrt(K / self.K_t)
            print('按实际载荷系数校正所算得的d_1 =', d_1)
            m = d_1 / self.Z_1
            print('大端模数：m =', m)
            m = round(d_1 / self.Z_1)
            print('取标准值', m)
            return m, d_1

    # 3、校核齿根弯曲强度
    class CheckToothRootBendingStrength:
        # 1）确定公式中各计算数值
        def __init__(self, mu, Z_1, Z_2):
            self.Z_1 = Z_1
            self.Z_2 = Z_2
            self.mu = mu
            K_A = 1.00
            K_V = 1.00
            K_Fbeta = 1.12
            K_Falpha = 1.248
            self.K = K_A * K_V * K_Fbeta * K_Falpha
            self.phi_FE1 = 400
            self.phi_FE2 = 380
            self.K_FN1 = 0.88
            self.K_FN2 = 0.90
            self.S = 1.4
            self.sigma_F1 = (self.K_FN1 * self.phi_FE1) / self.S
            self.sigma_F2 = (self.K_FN2 * self.phi_FE2) / self.S
            print('弯曲疲劳许用应力：[σ_F]_1 =', self.sigma_F1,
                  '\n弯曲疲劳许用应力：[σ_F]_2 =', self.sigma_F2)
            self.delta_1 = atan(1 / self.mu) * 180 / pi
            self.delta_2 = 90 - self.delta_1
            print('分锥角：δ_1 =', self.delta_1,
                  '\n分锥角：δ_2 =', self.delta_2)
            Z_v1 = self.Z_1 / cos(self.delta_1 * pi / 180)
            Z_v2 = self.Z_2 / cos(self.delta_2 * pi / 180)
            print('当量齿数：Z_v1 ≈', Z_v1,
                  '\n当量齿数：Z_v2 ≈', Z_v2)
            Y_Fa1 = 2.76
            Y_Fa2 = 2.124
            Y_Sa1 = 1.56
            Y_Sa2 = 1.86
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

        # 2）代入数值计算
        def Substitution_Calculation_1(self, T_1, phi_R, d_1, m):
            m_min = np.cbrt(
                (4 * self.K * T_1) / (
                        phi_R * (1 - 0.5 * phi_R) ** 2 * self.Z_1 ** 2 * (self.mu ** 2 + 1)) * self.YFaYSa_sigmaF)
            print('m ≥', m_min)
            Z_1 = round(d_1 / m)
            Z_2 = self.mu * Z_1
            print('小齿轮齿数：Z_1 =', Z_1,
                  '\n小齿轮齿数：Z_2 =', Z_2)
            return m_min

        def Substitution_Calculation_2(self, m, phi_R):
            d_1 = self.Z_1 * m
            d_2 = self.Z_2 * m
            print('分度圆直径：d_1 =', d_1,
                  '\n分度圆直径：d_2 =', d_2)
            R = d_1 * np.sqrt(self.mu ** 2 + 1) / 2
            print('锥距：R =', R)
            float_B = R * phi_R
            B = round(float_B)
            print('B =', float_B)
            print('取整B =', B)
            B_1 = float(B) * (7 / 6)
            B_2 = B
            print('B_1 =', B_1,
                  '\nB_2 =', B_2)
            d_m1 = d_1 * (1 - (0.5 * phi_R))
            d_m2 = d_2 * (1 - (0.5 * phi_R))
            print('d_m1 =', d_m1,
                  '\nd_m2 =', d_m2)
            return d_m1, d_m2, d_2, B_1, B_2


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
                (2 * self.K_t * self.T_2) / (self.phi_d * self.epsilon_alpha) * (self.mu + 1) / self.mu * (self.Z_H * self.Z_E / self.sigma_H))
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
            K_v = 1.08
            K_Halpha = K_Falpha = 1.2
            K_Hbeta = 1.417

            self.K =


if __name__ == '__main__':
    bevel_gear_D = BevelGear.DesignAccordingToToothSurfaceContactStrength(i_1=2, T_1=30.595749463944532, n_1=1440)
    bevel_gear_D.Tooth_Contact_Strength_Design(n_1=1440)
    bevel_gear_D.Load_Factor()
    bevel_gear_C = BevelGear.CheckToothRootBendingStrength(Z_1=16, Z_2=48, mu=2)
    bevel_gear_C.Substitution_Calculation_1(T_1=30.595749463944532, phi_R=1 / 3, d_1=32.0042098044378, m=2)
    bevel_gear_C.Substitution_Calculation_2(m=2, phi_R=1 / 3)
