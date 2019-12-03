#The Dungeon RPG
prompt = ">>> "

class_choosen = False

while not class_choosen:
    print("Choose your class: Mage or Warrior")
    rpg_class=input(prompt)

    if rpg_class == warrior:
        #set player to warrior
        warrior = {
            display_name= "Hans"
            attacks=[Slash],
            maximum_health=30,
            maximum_stamina=30,
            strength=8,
            defence=10,
        }
        class_choosen = True

    elif rpg_class == mage:
        #set player to mage

        mage = {
            display_name= "Merlin",
            attacks=[Firebolt],
            maximum_health=30,
            maximum_mana=25,
            magic=12,
            strength=2,
            defence=6,
        }
        class_choosen = True
        
    else:
        print("This class does not exist, try again.")