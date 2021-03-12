'''
Author: your name
Date: 2020-10-15 15:27:11
LastEditTime: 2020-10-16 20:18:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /计算概论C/作业/第三次作业/excise2.py
'''
maxPathNum = 1
maxPath = []

for i in range(2, 10000):
    num = i
    tempPath = [i]
    while(i != 1):
        if i%2:
            i = 3*i+1
            tempPath.append(i)
        else:
            i //= 2
            tempPath.append(i)
    if(len(tempPath) > len(maxPath)):
        maxPath = tempPath
        maxPathNum = num

print(maxPathNum, len(maxPath), sep = '\n')
