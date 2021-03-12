'''
Author: your name
Date: 2020-10-20 16:18:38
LastEditTime: 2020-10-23 15:05:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第四次作业/答案/excise1.py
'''

'''
1. 输入的三角形边长应该用浮点数储存，因为边长不一定是整数
2. 三角形的性质：任意两边长度之和大于第三边，并且边长只能为正数
'''
a = float(input("num1:"))
b = float(input("num2:"))
c = float(input("num3:"))

if (a+b > c and a+c > b and c+b > a and a > 0 and b > 0 and c > 0):
    print("Triangle!")
else:
    print("Error!")
