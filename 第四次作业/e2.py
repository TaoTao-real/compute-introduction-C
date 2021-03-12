'''
Author: your name
Date: 2020-12-11 09:34:47
LastEditTime: 2020-12-11 09:52:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第四次作业/e2.py
'''
for i in range(1,10):
    for j in range(i,10):
        if i*j<10:
            print(f"{i}*{j}= {i*j}",end=" ")
        else:
            print(i,"*",j,"=",i*j,sep='',end=" ")
    print()
    
