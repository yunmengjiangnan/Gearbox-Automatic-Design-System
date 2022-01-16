# encoding:utf-8
from src.parameters_list import *
from src.toolfunc import resLinerFunc, roundness
from material_selection import MS

ms1 = MS()
print(ms1.name)
print(ms1.sigma_s)
print(ms1.hardness)
sigma_Hlim = resLinerFunc(Fzj[0][0],Fzj[0][1],Fzj[0][2],Fzj[0][3],ms1.hardness)
print(sigma_Hlim)
print(roundness(sigma_Hlim))
