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
    'The Spiders Nest': {
        'West': 'Start',
        'North': 'The Torture Chamber',
        'South': 'The Poisonous Pit'
    },
    'The Poisonous Pit': {
        'North': 'The Spiders Nest',
        'East': 'The Ghouls-infested Crypt'
    },
    'The Ghouls-infested Crypt': {'West': 'The Poisonous Pit'},
    'The Torture Chamber': {
        'West': 'Boss',
        'North': 'The Shadowy Hallway',
        'East': 'The Ominous Altar Room',
        'South': 'The Spiders Nest'
    },
    'The Ominous Altar Room': {
        'West': 'The Torture Chamber',
        'North': 'The Bone-strewn Catacombs'
    },
    'The Bone-strewn Catacombs': {
        'South': 'The Ominous Altar Room',
        'West': 'The Shadowy Hallway'
    },
    'The Shadowy Hallway': {
        'West': 'The Abyssal Abyss',
        'South': 'The Torture Chamber'
    },
    'The Abyssal Abyss': {
        'West': 'The Chamber of Eternal Darkness',
        'East': 'The Shadowy Hallway',
        'South': 'Boss'
    },
    'The Chamber of Eternal Darkness': {
        'West': 'The Riddle-filled Chamber',
        'East': 'The Abyssal Abyss',
        'South': 'The Rotting Prison Cells'
    },
    'The Riddle-filled Chamber': {
        'East': 'The Chamber of Eternal Darkness',
        'South': 'The Cursed Well Room'
    },
    'The Cursed Well Room': {
        'North': 'The Riddle-filled Chamber',
        'South': 'The Chamber of Whispers',
        'East': 'The Rotting Prison Cells'
    },
    'The Chamber of Whispers': {
        'North': 'The Cursed Well Room',
        'East': 'The Maze of Madness'
    },
    'The Rotting Prison Cells': {
        'West': 'The Cursed Well Room',
        'North': 'The Chamber of Eternal Darkness',
        'East': 'Boss',
        'South': 'The Maze of Madness'
    },
    'The Maze of Madness': {
        'West': 'The Chamber of Whispers',
        'North': 'The Rotting Prison Cells',
        'East': 'Start'
    },
    'Boss': {
        'West': 'The Rotting Prison Cells',
        'North': 'The Abyssal Abyss',
        'East': 'The Torture Chamber'
    }
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
    combined_text = "\n"
    for i, val in enumerate(myList):
        combined_text += f"{i}) {val}\n"
    return combined_text + "\n"


def checkMenuRange(question, list_name, is_canceable=False):
    """
    Safely check user input for a given menu list.
    If invalid, re-prompt until a valid choice or cancellation is made.
    """
    while True:
        prompt = question + listToText(list_name)
        if is_canceable:
            prompt += "(Enter -1 to cancel)\n"
        user_input = input(prompt)
        user_input = user_input.strip()

        if user_input == "" or not user_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a number.")
            continue
        index = int(user_input)
        if is_canceable and index == -1:
            return -1
        if 0 <= index < len(list_name):
            return index
        else:
            print("Invalid choice, please try again.")


def starLine(numRows, numSleep):
    """Print a decorative line and pause."""
    sLine = "*" * 10
    for _ in range(numRows):
        print(sLine)
    time.sleep(numSleep)


def showInvetory(inventory_list):
    """Show the player's inventory, or inform if empty."""
    if len(inventory_list) < 1:
        print("Inventory is Empty! Go Explore.")
        return
    uniq_inventory = list(set(inventory_list))
    for i, item in enumerate(uniq_inventory):
        count = inventory_list.count(item)
        print(f"{i}) {item} (x{count})")


# -----------------------------------
# Combat Mechanics
# -----------------------------------
def combat(player_stats, monster_stats, monster_highest_stat_index):
    """
    Simulate a combat scenario between player and monster.
    Player can choose 'Attack' or 'Run'.
    Combat ends when player or monster health <= 0, or player runs.
    """
    while player_stats[4] > 0 and monster_stats[4] > 0:
        player_action = input("Choose your action (Attack/Run): ")
        player_action = player_action.capitalize().strip()

        if player_action == "Attack":
            p_damage = (player_stats[monster_highest_stat_index] -
                            monster_stats[monster_highest_stat_index])
            player_damage = max(1, p_damage)
            monster_stats[4] -= player_damage
            print(f"You attack the monster for {player_damage} damage. "
                    f"Monster health: {monster_stats[4]}")
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
            m_damage = (monster_stats[monster_highest_stat_index] -
                        player_stats[monster_highest_stat_index])
            monster_damage = max(0, m_damage)
            player_stats[4] -= monster_damage
            print(f"The monster attacks you for {monster_damage} damage. "
                  f"Your health: {player_stats[4]}")
            if player_stats[4] <= 0:
                print("You were defeated by the monster!")
                return False


