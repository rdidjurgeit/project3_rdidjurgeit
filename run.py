#Build Player
import random
import time
import math


#To build Caracter
classTypes = ["Mage", "Palading", "Rogue", "Barbarian"]
statNames = ["Attack", "Speed"," Defense","MPower", "Health"]
classStats = [[2, 5, 3, 80, 60],[8, 6, 6, 60, 80],[8, 10, 5, 0, 80],[10, 7, 8, 0, 100]]
pName = ""
pStatus =[0,0,0,0,0]
pClass = -1
pStatus = "Fine"
pMoney = 300
pLevel =0
pExp = 0
inventory =[]
activityMenu = ["View Stats", " Explore", "Invetory"]


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
        

def starLine(numRows,numSleep):
    sLine = "*" * 10
    for i in range(numRows):
        print (sLine)
    time.sleep(1)
  

pName = input("What is your Name\n")
print("Welcome to the Dangeoun" +" "+ pName + "!")
starLine(3,1)
for i in range(len(classTypes)):
    print(classTypes[i]+":")
    for j in range(len(classStats[i])):
        print(statNames[j],classStats[i][j])
    starLine(1,2)
pClass = checkMenuRange("Chosse your Class: ", classTypes)
print("you have chosen " + classTypes[pClass]+"!")
pStats = classStats[pClass]
starLine(2,4)
print("From this moment you will be know as "+pName + " The " + classTypes [pClass])


#Main Loop
inGameLoop = True
while(inGameLoop and pStats[4] > 0):
    #activityMenu = ["View Stats", " Explore", "Invetory"]
    actChoice = checkMenuRange("What you will like to do? ", activityMenu)
    if( actChoice == 0):
        print("stats")
    elif(actChoice == 1):
        print("Explore")
    elif(actChoice == 2):
        print("Inventory")
"""
#rooms directions
rooms = {
    'Start': {'West': 'The Maze of Madness', 'East': 'The Spider s Nest',},
    
}

# Tracks current room
current_room = "Start"

# Tracks last move
msg = ""

# Define a function for combat
def combat():
    # Generate a random action for the opponent
    opponent_action = random.choice(_ActionStr)
    
    # Let the player choose their action
    player_action = input("Choose your action (rock/paper/scissors): ").lower()
    
    # Determine the outcome of the combat
    if player_action in _ActionsContainer:
        if (player_action == "rock" and opponent_action == "scissors") or \
           (player_action == "paper" and opponent_action == "rock") or \
           (player_action == "scissors" and opponent_action == "paper"):
            print("You win!")
        elif player_action == opponent_action:
            print("It's a tie!")
        else:
            print("You lose!")
    else:
        print("Invalid action. Try again.")
        """