'''
Author: your name
Date: 2020-10-20 16:28:11
LastEditTime: 2020-10-23 15:05:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第四次作业/答案/excise2.py
'''

'''
1. 九九乘法表，外部的for循环每循环一次输出一行，内部的for循环每循环一次输出一项
2. 在每一项之间使用空格间隔，而不是每输出一项就换行，所以需要通过修改print中的end参数，设置成‘ ’
3. 每次输出一行之后，输出换行符'\n'在新的一行中继续输出下一行，这里通过print（）的方式，因为print（）隐式的含义是print(end='\n')
4. 内循环要注意乘法项中的第二个数一定是大于等于当前行数
5. 为了每一个乘法项对齐，需要根据乘积是一位数还是两位数来修改输出格式
'''
for i in range(1, 10):
    for j in range(i, 10):
        if i*j >= 10:
            print(f"{i}*{j}={i*j}", sep='', end=' ')
        else:
            print(f"{i}*{j}= {i*j}", sep='', end=' ')
    print()
