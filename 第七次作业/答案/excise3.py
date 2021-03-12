'''
Author: your name
Date: 2020-11-12 19:25:02
LastEditTime: 2020-11-12 19:47:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第七次作业/答案/excise3.py
'''
def isPrimeNum(num):
    for i in range(2, num):
        if (num/i) % 1 == 0:
            return False
    return True

start = int(input("Input start num: "))
end = int(input("Input end num: "))

primenum1 = 0
primenum2 = 0
maxDistance = 0
maxDistancePM1 = 0
maxDistancePM2 = 0

for num in range(start, end+1):
    if(isPrimeNum(num) and primenum1 == 0):
        primenum1 = num
    elif(isPrimeNum(num) and primenum2 == 0):
        primenum2 = num
        maxdistance = primenum2 - primenum1
        maxDistancePM1 = primenum1
        maxDistancePM2 = primenum2
    elif(isPrimeNum(num)):
        primenum1 = primenum2
        primenum2 = num
        if primenum2 - primenum1 - 1 > maxDistance:
            maxDistance = primenum2 - primenum1 -1
            maxDistancePM1 = primenum1
            maxDistancePM2 = primenum2
print(maxDistancePM1, maxDistancePM2)
        