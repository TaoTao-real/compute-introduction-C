'''
Author: your name
Date: 2020-10-28 09:40:00
LastEditTime: 2020-11-03 12:55:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第五次作业/答案/excise1.py
'''
'''
1. 每一个乘法项占用7个单元格
2. 每一行计算之前要插入对应的空格，规律递减
'''
prespace = " "*7
for i in range(1, 10):
    print(prespace*(9-i), end="")
    for j in range(1, i + 1):
        if(i*j < 10):
            print(f"{j}*{i}={j*i} ", end=" ")
        else:
            print(f"{j}*{i}={j*i}", end=" ")
    print()
