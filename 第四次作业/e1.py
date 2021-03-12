'''
Author: your name
Date: 2020-12-11 09:30:58
LastEditTime: 2020-12-11 09:33:53
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第四次作业/e1.py
'''
x=int(input("请输入一个数"))
y=int(input())
z=int(input())
if x+y>z and x+z>y and y+z>x:
    print("Triangle")
else:
    print("Error")
    