'''
Author: your name
Date: 2020-11-26 14:35:59
LastEditTime: 2020-11-26 14:39:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第八次作业/答案/excise2.py
'''
asmFile = open("/Users/starwish/projects/计算概论C/作业/第八次作业/asmData.txt", 'r', encoding="UTF-8")
asmProgram = asmFile.read()
asmFile.close()

asmInstruction = asmProgram.splitlines()

insCnt = {}
for ins in asmInstruction:
    ins = ins.split()
    if(len(ins) >= 4):
        if(ins[3] in insCnt):
            insCnt[ins[3]]+=1
        else:
            insCnt[ins[3]] = 1

print(insCnt)