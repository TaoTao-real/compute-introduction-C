'''
Author: your name
Date: 2020-12-11 10:42:29
LastEditTime: 2020-12-11 10:58:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第五次作业/e1.py
'''

space = '       '
for i in range(1,9):
    print((8-i)*space, end = '')
    for j in range(1,i+1):
        if i*j<10:
            print(f"{j}*{i}= {i*j}",end=" ")
        else:
            print(f"{j}*{i}={i*j}",end=" ")
    print()