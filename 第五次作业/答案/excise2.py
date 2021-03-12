'''
Author: your name
Date: 2020-10-28 09:47:00
LastEditTime: 2020-11-03 12:56:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第五次作业/答案/excise2.py
'''

'''
1. 用持续循环读取数据，当读到终结成绩的时候跳出循环
2. 计算这些特征值很简单，但是要注意先排序，才能找到中位数
'''

scores = []
while(True):
    score = int(input("score:"))
    if(score != -9999):
        scores.append(score)
    else:
        break

scoresLen = len(scores)
scoressum = sum(scores)
median = scores[scoresLen//2] if scoresLen % 2 == 1 else (scores[scoresLen//2]+scores[scoresLen//2-1])/2

mean = scoressum/scoresLen

temp = 0
for score in scores:
    temp += pow(score-mean, 2)
deviation = pow(temp/scoresLen, 0.5)

print(f"median:{median}, mean:{mean}, standard deviation:{deviation}")
