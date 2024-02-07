#Build Player
import random
import time
import math


#To build Caracter
classTypes = ["Mage", "Palading", "Rogue", "Barbarian"]
statNames = ["Attack", "Speed","Defense","MPower", "Health"]
classStats = [[2, 5, 3, 80, 60],[8, 6, 6, 60, 80],[8, 10, 5, 0, 80],[10, 7, 8, 0, 100]]
pName = ""
pStatus =[0,0,0,0,0]
pClass = -1
pStatus = "Fine"
pMoney = 300
pLevel =0
pExp = 0
inventory =["potion"]
activityMenu = ["View Stats", "Explore", "Invetory","Vendedor"]
itemsToBuy = [["potion", "burnHeal", "statBoost"], [100, 50, 50, 200]]


#Check Player Sheet
def indexInList(item,myList):
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


def combat(player_stats, monster_stats):
    while player_stats[4] > 0 and monster_stats[4] > 0:
        # Player attacks
        player_damage = max(0, player_stats[0] - monster_stats[2])
        monster_stats[4] -= player_damage
        print("You attack the monster for", player_damage, "damage. Monster health:", monster_stats[4])
        if monster_stats[4] <= 0:
            print("You defeated the monster!")
            return True
        # Monster attacks
        monster_damage = max(0, monster_stats[0] - player_stats[2])
        player_stats[4] -= monster_damage
        print("The monster attacks you for", monster_damage, "damage. Your health:", player_stats[4])
        if player_stats[4] <= 0:
            print("You were defeated by the monster!")
            return False


# Add combat functionality to the monsterEncounter function
def monsterEncounter():
    monster_types = ["Goblin", "Skeleton", "Orc", "Zombie"]
    monster = random.choice(monster_types)
    print("You encountered a", monster + "!")
    # Initialize monster stats
    monster_stats = [random.randint(3, 10) for _ in range(5)]
    print("Monster Stats: Attack:", monster_stats[0], "Speed:", monster_stats[1], "Defense:", monster_stats[2], "MPower:", monster_stats[3], "Health:", monster_stats[4])
    combat_result = combat(pStats, monster_stats)
    if combat_result:
        print("You emerge victorious!")
    else:
        print("Game over!")


#function inventory
def showInvetory(inventoryList):
    if(len(inventoryList) < 1):
        print("Inventory is Empty! Go Explore")
        return
    uniqInventoryList = list(set(inventoryList))
    for i in range(len(uniqInventoryList)):
        print(str(i)+ ") " + uniqInventoryList[i] +"("+str(inventoryList.count(uniqInventoryList[i]))+")")


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


#rooms directions
rooms = {
    'Start': {'West': 'The Maze of Madness', 'East': 'The Spiders Nest',},
    'The Maze of Madness': {'North':'The Rotting Prison Cells', 'West':'The Chamber of Whispers', 'East':'Start',},
    'The Spiders Nest': {'North':'The Torture Chamber', 'South':'The Poisonous Pit', 'West':"Start"},   
}


current_room ="Start"

#Resolt of the last move
msg=""


#Main Loop
inGameLoop = True
while inGameLoop and pStats[4] > 0:
    # Activity Menu = ["View Stats", "Explore", "Inventory", "Vendedor"]
    actChoice = checkMenuRange("What would you like to do? ", activityMenu)
    if actChoice == 0:
        print("Stats")
    elif actChoice == 1:
        while True:
            print("You are in the", current_room)
            print(msg)
            direction = input("Enter the direction you want to go (North/South/East/West), or type 'Back' to return to the main menu: ").capitalize()
            if direction == "Back":
                break
            elif direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                msg = ""
                if random.random() < 0.9:
                    monsterEncounter()
            else:
                msg = "You can't go that way."
    elif(actChoice == 2):
        showInvetory(inventory)
    elif(actChoice == 3):
        while(True):
            print("Current balance is $" +str(pMoney))
            shopChoice = checkMenuRange("Welcome to my the Shop! My name is Mario,you like to Buy or Sell",["Buy", "Sell", "SHow Inventory", "Go Back"], True)
            if shopChoice == -1:
                break
            elif shopChoice == 0:
                buyChoice = checkMenuRange("What would you like to buy?", itemsToBuy[0])
                if(pMoney - itemsToBuy[1][buyChoice] >=0):
                    inventory.append(itemsToBuy[0][buyChoice])
                    pMoney -= itemsToBuy[1][buyChoice]
                else:
                    print("Sorry you can not afford " + itemsToBuy[0][buyChoice])
            elif shopChoice == 1:
                if(len(inventory) > 0):
                    itemList =list(set(inventory))
                    showInvetory(inventory)
                    sellChoice = checkMenuRange("What would you like to sell?", itemList)
                    if(sellChoice != -1):
                        itemIndex = indexInList(itemList[sellChoice], itemsToBuy[0])
                        sellPrice = math.floor(itemsToBuy[1][itemIndex] * .9)
                        confirmChoice = checkMenuRange("RElly?",["Yes", "No"])
                        if confirmChoice == 0:
                            pMoney +=sellPrice
                            inventory.remove(itemsToBuy[0][itemIndex])
                            print("ITem Sold balance $"+str(pMoney))
                        else:
                            print("Sorry you have nothing to Sell!")
            elif shopChoice == 2:
                showInvetory(inventory)
            elif shopChoice == 3:
                break
                

        
        
"""
#

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