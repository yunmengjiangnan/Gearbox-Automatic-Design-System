# -*- coding = utf-8 -*-
# @Time : 2022/1/19 14:35
# @Author : xzh
# @File : main.py
# @Software: PyCharm

import numpy as np
from math import pi, atan, cos, tan
from rich import print
from rich.console import Console

# 实例化一个输出控制端
console = Console()


class Axis:
    def __init__(self):
        self.P_1 = 3.50
