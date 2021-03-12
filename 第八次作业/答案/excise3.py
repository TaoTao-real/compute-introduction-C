'''
Author: your name
Date: 2020-11-26 14:39:55
LastEditTime: 2020-11-26 14:48:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第八次作业/答案/excise3.py
'''
asmFile = open("/Users/starwish/projects/计算概论C/作业/第八次作业/asmData.txt", 'r', encoding="UTF-8")
asmProgram = asmFile.read()
asmFile.close()

asmInstruction = asmProgram.splitlines()

insKindCnt = {"单参数指令":0, "双参数指令":0, "三参数指令":0, "无参数指令":0}
for ins in asmInstruction:
    ins = ins.split()
    if(len(ins) >= 4):
        if(len(ins) == 4):
            insKindCnt["无参数指令"]+=1
        elif(len(ins) == 5):
            insKindCnt["单参数指令"]+=1
        elif(len(ins) == 6):
            insKindCnt["双参数指令"]+=1
        elif(len(ins) == 7):
            insKindCnt["三参数指令"]+=1
            

print(insKindCnt)