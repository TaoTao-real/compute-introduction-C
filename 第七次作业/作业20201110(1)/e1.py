'''
Author: your name
Date: 2020-12-25 09:33:25
LastEditTime: 2020-12-25 10:54:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第七次作业/作业20201110(1)/e1.py
'''
sfz=input()
lstxs=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
lst=['1','0','x','9','8','7','6','5','4','3','2']
if 'z'==sfz[17]:
    sum = 0
    for i in range(0,17):
        sum=sum+int(sfz[i])*lstxs[i]
    ys=sum%11
    print(lst[ys])
else:
    for i in range(0,10):
        sum=0
        for j in range(0,17):
            if sfz[j]=='z':
                sum=sum+i*lstxs[j]
            else:
                sum=sum+int(sfz[j])*lstxs[j]
        ys=sum%11
        
        if (lst[ys]==int(sfz[17])):
            print(i)
            break
                           
            


