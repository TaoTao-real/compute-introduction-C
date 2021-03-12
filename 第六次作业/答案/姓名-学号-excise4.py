namesFile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/内容/50万人名.txt", encoding="UTF-8")
namesFileContent = namesFile.read()
namesFile.close()
names = namesFileContent.splitlines()

lastNameCountDict = {}
lastNameCount = 0
for name in names:
    if(len(name)!=4):
        continue
    lastNameCount+=1
    lastName = name[0:2]
    if lastName in lastNameCountDict:
        lastNameCountDict[lastName]+=1
    else:
        lastNameCountDict[lastName]=1
lastNameCountList = []
for lastName in lastNameCountDict:
    lastNameCountList.append((lastName, lastNameCountDict[lastName]))
lastNameCountList.sort(key = lambda x:x[1], reverse = True)

outfile = open("/Users/starwish/projects/计算概论C/作业/第六次作业/答案/out4.txt", "w", encoding="UTF-8")
printedNameCount = 0
for item in lastNameCountList:
    if(printedNameCount>=lastNameCount*0.8):
        break
    print(f"{item[0]}{item[1]}", file = outfile)
    printedNameCount+=item[1]
outfile.close()