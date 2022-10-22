# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:47:29 2022

@author: 徐湖山
"""

#%% 练习1-1
# ....
# 1．会报语法错误：SyntaxError: Missing parentheses in call to 'print' 因为python3中print内容必须放在括号中。

# 2．会报语法错误：SyntaxError: EOL while scanning string literal 因为字符换内容必须放在完整的引号中。

# 3．数字前加正号不会报错，可以正常运行。如果是2++2，可以正确输出结果4.

# 4．python中数字前的前置0会报错：SyntaxError: leading zeros in decimal integer literals are not permitted。

# 5．如果在两个值之间不放任何操作符，会报错：SyntaxError: invalid syntax
# ....

#%% 练习1-2
def count_s(m,s):
    return s + m * 60

def conver2mile(km):
    return km / 1.61

def speed(s,km):
    return s/km

if __name__ == '__main__':
    # 请把函数调用放在这里
    s = count_s(42,42)
    km = 10
    mile = conver2mile(km)
    print(s)
    print(mile)
    sp = speed(s,km)
    print('平均速度是每千米{}分{}秒'.format(sp//60,round(sp%60,2)))
    print('平均速度是每小时{}千米'.format(round(km/s * 3600,2) ))

