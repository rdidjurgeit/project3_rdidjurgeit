import random
import time
import math

# -----------------------------------
# Data Models and Global Variables
# -----------------------------------
classTypes = ["Mage", "Paladin", "Rogue", "Barbarian"]
statNames = ["Attack", "Speed", "Defense", "MPower", "Health"]
classStats = [
    [2, 5, 4, 80, 60],
    [8, 6, 6, 60, 80],
    [8, 12, 5, 0, 80],
    [10, 7, 8, 0, 100]
]

pName = ""
pClass = -1
pStatus = "Fine"
pMoney = 300
pLevel = 0
pExp = 0
inventory = ["potion"]
activityMenu = ["View Stats", "Explore", "Inventory", "Vendor"]
itemsToBuy = [
    ["potion", "burnHeal", "statBoost"],
    [100, 50, 200]
]

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

current_room = "Start"
msg = ""


# -----------------------------------
# Helper Functions
# -----------------------------------
def indexInList(item, myList):
    """Return the index of an item in a list or -1 if not found."""
    for i, val in enumerate(myList):
        if item == val:
            return i
    return -1


def listToText(myList):
    """Convert a list to a user-friendly string representation."""
    combinedText = "\n"
    for i, val in enumerate(myList):
        combinedText += f"{i}) {val}\n"
    return combinedText + "\n"


def checkMenuRange(question, listName, isCanceable=False):
    """
    Safely check user input for a given menu list.
    If invalid, re-prompt until a valid choice or cancellation is made.
    """
    while True:
        user_input = input(question + listToText(listName) + 
                           ("(Enter -1 to cancel)\n" if isCanceable else ""))
        if user_input.strip() == "" or not user_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a number.")
            continue
        index = int(user_input)
        if isCanceable and index == -1:
            return -1
        if 0 <= index < len(listName):
            return index
        else:
            print("Invalid choice, please try again.")


def starLine(numRows, numSleep):
    """Print a decorative line and pause."""
    sLine = "*" * 10
    for _ in range(numRows):
        print(sLine)
    time.sleep(numSleep)


def showInvetory(inventoryList):
    """Show the player's inventory, or inform if empty."""
    if len(inventoryList) < 1:
        print("Inventory is Empty! Go Explore.")
        return
    uniqInventoryList = list(set(inventoryList))
    for i, item in enumerate(uniqInventoryList):
        print(f"{i}) {item} (x{inventoryList.count(item)})")


# -----------------------------------
# Combat Mechanics
# -----------------------------------
def combat(player_stats, monster_stats, monster_highest_stat_index):
    """
    Simulate a combat scenario between player and monster.
    Player can choose 'Attack' or 'Run'.
    Combat ends when player or monster health reaches 0, or player runs.
    """
    while player_stats[4] > 0 and monster_stats[4] > 0:
        player_action = input("Choose your action (Attack/Run): ").capitalize().strip()
        if player_action == "Attack":
            player_damage = max(0, player_stats[monster_highest_stat_index] - monster_stats[monster_highest_stat_index])
            monster_stats[4] -= player_damage
            print(f"You attack the monster for {player_damage} damage. Monster health: {monster_stats[4]}")
            if monster_stats[4] <= 0:
                print("You defeated the monster!")
                return True
        elif player_action == "Run":
            run_chance = random.random()
            if run_chance < 0.5:
                print("You failed to run away!")
            else:
                print("You successfully ran away!")
                return None
        else:
            print("Invalid action. Please choose Attack or Run.")

        # Monster attacks if still alive
        if monster_stats[4] > 0:
            monster_damage = max(0, monster_stats[monster_highest_stat_index] - player_stats[monster_highest_stat_index])
            player_stats[4] -= monster_damage
            print(f"The monster attacks you for {monster_damage} damage. Your health: {player_stats[4]}")
            if player_stats[4] <= 0:
                print("You were defeated by the monster!")
                return False


def monsterEncounter(player_stats, current_room):
    """Handle encountering a monster in a given room."""
    monster_types = ["Goblin", "Skeleton", "Orc", "Zombie"]
    monster = random.choice(monster_types)
    print("You encountered a", monster + "!")
    # Randomize monster stats
    monster_stats = [random.randint(3, 10) for _ in range(5)]
    monster_highest_stat_index = monster_stats.index(max(monster_stats[:-1]))
    print(f"Monster's highest stat index {monster_highest_stat_index}: {monster_stats[monster_highest_stat_index]}")
    print(f"Monster Stats: Attack: {monster_stats[0]} Speed: {monster_stats[1]} Defense: {monster_stats[2]} MPower: {monster_stats[3]} Health: {monster_stats[4]}")

    # Map monster's highest stat to player's stat comparison
    player_highest_stat_index = monster_highest_stat_index
    print(f"Player's highest stat index: {player_highest_stat_index}, Value: {player_stats[player_highest_stat_index]}")

    combat_result = combat(player_stats, monster_stats, player_highest_stat_index)
    if combat_result is True:
        print("You emerge victorious!")
    elif combat_result is False:
        print("Game over!")
    else:
        print("You successfully ran away!")
        return None

    return current_room


