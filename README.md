# Endless Dungeon

Endless Dungeon is a text-based adventure game where players explore dungeons, battle monsters, and uncover treasures. The game operates within a terminal interface and provides an engaging experience with various classes, combat mechanics, and character progression.

 [Link for Game](https://project3-rdidjurgeit-d227d31817aa.herokuapp.com/)

## Table of Contents

- [Endless Dungeon](#endless-dungeon)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Character Classes](#character-classes)
      - [Combat System](#combat-system)
      - [Dungeon Exploration](#dungeon-exploration)
      - [Inventory and Items](#inventory-and-items)
      - [Game Progression](#game-progression)
      - [Terminal Interaction](#terminal-interaction)
      - [Start Button](#start-button)
    - [Future Ideas](#future-ideas)
    - [Images](#images)
- [Technology Used](#technology-used)
  - [Languages](#languages)
  - [Platforms](#platforms)
  - [Other Tools](#other-tools)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Validator Testing](#validator-testing)
- [Deployment](#deployment)
  - [Local](#local)
    - [Local Preparation](#local-preparation)
  - [Credits and Contact](#credits-and-contact)
    - [Credits](#credits)
    - [Contact](#contact)

----

## Overview

Endless Dungeon is a thrilling terminal-based adventure game that focuses on exploration and combat. Players choose from different character classes, each with unique stats and abilities. The game provides an interactive and challenging experience where players engage in battles with monsters, solve puzzles, and unlock treasure.

The game is designed to keep players engaged with a series of randomly monster and 16 possibles rooms with a dynamic combat mechanics based on the player's chosen class. This game is perfect for fans of text-based RPGs who enjoy a nostalgic, immersive experience in the terminal.

## Features

### Existing Features

#### Character Classes

- Choose from multiple classes, each with distinct stats and abilities. Classes are designed with advantages and disadvantages in combat, adding strategic depth to battles.
- Each class has a unique set of strengths and weaknesses, which influence gameplay and strategy.

#### Combat System

- The combat system is based on stats that determine the effectiveness of attacks and defense.
- Monster Stats are Generate random.
- The Stats use for Combat is always base in the Monster highest status.
- Players face different types of monsters, each with its own strengths and weaknesses.
- If player win he will level stats and win gold our items.
- If Player run he will end up in a different rum from the Dungeon.

#### Dungeon Exploration

- Players can explore the Dungeon giving directions, there is a set of Direction that a person can go for each room.
- The final Bos have their own status and He is in the Boss Rum.

#### Inventory and Items

- Players can collect and use various items, including potions, to enhance their chances of survival.
- The inventory system allows easy management of items found during exploration.

#### Game Progression

- Players level up by defeating monsters.
- Character progression includes stat boosts,and access to vender.

#### Terminal Interaction

- The game runs directly in the terminal, providing a nostalgic and immersive text-based interface.
- The possibles commands are display to interact with the game world, including movement, combat, and inventory management.

#### Start Button

- Press the "Run Program" button to begin the game, and follow the in-game instructions to start your adventure.

### Future Ideas

1. **Graphical Interface**: In future updates, a graphical user interface (GUI) will be implemented to enhance the gaming experience.
2. **Multiplayer Support**: A multiplayer mode where players can team up or compete against each other in dungeons.
3. **Expanded Storylines**: More quests and story arcs, including branching storylines based on the player's decisions.
4. **Additional Classes and Monsters**: Introducing new classes, monsters, and items to increase replayability.

### Images

- The Map for better See the dungeon.
  
![Map](/img/map.webp)
  
----

# Technology Used

## Languages

- [Python]
  - Running function for interactive.

## Platforms

- [Github](https://github.com/)
  - Storing code remotely and deployment.
- [Heroku](https://dashboard.heroku.com/)
  - for Deployment .

## Other Tools

- [Visual Studio Code](https://code.visualstudio.com/)
  - To create.
  - Extension: Code Spell Checker;Prettier; Live Server,ESlint,Node.js,PowerShell

----

## Testing

- Following recommendation from Original Assessment it was include true the code rules so any input that is not allow will not brake the game.
- Testing playing the game. Original code for example wold have in during compat if you press Enter it will count as a turn making you reaching HP 0 if you give incorrect command.

### Manual Testing

| What will be Tested? | Expected Outcome | Data Entered | Result |
|----------------------|------------------|--------------|--------|
| Character Class Selection | Player can select a class | Warrior, Mage, Rogue | Pass |
| Combat Mechanics | Combat resolves based on stats | Warrior attacks Goblin | Pass |
| Inventory Management | Items are added/removed from inventory | Potion used | Pass |
| Dungeon Exploration | Player can move through the dungeon | north, explore | Pass |
| Leveling Up | Player's stats increase with leveling | Defeat monster, level up | Pass |

### Validator Testing

- The PEP8 Python formatting [validator](https://pep8ci.herokuapp.com/) initially showed many errors like indentation and passing max Character  when it first scanned my Python code. I took time to correct every little detail, including reformatting lines that were too long, and the current version of the app shows no errors when the Python code is run through the validator. But in the end it should look no messages:
  
![PIP8results](/img/pip8_results.webp)

- The W3C Was also use just in case there was some error in the was a problem in the style.

![W3Validation](/img/w3validator.webp)

----

# Deployment

-The project was Deploy To Heruko following the steps give by the Walkthrough Project Love Sandwiches

## Local

-It is also possible to Deploy this project Local following the steps bellow in case you do not have a Heruko.

### Local Preparation

Local Requirements as follow:

**Requirements:**

- An IDE of your choice, such as [Visual Studio Code](https://code.visualstudio.com/)
- You will net to Set [Git](https://git-scm.com/)
- You will have to set up a connection with an email
- Navigate to git [repository](https://github.com/rdidjurgeit/project3_rdidjurgeit) and find the Green Button:
  
  ```
  <>Code
  ```

- The option to close true HTTPS our Download Zip

## Credits and Contact

### Credits

- THe initial code was take as exemple from the Youtuber  [Tez Fraser](https://www.youtube.com/@TezFraser).

- For some question about the code and underspending ,Chat GBT was use

- Readme example provide by my mentor Patrick Rory.

### Contact

Please feel free to contact me at `didjurgeit.raphael@gmail.com`
