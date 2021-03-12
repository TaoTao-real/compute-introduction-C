'''
Author: your name
Date: 2020-12-11 10:59:28
LastEditTime: 2020-12-11 11:27:01
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第五次作业/e2.py
'''

lst=[]
while(True):
    num=int(input())
    if num==-9999:
        break
    lst.append(num)
lst.sort()
i=len(lst)
if i%2==0:
    zws=(lst[(i//2)-1]+lst[i//2])/2
else:
    zws=lst[(i-1)//2]
print(zws)