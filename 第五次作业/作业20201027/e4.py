'''
Author: your name
Date: 2020-12-16 10:16:42
LastEditTime: 2020-12-16 10:39:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第五次作业/作业20201027/e4.py
'''
ChinaDynasty=[["夏朝",-2029,-1559],["商朝",-1559,-1046],
["西周",-1046,-771],["东周",-771,-256],["秦朝",-221,-207],
["汉朝",-202,220],["魏晋南北朝",220,581],["隋朝",581,618],
["唐朝",618,907],["五代十国",907,979],["宋朝",960,1279],
["元朝",1271,1368],["明朝",1368,1644],["清朝",1644,1911]]
newChinaDynasty=sorted(ChinaDynasty,key=lambda x:x[2]-x[1])
print(newChinaDynasty)
newChinaDynasty=sorted(ChinaDynasty,key=lambda x:x[2])
for dynsty in newChinaDynasty:   
    print(f"{dynsty[0]}({dynsty[1]}{dynsty[2]})持续{dynsty[2]-dynsty[1]}年")

newlist = []