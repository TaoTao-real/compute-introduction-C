'''
Author: your name
Date: 2020-10-20 16:38:01
LastEditTime: 2020-10-28 09:23:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第四次作业/答案/excise3.py
'''
'''
1. 质数的定义，不能被任何除了1之外的小于其自身的整数整除
2. 需要使用函数，方便我们反复使用判断一个数是否是质数的功能
3. 定义一个函数的时候，函数将根据写入的参数来进行定义好的运算，在最后返回结果或者直接对参数进行修改操作
4. 关于最后输出前一个质数较小的结果，其实不用多做判断，例如10 = 3+7，按照第一个操作数从小到大的寻找顺序，一定会先找到3+7然后才可能遇到7+3
'''

def isPrimeNum(num):
    for i in range(2, num):
        if (num/i) % 1 == 0:
            return False
    return True

num = int(input('num:'))

if num <= 6 or num % 2 == 1:
    print("ERROR!")
else:
    for i in range(2, num-1):
        if(isPrimeNum(i) and isPrimeNum(num-i)):
            print(f"{num}={i}+{num-i}")
            break
