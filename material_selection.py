# encoding:utf-8
# @Time : 2022/1/16 12:15
# @Author : Mahx2019

'''
相关的金属材料的选择部分

材料的介绍：
具体常用材料详见material.png内容

正火后和调质处理后的钢材料的区别：
调质处理后的力学性能与正火相比，不仅强度高，而且塑性和韧性也较好

最最最常用的材料：
45,40Cr,20Cr,20CrMnTi,

上述材料的具体参数：
材料名  热处理方法     强度极限（sigma_s/MPa）
45钢（调质）                650
45钢（正火）                580
20Cr（渗碳后淬火）          650
40Cr（调质）                700
20CrMnTi（渗碳后淬火）      1100
'''
from src.toolfunc import resLinerFunc
from src.parameters_list import *



class MS:
    '''
    材料选择的类
    MS:Material Selection
    self.__materialBox:最好使用的材料及参数，['代号名','材料名','强度极限','最小硬度','最大硬度']
    self.name:材料名称
    self.sigma_s:材料强度极限

    '''
    __material = input(
'''材料的选择：
   <编号> <材料名称>
    M0:   45钢（调质）
    M1:   45钢（正火）
    M2:   20Cr（渗碳后淬火）
    M3:   40Cr（调质）
    M4:   20CrMnTi（渗碳后淬火）
请键入编号：''')

    __materialBox = [
        ['M0','45钢（调质）',650,217,255],
        ['M1','45钢（正火）',580,162,217],
        ['M2','20Cr（渗碳后淬火）',650,300,300],
        ['M3','40Cr（调质）',700,241,286],
        ['M4','20CrMnTi（渗碳后淬火）',1100,300,300]
    ]
    name = ''
    sigma_s = 0
    hardnessMin = 0
    hardnessMax = 0

    def __init__(self):

        for i in range(len(self.__materialBox)):
            if self.__materialBox[i][0] == self.__material:
                self.name, self.sigma_s = self.__materialBox[i][1], self.__materialBox[i][2]
                self.hardnessMin,self.hardnessMax = self.__materialBox[i][3], self.__materialBox[i][4]

        if self.name == '':
            return print('请输入正确的编号！')

        '''
        配对两轮齿面硬度差在30~50HBW或更多
        此部分为齿面接触疲劳极限部分
        '''
        self.hardness = int(input('选择在 {} HBW ~ {} HBW的硬度：'.format(self.hardnessMin,self.hardnessMax)))
        

