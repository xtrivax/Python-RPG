from character_class import *
from items import *
from skills import *
import random
import math

"""
Todo:
In here i will save all characters, including my Player character.
"""

player_warrior = Character("Player:", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)

player_mage = Character("Player:", 5, 416, 535, 359, 535, 239, 379, [fireball, flamethrower], [], 0, 0)


'''
Item Inventory Example;
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},]
'''
