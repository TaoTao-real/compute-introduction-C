'''
Author: your name
Date: 2020-12-27 09:32:59
LastEditTime: 2020-12-27 11:24:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /projects/计算概论C/作业/第七次作业/作业20201110(1)/e3.py
'''
shengdic={}
shengfenfile=open('/Users/starwish/projects/计算概论C/作业/第七次作业/作业20201110(1)/ShengCode.txt','r',encoding='UTF-8')
sfcontent=shengfenfile.read()
sfcontent=sfcontent.splitlines()
for everyline in sfcontent:
    everyline=everyline.split(',')    
    shengdic[everyline[0]]=[everyline[1],0,0]
shengfenfile.close()               
idXfile=open('/Users/starwish/projects/计算概论C/作业/第七次作业/作业20201110(1)/idX.txt','r',encoding='UTF-8') 
idXcontent=idXfile.read()
idXcontent=idXcontent.splitlines()
for everyid in idXcontent:
    if everyid[0:2] in shengdic:
        if(int(everyid[-2])%2 == 1):
            shengdic[everyid[0:2]][1]+=1
        else:
            shengdic[everyid[0:2]][2]+=1
shenglst=list(shengdic.items())
shenglst.sort(key=lambda x:x[1][1]+x[1][2],reverse=True)
newfile=open('/Users/starwish/projects/计算概论C/作业/第七次作业/作业20201110(1)/newfile.txt','w')
print("省区代码，省区名称，性别，人数", file = newfile)
for everysheng in shenglst:
    print(everysheng[0],everysheng[1][0],'男',everysheng[1][1],sep=',', file = newfile)
    print(everysheng[0],everysheng[1][0],'女',everysheng[1][2],sep=',', file = newfile)
newfile.close()
    

    