# -----------------------------------
# Shop / Vendor Functions
# -----------------------------------
def vendor_menu(player_stats, player_money, inventory):
    """Allow buying and selling items from the vendor."""
    while True:
        print(f"Current balance: ${player_money}")
        shopChoice = checkMenuRange("Welcome to the Shop! Choose an option:",
                                    ["Buy", "Sell", "Show Inventory", "Go Back"], True)
        if shopChoice == -1 or shopChoice == 3:
            break
        elif shopChoice == 0:  # Buy
            buyChoice = checkMenuRange("What would you like to buy?", itemsToBuy[0])
            cost = itemsToBuy[1][buyChoice]
            if player_money - cost >= 0:
                inventory.append(itemsToBuy[0][buyChoice])
                player_money -= cost
                print(f"You bought {itemsToBuy[0][buyChoice]} for ${cost}.")
            else:
                print("Sorry, you cannot afford that item.")
        elif shopChoice == 1:  # Sell
            if len(inventory) > 0:
                itemList = list(set(inventory))
                showInvetory(inventory)
                sellChoice = checkMenuRange("What would you like to sell?", itemList)
                if sellChoice != -1:
                    itemIndex = indexInList(itemList[sellChoice], itemsToBuy[0])
                    if itemIndex >= 0:
                        sellPrice = math.floor(itemsToBuy[1][itemIndex] * 0.9)
                        confirmChoice = checkMenuRange("Really sell?", ["Yes", "No"])
                        if confirmChoice == 0:
                            player_money += sellPrice
                            inventory.remove(itemsToBuy[0][itemIndex])
                            print(f"Item sold! New balance: ${player_money}")
                        else:
                            print("Transaction canceled.")
                    else:
                        print("The vendor does not buy that item.")
                else:
                    print("No item sold.")
            else:
                print("You have nothing to sell!")
        elif shopChoice == 2:  # Show Inventory
            showInvetory(inventory)

    return player_money


# -----------------------------------
# Player Setup
# -----------------------------------
pName = input("What is your Name?\n").strip()
if pName == "":
    pName = "Adventurer"  # Default name if none provided
print("Welcome to the Dungeon " + pName + "!")
starLine(3, 1)

print("Choose your Class:")
for i, cType in enumerate(classTypes):
    print(f"{i}) {cType}:")
    for j, statVal in enumerate(classStats[i]):
        print(f"   {statNames[j]}: {statVal}")
    starLine(1, 1)

pClass = checkMenuRange("Choose your Class: ", classTypes)
pStats = classStats[pClass]
starLine(2, 1)
print("From this moment you will be known as " + pName + " the " + classTypes[pClass] + ".")

# -----------------------------------
# Main Game Loop
# -----------------------------------
inGameLoop = True
while inGameLoop and pStats[4] > 0:
    actChoice = checkMenuRange("What would you like to do?", activityMenu)
    if actChoice == 0:
        # View Stats
        print("Your Stats:")
        for i, stat in enumerate(statNames):
            print(f"{stat}: {pStats[i]}")
    elif actChoice == 1:
        # Explore
        while True:
            print("You are in the", current_room)
            print(msg)
            direction = input("Enter direction (North/South/East/West) or 'Back': ").capitalize().strip()
            if direction == "Back":
                break
            elif direction in rooms[current_room]:
                try:
                    current_room = rooms[current_room][direction]
                    msg = ""
                    # Random encounter chance
                    if random.random() < 0.9:
                        result = monsterEncounter(pStats, current_room)
                        if result is None:
                            # If player ran away, teleport to random room
                            current_room = random.choice(list(rooms.keys()))
                except KeyError:
                    msg = "You can't go that way."
            else:
                msg = "You can't go that way."
    elif actChoice == 2:
        # Inventory
        showInvetory(inventory)
    elif actChoice == 3:
        # Vendor
        pMoney = vendor_menu(pStats, pMoney, inventory)


# -----------------------------------
# Testing Steps (LO5 - partial notes)
# -----------------------------------
# Testing Steps:
# 1. Run the game and enter various inputs to test handling of invalid directions and shop selections.
# 2. Attempt to buy items with insufficient funds.
# 3. Attempt to run away from monsters multiple times.
# 4. Check if inventory and money updates are reflected correctly.
# 5. Try empty input or invalid values where the code asks for direction or menu options to ensure it asks again.