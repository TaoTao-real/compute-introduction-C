'''
Author: your name
Date: 2020-10-28 10:11:51
LastEditTime: 2020-11-03 12:57:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第五次作业/答案/excise3.py
'''
'''
1. 原理已经在群里告诉大家，可以自行证明
'''
def primeFactor(N):
    factors = []
    if(N < 2):
        return factors
    factor = 2
    while(N != 1):
        if(N % factor == 0):
            factors.append(factor)
            N = N//factor
        else:
            factor = factor+1
    return factors

num = int(input("num:"))
print(primeFactor(num))
