'''
Author: your name
Date: 2020-12-11 09:53:20
LastEditTime: 2020-12-11 10:41:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第四次作业/e3.py
'''
'''
def isPrime(num):
    for i in range(2,num):
        if  num%i==0:
           return(False)
    return(True)

x=int(input("请输入一个大于6的偶数"))
if x%2==0 and x>6:
    for i in (3,x):
        if isPrime(i) and isPrime(x-i):
            print(f"{x}={i}+{x-i}")
else:
    print("ERROR!")
'''

print("xAA" in "xAAYaa")

