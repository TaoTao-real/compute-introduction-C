'''
Author: your name
Date: 2020-11-03 16:10:56
LastEditTime: 2020-11-17 12:44:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第六次作业/答案/excise1.py
'''
namesFile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/内容/50万人名.txt", encoding="UTF-8")
namesFileContent = namesFile.read()
namesFile.close()
names = namesFileContent.splitlines()

lastNameCountDict = {}
for name in names:
    lastName = name[0]
    if lastName in lastNameCountDict:
        lastNameCountDict[lastName]+=1
    else:
        lastNameCountDict[lastName]=1
lastNameCountList = []
for lastName in lastNameCountDict:
    lastNameCountList.append((lastName, lastNameCountDict[lastName]))
lastNameCountList.sort(key = lambda x:x[1], reverse = True)
outfile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/答案/out1.txt", "w", encoding="UTF-8")
for item in lastNameCountList:
    print(f"{item[0]},{item[1]}", file = outfile)
outfile.close()
