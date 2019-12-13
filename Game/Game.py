import random
from character_class import Character
from skills import *
from items import Item
from battle_code import battle

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






# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Hyper-Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Team-Elixer", "elixer", "Fully restores party's HP/MP", 9999)


enemy_spells = [fireball, flamethrower, cure2]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},]


# Instantiate People
if player_class == "warrior":
    player_spells = [slash, jstrike, blade, cure, cure2]
    player1 = Character("Vamirio:", 1, 100, 30, 500, 100, 34, 20, player_spells, player_items)
elif player_class == "mage":
    player_spells = [fireball, flamethrower, eruption, cure, cure2]
    player1 = Character("Vamirio:", 1, 3260, 432, 300, 500, 20, 50, player_spells, player_items)
else:
    print("""Error in class selection. Loading Backupclass.
    Godclass loaded.""")
    player_spells = [fireball, flamethrower, eruption, slash, jstrike, blade, cure, cure2]
    player1 = Character("Vamirio:", 1, 6260, 132, 500, 100, 34, 20, player_spells, player_items)   


enemy1 = Character("Goblin", 1, 1250, 130, 560, 1, 325, 1, enemy_spells, [])
enemy2 = Character("Hobgoblin", 1, 5000, 701, 525, 1, 25, 1,enemy_spells, [])


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