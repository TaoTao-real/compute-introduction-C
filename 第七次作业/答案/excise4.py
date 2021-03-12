'''
Author: your name
Date: 2020-11-12 19:48:06
LastEditTime: 2020-11-12 20:39:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第七次作业/答案/excise4.py
'''

idfile = open("计算概论C/作业/第七次作业/作业20201110/idX.txt", 'r', encoding="UTF-8")
idcontent = idfile.read()
idfile.close()

statefile = open("计算概论C/作业/第七次作业/作业20201110/ShengCode.txt", 'r', encoding = "UTF-8")
statecontent = statefile.read()
statefile.close()

ids = idcontent.splitlines()
states = statecontent.splitlines()

statesDict = {}
for i in range(0, len(states)):
    states[i] = states[i].split(',')
    statesDict[states[i][0]] = [states[i][1],[0,0]]
    
for i in range(0, len(ids)):
    if(ids[i][0:2] in statesDict):
        if(int(ids[i][-2])%2):
            statesDict[ids[i][0:2]][1][0]+=1
        else:
            statesDict[ids[i][0:2]][1][1]+=1

statesList = sorted(statesDict.items(), key=lambda item:int(item[1][1][0])+int(item[1][1][1]), reverse = True)
for item in statesList:
    print(item[0], item[1][0], "男", item[1][1][0], sep = ',')
    print(item[0], item[1][0], "女", item[1][1][1], sep = ',')