'''
Author: your name
Date: 2020-11-12 16:49:13
LastEditTime: 2020-11-12 20:06:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第七次作业/答案/excise2.py
'''

factors = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
lastnum = [1,0,'X',9,8,7,6,5,4,3,2]

ID = input("input your ID num:")

if(ID[17] == 'Z'):
    sum = 0
    for i in range(0, 17):
        sum += int(ID[i])*factors[i]
    print("Z is: ",lastnum[sum%11])
else:
    for i in range(0, 10):
        sum = 0
        for j in range(0, 17):
            if(ID[j]!='Z'):
                sum += int(ID[j])*factors[j]
            else:
                sum += i*factors[j]
        if(lastnum[sum%11] == int(ID[17])):
            print("Z is: ", i)
            break

