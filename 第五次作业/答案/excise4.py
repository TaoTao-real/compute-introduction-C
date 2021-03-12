'''
Author: your name
Date: 2020-10-28 11:03:48
LastEditTime: 2020-11-03 12:58:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第五次作业/答案/excise4.py
'''
'''
1. 同样需要用到排序操作，这里需要用lambda函数来自定义排序规则
'''

def printChinaDynasty(dynastys):
    durations = []
    maxDuration = 0
    minDuration = 1000
    for dynasty in dynastys:
        duration = dynasty[2]-dynasty[1]
        if(duration > maxDuration):
            maxDuration = duration
        if(duration < minDuration):
            minDuration = duration
        durations.append(duration)
    totalSpaceCount = maxDuration//minDuration
    blackSpace = '◻'
    whiteSpace = '◼︎'
    for i in range(0, len(dynastys)):
        whiteSpaceCount = durations[i]//minDuration
        blackSpaceCount = totalSpaceCount-whiteSpaceCount
        print(
            f"{blackSpace*blackSpaceCount+whiteSpace*whiteSpaceCount}{dynastys[i][0]}({dynastys[i][1]},{dynastys[i][2]})持续{dynastys[i][2]-dynastys[i][1]}年")


ChinaDynasty = [["夏朝", -2029, -1559], ["商朝", -1559, -1046],
                ["西周", -1046, -771], ["东周", -771, -256], ["秦朝", -221, -207],
                ["汉朝", -202, 220], ["魏晋南北朝", 220, 581], ["隋朝", 581, 618],
                ["唐朝", 618, 907], ["五代十国", 907, 979], ["宋朝", 960, 1279],
                ["元朝", 1271, 1368], ["明朝", 1368, 1644], ["清朝", 1644, 1911]]

sortedChinaDynasty = sorted(ChinaDynasty, key=lambda x: x[2]-x[1])

printChinaDynasty(ChinaDynasty)
print()
print("按朝代持续时间排序显示")
print()
printChinaDynasty(sortedChinaDynasty)
