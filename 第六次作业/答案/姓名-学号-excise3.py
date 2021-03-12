'''
Author: your name
Date: 2020-11-03 16:57:44
LastEditTime: 2020-11-05 19:55:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第六次作业/答案/excise3.py
'''
namesFile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/内容/50万人名.txt", encoding="UTF-8")
namesFileContent = namesFile.read()
namesFile.close()
names = namesFileContent.splitlines()

doubleCCountDict = {}

for name in names:
    for i in range(2, len(name)):
        if(name[i] == name[i-1]):
            if name[i]+name[i-1] in doubleCCountDict:
                doubleCCountDict[name[i]+name[i-1]]+=1
            else:
                doubleCCountDict[name[i]+name[i-1]]=1
            break

doubleCCountList = []
for doubleC in doubleCCountDict:
    doubleCCountList.append((doubleC, doubleCCountDict[doubleC]))
doubleCCountList.sort(key = lambda x:x[1], reverse = True)

outfile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/答案/out3.txt", "w", encoding="UTF-8")
for i in range(0, 201):
    print(f"{doubleCCountList[i][0]}\t{doubleCCountList[i][1]}", file = outfile)
outfile.close()