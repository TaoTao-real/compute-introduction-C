'''
Author: your name
Date: 2020-11-03 16:55:32
LastEditTime: 2020-11-14 19:43:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第六次作业/答案/excise2.py
'''
namesFile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/内容/50万人名.txt", encoding="UTF-8")
namesFileContent = namesFile.read()
namesFile.close()
names = namesFileContent.splitlines()

firstNameCountDict = {}
for name in names:
    for c in name[1:]:
        if c in firstNameCountDict:
            firstNameCountDict[c]+=1
        else:
            firstNameCountDict[c]=1
            
firstNameCountList = []
for firstName in firstNameCountDict:
    firstNameCountList.append((firstName, firstNameCountDict[firstName]))
firstNameCountList.sort(key = lambda x:x[1], reverse = True)
outfile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/答案/out2.txt", "w", encoding="UTF-8")
for i in range(0, 201):
    print(f"{firstNameCountList[i][0]}\t{firstNameCountList[i][1]}", file = outfile)
outfile.close()