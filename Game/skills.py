import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    #To be replaced by generate_spelldagamge
    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)





#Spells and Abilitys

# Create Damage Skills
fireball = Spell("Fire", 25, 600, "skill")
flamethrower = Spell("flamethrower", 40, 1200, "skill")
eruption = Spell("eruption", 60, 2000, "skill")
slash = Spell("Sword Slash", 25, 600, "skill")
jstrike = Spell("Jaizhenju Strike", 35, 1000, "skill")
blade = Spell("Seeking Blade", 60, 2000, "skill")

# Create white Magic
cure = Spell("Small Heal", 25, 620, "white")
cure2 = Spell("Heal", 32, 1500, "white")