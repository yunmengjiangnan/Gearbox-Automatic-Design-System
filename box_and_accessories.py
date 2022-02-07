# -*- coding = utf-8 -*-
# @Time : 2022/2/3 16:38
# @Author : xzh
# @File : box_and_accessories.py
# @Software: PyCharm
from rich.console import Console

# 实例化一个输出控制端
console = Console()


class box:
    def __init__(self):
        console.print("参考参考文献[1]表11－１（铸铁减速器箱体结构尺寸），初步取如下尺寸：", style='#FF6100')
        self.delta = 8
        print('箱座壁厚:δ ≥ ', self.delta, 'mm，取δ ≥ ', self.delta, 'mm'
              '\n箱盖壁厚：δ_1 ≥ ', self.delta, 'mm，取δ_1 =', self.delta, 'mm'
              '\n箱体凸缘厚度：'
              '箱座b = 1.5δ =', self.delta * 1.5, 'mm，箱盖b_1 = 1.5δ =', self.delta * 1.5,
              '，箱底座b_2 = 2.5δ =', self.delta * 2.5, 'mm'
              '\n')
