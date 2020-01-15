from character_class import *
from items import *
from skills import *
import random
import math

#To do: put all enemies into this file and then adjust their stats
#(name, level, basehp, basemp, baseatk, basespatk, basedf, basespdf, magic, items, xp, xp_worth)

#goblins
goblin = Character("Goblin", 100, 274, 1, 185, 80, 152, 80, [], [], 0, 5)
hobgoblin = Character("Hobgoblin", 100, 354, 1, 284, 149, 209, 152, [], [], 0, 10)

#slimes
slime = Character("Slime", 100, 304, 1, 80, 125, 180, 200, [], [], 0, 5)

#insects
