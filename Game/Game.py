import random
from defs import Person, Spell, Item
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



# Create Damage "Spells"
fire = Spell("Fire", 25, 600, "ability")
ember = Spell("ember", 25, 600, "ability")
flamethrower = Spell("flamethrower", 40, 1200, "ability")
eruption = Spell("eruption", 60, 2000, "ability")
slash = Spell("Sword Slash", 25, 600, "ability")
jstrike = Spell("Jaizhenju Strike", 35, 1000, "ability")
blade = Spell("Seeking Blade", 60, 2000, "ability")

# Create white Magic
cure = Spell("Small Heal", 25, 620, "white")
cure2 = Spell("Heal", 32, 1500, "white")


# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Hyper-Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Team-Elixer", "elixer", "Fully restores party's HP/MP", 9999)


enemy_spells = [fire, flamethrower, cure2]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},]


# Instantiate People
if player_class == "warrior":
    player_spells = [slash, jstrike, blade, cure, cure2]
    player1 = Person("Vamirio:", 6260, 132, 500, 34, player_spells, player_items)
elif player_class == "mage":
    player_spells = [fire, ember, flamethrower, eruption, cure, cure2]
    player1 = Person("Vamirio:", 3260, 432, 300, 50, player_spells, player_items)
else:
    print("""Error in class selection. Loading Backupclass.
    Godclass loaded.""")
    player_spells = [fire, ember, flamethrower, eruption, slash, jstrike, blade, cure, cure2]
    player1 = Person("Vamirio:", 3260, 132, 300, 34, player_spells, player_items)    


enemy1 = Person("Goblin", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Hobgoblin", 5000, 701, 525, 25, enemy_spells, [])


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
