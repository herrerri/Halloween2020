from random import randint
import wpns
# Player File - All things Player


class Player:  # Player class initializer
    def __init__(self):
        self.hp = randint(100, 125)
        self.weapons = [wpns.HersheyKisses(), wpns.SourStraws(),
                        wpns.ChocolateBar(), wpns.NerdBombs()]
        for i in range(9):
            j = randint(1, 3)
            self.weapons[j].add_ammo()

    # Returns Player HP
    def get_hp(self):
        return self.hp

    # Returns a specific name for a weapon the player holds
    def get_weapon(self, i):
        return self.weapons[i].name

    # Returns how much ammo a specific weapon holds
    def get_ammo(self, i):
        return self.weapons[i].ammo

    # Reloads a weapon once based on its ammo count
    def reload(self, i):
        self.weapons[i].add_ammo()

    # Returns a weapons damage range
    def get_dmg(self, i):
        return self.weapons[i].low_mod, self.weapons[i].high_mod

    # Player attacks during the game
    def attack(self, i):
        return randint(10, 20) * self.weapons[i].use_weapon()

    # Player defends against incoming damage
    def defend(self, value):
        self.hp -= value
        if value >= 0:
            print(f"Total dmg taken: {value}")
            print(f"Remaining HP: {self.hp}")
        return self.get_hp()

