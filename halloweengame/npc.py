from random import randint
# NPC File - All things NPC!


class NPC:  # NPC default class
    def __init__(self, name, hp_value, min_atk, max_atk):
        self.houses = []
        self.name = name
        self.hp = hp_value
        self.min_atk = min_atk
        self.max_atk = max_atk
        self.special_dmg = []
        self.dmg_mod = 1

    # Returns the name of the NPC
    def get_name(self):
        return self.name

    # NPC defends against damage taken during game
    def defend(self, value, weapon):
        if weapon in self.special_dmg:
            self.hp -= (value * self.dmg_mod)
        else:
            self.hp -= value
        self.monster_update()

    # NPC attacks user with its own damage during game
    def attack(self):
        return randint(self.min_atk, self.max_atk)

    # 3 Default observable methods
    def add_house(self, house):
        if house not in self.houses:
            self.houses.append(house)

    def remove_house(self, house):
        if house in self.houses:
            self.houses.remove(house)

    def remove_all_houses(self):
        self.houses = []

    # Update for the house to replace a defeated monster
    def monster_update(self):
        if self.hp <= 0:
            for house in self.houses:
                house.replace_monster(self, self.name)


class Person(NPC):  # Person subclass
    def __init__(self):
        super().__init__("Person", 100, -1, -1)
        self.special_dmg.append("ChocolateBars")
        self.special_dmg.append("SourStraws")
        self.special_dmg.append("NerdBombs")
        self.special_dmg.append("HersheyKisses")
        self.dmg_mod = 0


class Zombie(NPC):  # Zombie subclass
    def __init__(self):
        super().__init__("Zombie", randint(50, 100), 0, 10)
        self.special_dmg.append("SourStraws")
        self.dmg_mod = 2


class Vampire(NPC):  # Vampire subclass
    def __init__(self):
        super().__init__("Vampire", randint(100, 200), 10, 20)
        self.special_dmg.append("ChocolateBars")
        self.dmg_mod = 0


class Ghoul(NPC):  # Ghoul subclass
    def __init__(self):
        super().__init__("Ghoul", randint(40, 80), 15, 30)
        self.special_dmg.append("NerdBombs")
        self.dmg_mod = 5


class Werewolf(NPC):  # Werewolf subclass
    def __init__(self):
        super().__init__("Werewolf", 200, 0, 40)
        self.special_dmg.append("ChocolateBars")
        self.special_dmg.append("SourStraws")
        self.dmg_mod = 0
