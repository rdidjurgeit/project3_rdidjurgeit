#Build Player
import random
import time
import math


#To build Caracter
classTypes = ["Mage", "Palading", "Rogue", "Barbarian"]
statNames = ["Attack", "Speed","Defense","MPower", "Health"]
classStats = [[2, 5, 4, 80, 60],[8, 6, 6, 60, 80],[8, 12, 5, 0, 80],[10, 7, 8, 0, 100]]
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


def combat(player_stats, monster_stats, monster_highest_stat_index):
    while player_stats[4] > 0 and monster_stats[4] > 0:
        # Player's turn
        player_action = input("Choose your action (Attack/Run): ").capitalize()
        if player_action == "Attack":
            player_damage = max(0, player_stats[monster_highest_stat_index] - monster_stats[monster_highest_stat_index])  # Compare player's attack with monster's highest stat
            monster_stats[4] -= player_damage
            print("You attack the monster for", player_damage, "damage. Monster health:", monster_stats[4])
            if monster_stats[4] <= 0:
                print("You defeated the monster!")
                return True
        elif player_action == "Run":
            run_chance = random.random()
            if run_chance < 0.5:
                print("You failed to run away!")
            else:
                print("You successfully ran away!")
                return None  # Return None to indicate successful escape
        else:
            print("Invalid action. Please choose Attack or Run.")

        # Monster's turn
        if monster_stats[4] > 0:
            monster_damage = max(0, monster_stats[monster_highest_stat_index] - player_stats[monster_highest_stat_index])  # Compare monster's highest stat with player's corresponding stat
            player_stats[4] -= monster_damage
            print("The monster attacks you for", monster_damage, "damage. Your health:", player_stats[4])
            if player_stats[4] <= 0:
                print("You were defeated by the monster!")
                return False

# Add combat functionality to the monsterEncounter function
def monsterEncounter(player_stats, current_room):
    monster_types = ["Goblin", "Skeleton", "Orc", "Zombie"]
    monster = random.choice(monster_types)
    print("You encountered a", monster + "!")
    # Randomize monster stats
    monster_stats = [random.randint(3, 10) for _ in range(5)]
    # Ensure the highest stat determines the combat comparison
    monster_highest_stat_index = monster_stats.index(max(monster_stats[:-1]))  # Find the index of the highest stat excluding health
    print(f"Monster's highest stat is at index {monster_highest_stat_index}: {monster_stats[monster_highest_stat_index]}")
    print("Monster Stats: Attack:", monster_stats[0], "Speed:", monster_stats[1], "Defense:", monster_stats[2], "MPower:", monster_stats[3], "Health:", monster_stats[4])
    
    # Set the player's highest stat index based on the monster's highest stat index
    if monster_highest_stat_index == 0:
        player_highest_stat_index = 0  # Attack
    elif monster_highest_stat_index == 1:
        player_highest_stat_index = 1  # Speed
    elif monster_highest_stat_index == 2:
        player_highest_stat_index = 2  # Defense
    elif monster_highest_stat_index == 3:
        player_highest_stat_index = 3  # Mpower
    
    print(f"Player's highest stat index is set to {player_highest_stat_index}: {player_stats[player_highest_stat_index]}")
    
    # Store player's highest stat index for use in combat
    combat_result = combat(player_stats, monster_stats, player_highest_stat_index)
    if combat_result is True:
        print("You emerge victorious!")
    elif combat_result is False:
        print("Game over!")
    else:
        print("You successfully ran away!")
        # Return None if the player successfully escapes
        return None

    # Return the current room if the player is defeated
    return current_room


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
          'Start': {'West': 'The Maze of Madness', 'East': 'The Spiders Nest'},
            'The Spiders Nest': {'West': 'Start', 'North': 'The Torture Chamber', 'South': 'The Poisonous Pit'},
            'The Poisonous Pit': {'North': 'The Spiders Nest', 'East': 'The Ghouls-infested Crypt'},
            'The Ghouls-infested Crypt': {'West': 'The Poisonous Pit'},
            'The Torture Chamber': {'West': 'Boss', 'North': 'The Shadowy Hallway', 'East': 'The Ominous Altar Room', 'South': 'The Spiders Nest'},
            'The Ominous Altar Room': {'West': 'The Torture Chamber', 'North': 'The Bone-strewn Catacombs'},
            'The Bone-strewn Catacombs': {'South': 'The Ominous Altar Room', 'West': 'The Shadowy Hallway'},
            'The Shadowy Hallway': {'West': 'The Abyssal Abyss', 'South': 'The Torture Chamber'},
            'The Abyssal Abyss': {'West': 'The Chamber of Eternal Darkness', 'East': 'The Shadowy Hallway', 'South': 'Boss'},
            'The Chamber of Eternal Darkness': {'West': 'The Riddle-filled Chamber', 'East': 'The Abyssal Abyss', 'South': 'The Rotting Prison Cells'},
            'The Riddle-filled Chamber': {'East': 'The Chamber of Eternal Darkness', 'South': 'The Cursed Well Room'},
            'The Cursed Well Room': {'North': 'The Riddle-filled Chamber', 'South': 'The Chamber of Whispers', 'East': 'The Rotting Prison Cells'},
            'The Chamber of Whispers': {'North': 'The Cursed Well Room', 'East': 'The Maze of Madness'},
            'The Rotting Prison Cells': {'West': 'The Cursed Well Room', 'North': 'The Chamber of Eternal Darkness', 'East': 'Boss', 'South': 'The Maze of Madness'},
            'The Maze of Madness': {'West': 'The Chamber of Whispers', 'North': 'The Rotting Prison Cells', 'East': 'Start'},
            'Boss': {'West': 'The Rotting Prison Cells', 'North': 'The Abyssal Abyss', 'East': 'The Torture Chamber'}
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
                try:
                    current_room = rooms[current_room][direction]
                    msg = ""
                    if random.random() < 0.9:
                        # Pass the current room to the monsterEncounter function
                        result = monsterEncounter(pStats, current_room)
                        if result is None:
                            # If the player successfully ran away, move to a random room
                            current_room = random.choice(list(rooms.keys()))
                except KeyError:
                    msg = "You can't go that way. This room doesn't exist."
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
                