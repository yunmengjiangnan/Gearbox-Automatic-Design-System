# encoding:utf-8


"""说明：
一些实际中需要查表的参数，
简化为通过近似成函数（一次、二次等）求得。

这里记录：可以表示为一次函数的 => 两个点的坐标
"""

'''
品质标记：
    E：高等品质
    Q：一般品质
    L：下等品质
'''

# 齿轮的接触疲劳极限，直线求 sigma_Hlim

# 正火处理的结构钢zj_[?](45钢（正火）)
Hzj = [
    [150, 475, 200, 502],
    [150, 345, 200, 395],
    [150, 345, 200, 395]
]

# 调质处理钢：碳钢tg_[?](45钢（调质）,40Cr（调质）)
Htg = [
    [150, 560, 200, 610],
    [150, 500, 200, 555],
    [150, 425, 200, 490]
]

# 渗碳淬火钢(20Cr（渗碳后淬火）,20CrMnTi（渗碳后淬火）)
Hscg = [
    [150, 1650, 650, 1650],
    [150, 1500, 500, 1500],
    [130, 1300, 300, 1300]
]

# 齿轮的弯曲疲劳极限

# 正火处理的结构钢zj_[?](45钢（正火）)
Fzj = [
    [150, 410, 200, 450],
    [150, 280, 200, 320],
    [150, 280, 200, 320]
]

# 调质处理钢：碳钢tg_[?](45钢（调质）,40Cr（调质）)
Ftg = [
    [150, 495, 200, 530],
    [150, 400, 200, 445],
    [150, 280, 200, 310]
]

# 渗碳淬火钢(20Cr（渗碳后淬火）,20CrMnTi（渗碳后淬火）)
Hscg = [
    [130, 930, 930, 930],
    [130, 830, 830, 830],
    [130, 530, 530, 530]
]
