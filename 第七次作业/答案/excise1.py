'''
Author: your name
Date: 2020-11-12 16:25:14
LastEditTime: 2020-11-12 16:47:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第七次作业/作业20201110(1)/答案/excise1.py
'''
chinaDynastyFile = open("计算概论C/作业/第七次作业/作业20201110/ChinaDynasty.txt","r", encoding='UTF-8')
filecontent = chinaDynastyFile.read()
chinaDynastyFile.close()

ChinaDynasty = filecontent.splitlines()
for i in range(0, len(ChinaDynasty)):
    ChinaDynasty[i] = ChinaDynasty[i].split(",")
    ChinaDynasty[i][1] = int(ChinaDynasty[i][1])
    ChinaDynasty[i][2] = int(ChinaDynasty[i][2])
    
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

sortedChinaDynasty = sorted(ChinaDynasty, key=lambda x: x[2]-x[1])

printChinaDynasty(ChinaDynasty)
print()
print("按朝代持续时间排序显示")
print()
printChinaDynasty(sortedChinaDynasty)