#codestorage

#nameinput
name_choosen = False
print("""You try to remember your name...
...

...

slowly it comes back to your memories.
Your name was:
""")
while not name_choosen:
    player_name = input(prompt)
    print(f"""Are you sure your name was {player_name}?
    1. Yes
    2. No""")
    remember = input(prompt)
    if remember == "1":
        print()
    else:
        print()



#old classchoosing system


class_choosen = False

while not class_choosen:
    print("Choose your class: Mage or Warrior")
    rpg_class=input(prompt)

    if rpg_class == "warrior":
        #set player to warrior
        player_class = "warrior"
        player1 = player_warrior
        class_choosen = True

    elif rpg_class == "mage":
        #set player to mage

        player_class = "mage"
        player1 = player_mage
        class_choosen = True
        
    else:
        print("This class does not exist, try again.")


