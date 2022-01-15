# -*- coding = utf-8 -*-
# @Time : 2022/1/15 21:26
# @Author : xzh
# @File : gear_drive.py
# @Software: PyCharm
import numpy as np

print('#########六、齿轮传动的设计计算#########')
# 一、高速级锥齿轮传动：
# 1、选定齿轮类型、精度等级、材料及齿数(略)
# 2、按齿面接触强度设计
print('######(一)高速级锥齿轮传动：########'
      '\n#####1)确定公式的各计算数值#####')
K_t = 2.06  # 载荷系数
phi_R = 1 / 3  # 圆锥齿轮传动的齿宽系数
Z_1 = 20  # 小齿轮齿数
mu = i_1  # 齿数比
Z_2 = Z_1 * mu  # 大齿轮齿数
Z_E = 189.8  # 弹性影响系数
sigma_Hlim1 = 580  # 小锥齿轮的接触疲劳强度极限
sigma_Hlim2 = 540  # 大锥齿轮的接触疲劳强度极限
N_1 = 60 * n_1 * 1 * 16 * 300 * 15  # 小锥齿轮的应力循环次数
N_2 = N_1 / i_1  # 大锥齿轮的应力循环次数
K_HN1 = 0.90  # 接触疲劳寿命系数
K_HN2 = 0.95
S = 1.0  # 安全系数
sigma_H1 = (K_HN1 * sigma_Hlim1) / S  # 小锥齿轮的许用接触应力
sigma_H2 = (K_HN2 * sigma_Hlim2) / S  # 大锥齿轮的许用接触应力
sigma_H = max(sigma_H1, sigma_H2)  # 取两者许用接触应力较大值
d_1t_min = 2.93**2 * np.sqrt((Z_E / sigma_H) ** 2 * (K_t * T_1) / (phi_R * (1 - 0.5 * phi_R) ** 2 * mu))  # 求小锥齿轮分度圆直径
print('小齿轮分度圆直径：d_1t ≥', d_1t_min)
# 2)调整小齿轮分度圆直径
print('#####2)调整小齿轮分度圆直径#####')
d_m1 = d_1t_min * (1 - 0.5 * phi_R)
print('d_m1 =', d_m1)
v_m1 = (pi * d_m1 * n_1) / (60 * 1000)
print('圆周速度：v_m1 =', v_m1)
u = 3
R = d_1t_min * (u ** 2 + 1) ** 0.5 / 2
print('锥距：R =', R)
b = R * phi_R
print('齿宽：b =', b)
d_m = d_m1
phi_d = b / d_m
print('当量齿轮的齿宽系数：φ_d', phi_d)
# 3）计算载荷系数
print('########3）计算载荷系数########')
K_A = 1.00
v_m1 = 4.02
K_V = 1.12
K_Halpha = K_Falpha = 1
# K_Hbeta = 1.248
K_Hbeta = K_Fbeta = 1.248
K = K_A * K_V * K_Hbeta * K_Halpha
print('载荷系数：K =', K)
d_1 = d_1t_min * np.cbrt(K / K_t)
print('按实际载荷系数校正所算得的d_1 =', d_1)
m = d_1 / Z_1
print('大端模数：m =', m)
m = round(d_1 / Z_1)
print('取标准值', m)
# 3、校核齿根弯曲强度
print('##########3、校核齿根弯曲强度########')
# 1）确定公式中各计算数值
print('#####1）确定公式中各计算数值#####')
K = K_A * K_V * K_Fbeta * K_Falpha
phi_FE1 = 400
phi_FE2 = 380
K_FN1 = 0.88
K_FN2 = 0.90
S = 1.4
sigma_F1 = (K_FN1 * phi_FE1) / S
sigma_F2 = (K_FN2 * phi_FE2) / S
print('弯曲疲劳许用应力：[σ_F]_1 =', sigma_F1,
      '\n弯曲疲劳许用应力：[σ_F]_2 =', sigma_F2)
delta_1 = math.atan(1 / u) * 180 / pi
delta_2 = 90 - delta_1
print('分锥角：δ_1 =', delta_1,
      '\n分锥角：δ_2 =', delta_2)
Z_v1 = Z_1 / cos(delta_1 * pi / 180)
Z_v2 = Z_2 / cos(delta_2 * pi / 180)
print('当量齿数：Z_v1 ≈', Z_v1,
      '\n当量齿数：Z_v2 ≈', Z_v2)
Y_Fa1 = 2.76
Y_Fa2 = 2.124
Y_Sa1 = 1.56
Y_Sa2 = 1.86
YFa1YSa1_sigmaF1 = Y_Fa1 * Y_Sa1 / sigma_F1
YFa2YSa2_sigmaF2 = Y_Fa2 * Y_Sa2 / sigma_F2
print('YFa1YSa1_phiF1 =', YFa1YSa1_sigmaF1,
      '\nYFa2YSa2_phiF2 =', YFa2YSa2_sigmaF2)
if YFa1YSa1_sigmaF1 > YFa2YSa2_sigmaF2:
    Y_Fa = Y_Fa1
    Y_Sa = Y_Sa1
    sigma_F = sigma_F1
    print('YFa1YSa1_phiF1 > YFa2YSa2_phiF2小齿轮数值较大')
else:
    Y_Fa = Y_Fa2
    Y_Sa = Y_Sa2
    sigma_F = sigma_F2
    print('YFa1YSa1_phiF1 ≤ YFa2YSa2_phiF2大齿轮数值较大')
# 2）代入数值计算
m_min = np.cbrt((4 * K * T_1) / (phi_R * (1 - 0.5 * phi_R) ** 2 * Z_1 ** 2 * (u ** 2 + 1)) * (Y_Fa * Y_Sa) / sigma_F)
print('m ≥', m_min)
Z_1 = round(d_1 / m)
Z_2 = u * Z_1
print('小齿轮齿数：Z_1 =', Z_1,
      '\n小齿轮齿数：Z_2 =', Z_2)
# ３）代入数值计算
d_1 = Z_1 * m
d_2 = Z_2 * m
print('分度圆直径：d_1 =', d_1,
      '\n分度圆直径：d_2 =', d_2)
R = d_1 * np.sqrt(mu**2 + 1) / 2
print('锥距：R =', R)
float_B = R * phi_R
B = round(float_B)
print('B =', float_B)
print('取整B =', B)
# B_1 =
