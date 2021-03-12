'''
Author: your name
Date: 2020-10-20 16:49:32
LastEditTime: 2020-10-28 09:25:53
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第四次作业/答案/excise4.py
'''

'''
1. 由于题目已经告知是三位数，只需要求出个十百位的整数值，注意要使用//整数除法，要不然会得到小数
2. pow中的两个参数都必须是整数
'''

for num in range(100, 1001):
    a = num % 10
    b = (num % 100)//10
    c = num//100
    if pow(a, 3)+pow(b, 3)+pow(c, 3) == num:
        print(num)
