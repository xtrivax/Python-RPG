#!/usr/bin/python3

import random
from character_class import Character
from skills import *
from items import *
from battle_code import battle
from enemies import *

prompt = ">>> "

class_choosen = False

while not class_choosen:
    print("Choose your class: Mage or Warrior")
    rpg_class=input(prompt)

    if rpg_class == "warrior":
        #set player to warrior
        player_class = "warrior"
        class_choosen = True

    elif rpg_class == "mage":
        #set player to mage

        player_class = "mage"
        class_choosen = True
        
    else:
        print("This class does not exist, try again.")

print("""
When you enter the room you get attacked by Goblins.
Defend yourself and beat them.
""")




player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},]


# Instantiate People
if player_class == "warrior":
    player_spells = [slash, jstrike, blade, cure, cure2]
    player1 = Character("Vamirio:", 5, 25, 10, 20, 11, 14, 15, player_spells, player_items, 0, 0)
elif player_class == "mage":
    player_spells = [fireball, flamethrower, eruption, cure, cure2]
    player1 = Character("Vamirio:", 5, 416, 535, 359, 535, 239, 379, player_spells, player_items, 0, 0)
else:
    print("""Error in class selection. Loading Backupclass.
    Godclass loaded.""")
    player_spells = [fireball, flamethrower, eruption, slash, jstrike, blade, cure, cure2]
    player1 = Character("Vamirio:", 5, 6260, 132, 500, 100, 34, 20, player_spells, player_items, 0, 0)   



enemy1 = goblin
enemy2 = hobgoblin

players = [player1]
enemies = [enemy1, enemy2]

print("AN ENEMY ATTACKS!")

battle(players, enemies)

print("""
You have defeated the enemy

You can now proceed to the next room

...

...

To be continued
""")