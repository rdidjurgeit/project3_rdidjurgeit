

#Build Player

import time


classTypes =["Mage", "Palading", "Rogue", "Barbarian"]
statNames =["Attack", "Speed"," Defense","MPower", "Health"]
# classStats =[[2,5,3,80,60],[8,6,6,60,80],[,8,10,5,0,80],[10,7,8,0,100]]
pName = ""
pStatus =[0,0,0,0,0]
pClass = -1
pStatus = "Fine"
pMoney = 300
pLevel =0
pExp = 0
inventory =[]

#Check Player Sheet
def intexInList(item,myList):
    foundIndex = -1
    for i in range(len(myList)):
        if(item ==myList[i]):
            foundIndex = i
            break
    return foundIndex

def listToText(myList):
    combinedText = "\n"
    for i in range(len(myList)):
        combinedText += str(i) + ")" + myList[i] + "\n"
    return combinedText + "\n"

def checkMenuRange (question,listName,isCanceable =False):
    index = int(input(question + listToText(listName)))
    while(True):
        if(isCanceable and index == -1):
            return index
        elif index < 0 or index > len(listName) -1:
            index =int(input("INvalid choice please try again \n"))
        else:
            return index
        
value = checkMenuRange("what would you like to do?",classTypes)

print(value)

def starLine(numRows,numSleep):
    sLine = "*" * 10
    for i in range(numRows):
        print (sLine)
    time.sleep(numSleep)
    


pName = input("What is your Name\n")
print("Welcome to the Dangeoun" + pName + "!")
starLine(3,1)
