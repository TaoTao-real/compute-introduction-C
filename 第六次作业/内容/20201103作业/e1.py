'''
Author: your name
Date: 2020-12-16 11:01:57
LastEditTime: 2020-12-16 11:27:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第六次作业/内容/20201103作业/e1.py
'''

with open("/Users/starwish/projects/计算概论C/作业/第六次作业/内容/20201103作业/50万人名.txt","r",encoding="UTF-8") as f:
    fcontent=f.read()
    namelist = fcontent.splitlines()
    namedict = {}
    for name in namelist:
        if name[0] in namedict:
            namedict[name[0]]+=1
        else:
            namedict[name[0]] =1
    print(namedict)
    newnamelist = list(namedict.items())
    