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
fireball = Spell("Fire", 5, 60, "skill")
flamethrower = Spell("flamethrower", 8, 80, "skill")
eruption = Spell("eruption", 15, 120, "skill")
slash = Spell("Sword Slash", 5, 60, "skill")
jstrike = Spell("Jaizhenju Strike", 8, 80, "skill")
blade = Spell("Seeking Blade", 15, 120, "skill")

# Create white Magic
cure = Spell("Small Heal", 25, 620, "white")
cure2 = Spell("Heal", 32, 1500, "white")