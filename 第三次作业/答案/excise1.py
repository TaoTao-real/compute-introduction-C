'''
Author: your name
Date: 2020-10-15 14:43:24
LastEditTime: 2020-12-11 09:16:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /计算概论C/作业/第三次作业/excise1.py
'''
a = int(input("输入起点："))
b = int(input("输入终点："))
if(a >= b or a < 0 or b < 0):
    print("ERROR")
else:
    sum = 0
    for i in range(a,b+1):
        sum+=i    
    print(sum)
