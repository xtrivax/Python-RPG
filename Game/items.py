
class Item:
    def __init__(self, name, type, description, stats):
        self.name = name
        self.type = type
        self.description = description
        self.stats = stats

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Hyper-Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Team-Elixer", "elixer", "Fully restores party's HP/MP", 9999)