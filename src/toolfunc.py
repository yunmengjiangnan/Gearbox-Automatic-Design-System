# encoding:utf-8
# @Time : 2022/1/16 17:35
# @Author : Mahx2019

import math



# 根据已知两点坐标，求过这两点的直线方程的 y = -a/b*x - c/b：
def resLinerFunc(p1x, p1y, p2x, p2y, plz):
    '''
    parms:
    p1x => 第一个点x坐标值
    p1y => 第一个点y坐标值
    p2x => 第二个点x坐标值
    p2y => 第二个点y坐标值
    plz => 所求点已知的x坐标值
    return => 所求点y坐标值
    '''
    sign = 1
    a = p2y - p1y
    if a < 0:
        sign = -1
        a = sign * a
    b = sign * (p1x - p2x)
    c = sign * (p1y * p2x - p1x * p2y)
    def resplz(a,b,c,plz):
        return plz*a/b*-1 + c/b*-1
    return resplz(a,b,c,plz)
