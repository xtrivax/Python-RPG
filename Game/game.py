#!/usr/bin/python3

import random
from character_class import Character
from skills import *
from items import *
from battle_code import *
from enemies import *
from characters import *

prompt = ">>>  "

player1 = startbattle()

print("""
When you enter the room you get attacked by Goblins.
Defend yourself and beat them.
""")


enemy1 = Character("Goblin", 5, 274, 1, 185, 80, 152, 80, [], [], 0, 5)
enemy2 = Character("Hobgoblin", 5, 354, 1, 284, 149, 209, 152, [], [], 0, 10)
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