import random
from defs import Person, Spell, Item

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

print("Welcome to Dungeon")



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
    player_spells = [slash, jstrike, blade, eruption, cure, cure2]
    player1 = Person("Vamirio:", 3260, 132, 300, 34, player_spells, player_items)
elif player_class == "mage":
    player_spells = [fire, ember, flamethrower, eruption, cure, cure2]
    player1 = Person("Vamirio:", 3260, 132, 300, 34, player_spells, player_items)
else:
    print("""Error in class selection. Loading Backupclass.
    Godclass loaded.""")
    player_spells = [fire, ember, flamethrower, eruption, slash, jstrike, blade, cure, cure2]
    player1 = Person("Vamirio:", 3260, 132, 300, 34, player_spells, player_items)    


enemy1 = Person("Goblin", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Hobgoblin", 5000, 701, 525, 25, enemy_spells, [])


players = [player1]
enemies = [enemy1, enemy2]

player_nr = len(players)
enemy_nr = len(enemies)

running = True
i = 0

print("AN ENEMY ATTACKS!")

while running:
    print("======================")

    print("\n\n")
    print("NAME                 HP                                     MP")
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print("\nNot enough MP\n")
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print("\n" + spell.name + " heals for", str(magic_dmg), "HP.")
            elif spell.type == "ability":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)

                print("\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace(" ", ""))

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print("\n" + "None left...")
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + item.name + " heals for", str(item.prop), "HP")
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print("\n" + item.name + " fully restores HP/MP")
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print("\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if Player won
    if defeated_enemies == enemy_nr:
        print("You win!")
        running = False

    # Check if Enemy won
    elif defeated_players == player_nr:
        print("Your enemies have defeated you!")
        running = False

    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 1)

        if enemy_choice == 0:
            # Chose attack
            target = random.randrange(0, player_nr)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(spell.name + " heals " + enemy.name + " for", str(magic_dmg), "HP."                )
            elif spell.type == "ability":

                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)

                print("\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage to " + players[target].name.replace(" ", ""))

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[player]
            #print("Enemy chose", spell, "damage is", magic_dmg)
