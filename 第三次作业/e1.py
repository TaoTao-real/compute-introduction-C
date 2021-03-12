'''
Author: your name
Date: 2020-12-11 09:20:26
LastEditTime: 2020-12-11 09:29:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第三次作业/e1.py
'''
x=int(input("please input num1:"))
y=int(input("please input num2:"))
sum=0
if 0<x<y:
    for i in range(x,y+1):
        sum=sum+i
    print(sum)
else:
    print("ERROR")