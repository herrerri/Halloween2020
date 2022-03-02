from random import uniform
# Weapons File - Holds all things Weapons!


class Weapon:  # Default Weapon Class
    def __init__(self, name, low, high, inc):
        self.name = name
        self.low_mod = low
        self.high_mod = high
        self.ammo = 0
        self.ammo_increment = inc

    # Returns a random float to be used when attacking monsters
    def use_weapon(self):
        if self.ammo > 0:
            self.ammo -= 1
            return uniform(self.low_mod, self.high_mod)
        else:
            print("No ammo! Failed attack!")
            return 0

    # Adds ammo specified by the weapon's initializer
    def add_ammo(self):
        self.ammo += self.ammo_increment


class HersheyKisses(Weapon):  # HersheyKisses subclass
    def __init__(self):
        super().__init__("HersheyKisses", 1, 1, 0)
        self.ammo = float("inf")


class SourStraws(Weapon):  # SourStraws subclass
    def __init__(self):
        super().__init__("SourStraws", 1, 1.75, 2)


class ChocolateBar(Weapon):  # ChocolateBar subclass
    def __init__(self):
        super().__init__("ChocolateBars", 2, 2.4, 4)


class NerdBombs(Weapon):  # NerdBombs subclass
    def __init__(self):
        super().__init__("NerdBombs", 3.5, 5, 1)
