'''
Author: your name
Date: 2020-11-26 14:11:01
LastEditTime: 2020-11-26 14:35:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第八次作业/答案/excise1.py
'''
asmFile = open("/Users/starwish/projects/计算概论C/作业/第八次作业/asmData.txt", 'r', encoding="UTF-8")
asmProgram = asmFile.read()
asmFile.close()

asmInstruction = asmProgram.splitlines()

insSet = set()
for ins in asmInstruction:
    ins = ins.split()
    if(len(ins) >= 4):
        insSet.add(ins[3])

print(len(insSet))