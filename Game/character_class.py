import random
import math

class Character:
    def __init__(self, name, level, basehp, basemp, baseatk, basespatk, basedf, basespdf, magic, items, xp, xp_worth):
        self.level = level
        self.basehp = basehp
        self.basemp = basemp
        self.baseatk = baseatk
        self.basespatk = basespatk
        self.basedf = basedf
        self.basespdf = basespdf
        self.maxhp = round(basehp * level / 100)
        self.hp = round(basehp * level / 100)
        self.maxmp = round(basemp * level / 100)
        self.mp = round(basemp * level / 100)
        self.atk = round(baseatk * level / 100)
        self.spatk = round(basespatk * level / 100)
        self.df = round(basedf * level / 100)
        self.spdf = round(basespdf * level / 100)
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name
        self.xp = xp
        self.xp_worth = xp_worth        

    #Damage for normal Attacks
    def generate_damage(self):
        return round((2 * self.level / 5 + 2) * 50 * self.atk / 50)

    #Damage for Skills using physical stats
    def generate_skilldamage(self, skill):
        if skill.type == "skill":
            return 2 * self.level / 5 * self.atk / 50 * skill.dmg
        elif skill.type == "magic":
            return 2 * self.level / 5 * self.spatk / 40 * skill.dmg

    def take_damage(self, dmg):
        dmg = (dmg / self.df) + 2
        dmg = round(dmg)
        print(f"""
        {self.name} has received {dmg} Damage.
        """)
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def take_skilldamage(self, dmg, skill):
        if skill.type == "skill":
            dmg = (dmg // self.pdf) + 2
            dmg = round(dmg)
        elif skill.type == "magic":
            dmg = (dmg // self.spdf) + 2
            dmg = round(dmg)
        print(f"""
        {self.name} has received {dmg} Damage.
        """)
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "    " + self.name)
        print("    ACTIONS:")
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1

        print("\n""    MAGIC:")
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" "    ITEMS:")
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x" + str(item["quantity"]) +")")
            i += 1

    def choose_target(self, enemies):
        i = 1

        print("\n" "    TARGET:")
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice



    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                    __________________________________________________ ")
        print(self.name + "  " +
              current_hp + " |" + hp_bar + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "


        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string

        else:
            current_mp = mp_string

        print("                     _________________________              __________ ")
        print(self.name + "    " +
              current_hp +" |" + hp_bar + "|    " +
              current_mp + " |" + mp_bar + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg

#calculates xp that will be gained from enemies
def enemyxpworth(enemies):
    battlexp = 0
    for enemy in enemies:
        battlexp = battlexp + enemy.xp_worth * enemy.level
    return battlexp

#Gives XP and checks for levelup
def xpgain(players, battlexp):
    for player in players:
        print(f"{player.name} has gained {battlexp} XP")
        player.xp = player.xp + battlexp
        lvlupdone = False
        while not lvlupdone:
            if player.xp >= player.level ** 3:
                player.xp - player.level ** 3
                lvlup(player)            
            else:
                xptonextlvl = (player.level ** 3) - player.xp
                print(f"{xptonextlvl} until next level.")
                lvlupdone = True

#does the levelup
def lvlup(self):
    print("You gained a Level.")
    self.level = self.level + 1

    hpgain = round(self.basehp * self.level / 100) - self.maxhp
    print(f"HP +{hpgain}")
    self.maxhp += hpgain
    self.hp = self.maxhp

    mpgain = round(self.basemp * self.level / 100) - self.maxmp
    print(f"MP +{mpgain}")
    self.maxmp += mpgain
    self.mp = self.maxmp

    atkgain = round(self.baseatk * self.level / 100) - self.atk
    print(f"Attack +{atkgain}")
    self.atk += atkgain

    spatkgain = round(self.basespatk * self.level / 100) - self.spatk
    print(f"Special Attack +{spatkgain}")
    self.spatk += spatkgain

    dfgain = round(self.basedf * self.level / 100) - self.df
    print(f"Defense +{dfgain}")
    self.df += dfgain

    spdfgain = round(self.basespdf * self.level / 100) - self.spdf
    print(f"Special Defense +{spdfgain}")
    self.spdf += spdfgain
    print("""       
    """)
