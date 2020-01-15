import random
import sys
from character_class import *
from skills import *
from items import *
from characters import *

def startbattle()
    print("""
    The Goblin runs towards you.
    You feel your Adrenalin rising and you try to;.
    1. Rush forward and disarm the Goblin
    2. Conjure a spell
    """)
    attack_choice = input(">>>")
    if attack_choice == "1":
        print("""
        You rush forwards towards the Goblin.
        The surprised Goblin swings his Sword after you.

        But you react fast and evade it.
        You hit the Sword out of his Hand and then kick him.
        He Stumbles. Which gives you enough Time to get his Sword from the Ground.

        You attack him immediately and stab him into his chest.
        He cries in Agony while you press him to the ground.
        It becomes quiet. You apply some more pressure just to be sure and then pull the sword out.
        You have no scabbard but it should do just fine.
        """)
        player_class = "warrior"
        player1 = player_warrior

    elif attack_choice == "2":
        print()  
        player_class = "mage"
        player1 = player_mage

    else:
        print("""
        You try think of a way out of this situation but the Goblin is fast.
        You barely had time to react when you allready feel the cold of his Iron Dagger penetrating your Skin.

        Panic overcomes you and you look around.

        But its too late. Your vision becomes dark...
        ...
        ...
        ...


        YOU DIED
        """)
        sys.exit()
    players = [player1]
    xpgain(players, 125)

def battle(players, enemies):
    #I give over the list of Enemies and Players

    running = True
    battlexp = enemyxpworth(enemies)
    #Need it to adapt to different Battle size (E.G.: Enemies choosing target)
    player_nr = len(players)
    enemy_nr = len(enemies)

    #Printing stats
    while running:
        print("======================")

        print("\n\n")
        print("NAME                 HP                                     MP")
        for player in players:
            player.get_stats()

        print("\n")

        for enemy in enemies:
            enemy.get_enemy_stats()

        #Player attack phase
        for player in players:

            player.choose_action()
            choice = input("    Choose action: ")
            index = int(choice) - 1

            #Normal Attack
            if index == 0:
                dmg = player.generate_damage()
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(dmg)
                #print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

            #Skill and Spell attacks.
            elif index == 1:
                player.choose_magic()
                magic_choice = int(input("    Choose magic: ")) - 1

                if magic_choice == -1:
                    continue

                spell = player.magic[magic_choice]
                skill_dmg = player.generate_skilldamage(spell)

                current_mp = player.get_mp()

                if spell.cost > current_mp:
                    print("\nNot enough MP\n")
                    continue

                player.reduce_mp(spell.cost)

                if spell.type == "white":
                    player.heal(skill_dmg)
                    print("\n" + spell.name + " heals for", str(skill_dmg), "HP.")
                elif spell.type == "skill" or spell.type == "magic":

                    enemy = player.choose_target(enemies)

                    enemies[enemy].take_skilldamage(skill_dmg, spell)

                    #print("\n" + spell.name + " deals", str(skill_dmg), "points of damage to " + enemies[enemy].name.replace(" ", ""))

                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") + " has died.")
                        del enemies[enemy]
            
            #Items
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
                    player.heal(item.stats)
                    print("\n" + item.name + " heals for", str(item.stats), "HP")
                elif item.type == "elixer":

                    if item.name == "MegaElixer":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print("\n" + item.name + " fully restores HP/MP")                        
        """
        commented out cause only on cheack after enemy turn should be needed
        # Check if battle is over
        # Check if Player won
        if len(enemies) == 0:
            print("You win!")
            running = False

        # Check if Enemy won
        elif len(players) == 0:
            print("Your enemies have defeated you!")
            running = False
        """

        print("\n")
        # Enemy attack phase
        for enemy in enemies:
            enemy_choice = random.randrange(0, 1)
            
            if enemy_choice == 0:
                # Chose attack
                target = random.randrange(0, player_nr)
                enemy_dmg = enemy.generate_damage()

                players[target].take_damage(enemy_dmg)
                #print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg)
                
                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]

            elif enemy_choice == 1:
                spell, skill_dmg = enemy.choose_enemy_spell()
                enemy.reduce_mp(spell.cost)

                if spell.type == "white":
                    enemy.heal(skill_dmg)
                    print(spell.name + " heals " + enemy.name + " for", str(skill_dmg), "HP."                )
                elif spell.type == "skill":

                    target = random.randrange(0, 3)

                    players[target].take_skilldamage(skill_dmg, skill)

                    #print("\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(skill_dmg), "points of damage to " + players[target].name.replace(" ", ""))

                    if players[target].get_hp() == 0:
                        print(players[target].name.replace(" ", "") + " has died.")
                        del players[player]
                #print("Enemy chose", spell, "damage is", skill_dmg)

        # Check if Player won
        if len(enemies) == 0:
            print("You win!")
            xpgain(players, battlexp)
            running = False
        # Check if Enemy won
        elif len(players) == 0:
            print("Your enemies have defeated you!")
            running = False