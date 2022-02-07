# -*- coding = utf-8 -*-
# @Time : 2022/2/3 13:35
# @Author : xzh
# @File : key.py
# @Software: PyCharm
from rich.console import Console

# 实例化一个输出控制端
console = Console()


class high_speed_key:
    def __init__(self):
        console.print("1、与联轴器相连处的普通圆头平键：", style='yellow')
        print('轴的d = d_I_II =',
              '\n按参考文献[2]表6-2由轴的设计计算可知所选平键为按参考文献[2]公式6-1校核键连接强度的公式其中k=0.5h；l=L-b 强度满足，该键合理。')


if __name__ == '__main__':
    high_speed_key = high_speed_key()
