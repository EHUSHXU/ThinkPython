# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:47:29 2022

@author: 徐湖山
"""
#%% 练习2-1
# 1. 42=n是不合法的，会报错：SyntaxError: cannot assign to literal。无法给数值型数据赋值。
# 2. x = y =1 是合法的。x,y都被赋值为1.
# 3. python语句后加分号，不会报错，但是是多余的。
# 4. python语句后加句号会报错。因为python中句号有特殊的调用作用。
# 5. 在python中无法用xy表示两个变量相乘。会报错：NameError: name 'xy' is not defined。程序会任务xy是一个变量名。

#%%

import math
def volume(r):
    return (4/3)*math.pi*r**3

def book_price(n):

    return round((n*24.95*0.6 + n*3+(n-1)*0.75),3)

def count_minute():
    return ((6+10/60)*1.6 + (4+30/60)*4.8)
if __name__ == '__main__':
    r = 5
    print(('半径为{}的球体体积是{}').format(r,round(volume(r)),3))
    n = 60
    print(('{}本书的总价格是{}美元').format(n,book_price(n)))
    print(("返回时间为{}点{}分").format(int(6+(52+count_minute())//60),int((52+count_minute()) % 60)))

# %%