def monsterEncounter(player_stats, current_room_enc):
    """Handle encountering a monster in a given room."""
    monster_types = ["Goblin", "Skeleton", "Orc", "Zombie"]
    monster = random.choice(monster_types)
    print("You encountered a", monster + "!")

    # Randomize monster stats
    monster_stats = [random.randint(3, 10) for _ in range(5)]
    m_highest_index = monster_stats.index(max(monster_stats[:-1]))
    print(f"Monster's highest stat index {m_highest_index}: "
          f"{monster_stats[m_highest_index]}")
    print("Monster Stats: "
          f"Attack: {monster_stats[0]} "
          f"Speed: {monster_stats[1]} "
          f"Defense: {monster_stats[2]} "
          f"MPower: {monster_stats[3]} "
          f"Health: {monster_stats[4]}")

    player_highest_stat_index = m_highest_index
    print(f"Player's highest stat index: {player_highest_stat_index}, "
          f"Value: {player_stats[player_highest_stat_index]}")

    c_result = combat(player_stats, monster_stats, player_highest_stat_index)
    if c_result is True:
        print("You emerge victorious!")
        # Increase the player's Attack, Speed, Defense, and Health by 2
        # MPower (index 3) is not increased
        player_stats[0] += 2  # Attack
        player_stats[1] += 2  # Speed
        player_stats[2] += 2  # Defense
        player_stats[4] += 2  # Health

        print("You feel stronger after this victory!")
        print("Your Attack, Speed, Defense, and Health have each increased by 2.")
        print("Your new stats:")
        for i, stat in enumerate(statNames):
            print(f"{stat}: {player_stats[i]}")
        
    elif c_result is False:
        print("Game over!")
    else:
        print("You successfully ran away!")
        return None

    return current_room_enc



# -----------------------------------
# Shop / Vendor Functions
# -----------------------------------
def vendor_menu(player_stats, player_money, inv):
    """Allow buying and selling items from the vendor."""
    while True:
        print(f"Current balance: ${player_money}")
        vendor_options = ["Buy", "Sell", "Show Inventory", "Go Back"]
        shop_choice = checkMenuRange("Welcome to the Shop! Choose an option:",
                                     vendor_options, True)
        if shop_choice == -1 or shop_choice == 3:
            break
        elif shop_choice == 0:  # Buy
            buy_choice = checkMenuRange("What would you like to buy?",
                                        itemsToBuy[0])
            cost = itemsToBuy[1][buy_choice]
            if player_money - cost >= 0:
                inv.append(itemsToBuy[0][buy_choice])
                player_money -= cost
                print(f"You bought {itemsToBuy[0][buy_choice]} for ${cost}.")
            else:
                print("Sorry, you cannot afford that item.")
        elif shop_choice == 1:  # Sell
            if len(inv) > 0:
                item_list = list(set(inv))
                showInvetory(inv)
                sell_choice = checkMenuRange("What would you like to sell?",
                                             item_list)
                if sell_choice != -1:
                    i_index = indexInList(item_list[sell_choice],
                                          itemsToBuy[0])
                    if i_index >= 0:
                        sell_price = math.floor(itemsToBuy[1][i_index] * 0.9)
                        conf_choice = checkMenuRange("Really sell?",
                                                     ["Yes", "No"])
                        if conf_choice == 0:
                            player_money += sell_price
                            inv.remove(itemsToBuy[0][i_index])
                            print("Item sold! New balance: "
                                  f"${player_money}")
                        else:
                            print("Transaction canceled.")
                    else:
                        print("The vendor does not buy that item.")
                else:
                    print("No item sold.")
            else:
                print("You have nothing to sell!")
        elif shop_choice == 2:  # Show Inventory
            showInvetory(inv)

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
print("From this moment you will be known as " + pName + " the " +
      classTypes[pClass] + ".")

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
            direction = input("Enter direction (North/South/East/West) "
                              "or 'Back': ").capitalize().strip()
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
# 1. Run the game and enter various inputs to test handling of invalid
#    directions and shop selections.
# 2. Attempt to buy items with insufficient funds.
# 3. Attempt to run away from monsters multiple times.
# 4. Check if inventory and money updates are reflected correctly.
# 5. Try empty input or invalid values where the code asks for direction
#    or menu options to ensure it asks again.
