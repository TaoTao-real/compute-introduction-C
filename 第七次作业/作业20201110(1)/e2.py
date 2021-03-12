'''
Author: your name
Date: 2020-12-25 10:55:01
LastEditTime: 2020-12-25 11:11:01
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第七次作业/作业20201110(1)/e2.py
'''
'''
def isPrime(x):
    for i in range(2,x):
        if  x%i==0:
            return False
    return True
'''
'''
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
'''
def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n

sum(3)
    
