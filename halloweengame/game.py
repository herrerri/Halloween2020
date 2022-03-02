from nghbrhd import Neighborhood
from plyr import Player
from random import randint
import time
# Game File


class Game:
    def __init__(self):
        self.player = Player()
        self.neighborhood = Neighborhood()
        self.continue_game = 1

    def get_hp(self):
        return self.player.get_hp()

    def get_weapons(self):
        weapons = []
        total_ammo = []
        for i in range(4):
            weapons.append(self.player.get_weapon(i))
            total_ammo.append(self.player.get_ammo(i))
        return weapons, total_ammo

    def get_monsters(self):
        return self.neighborhood.get_monsters()

    def get_houses(self):
        return self.neighborhood.get_houses()

    def update_houses(self):
        self.neighborhood.sub_houses()
        print(f' There are {self.neighborhood.get_houses()} left to save! \n')
        if self.neighborhood.get_houses() < 1:
            self.win()

    def loss(self):
        print("The neighborhood has been taken over! Game Over!")
        print("Rerun the game to try again!")
        self.continue_game = 0

    def win(self):
        print("The neighborhood has been saved! Congratulations!")
        self.continue_game = 0
        pass

    @staticmethod
    def space_lines():
        print('=======================')

    def initialize(self):
        print("\nWelcome to Halloween RPG 2020!")
        print("Created by Ricardo Herrera-Santos")
        self.space_lines()
        time.sleep(2)
        
        print("Starting Stats")
        self.space_lines()
        time.sleep(1)
        
        print(f"Health Points:  {self.get_hp()}")
        print(f"Total Houses:   {self.get_houses()}")
        print(f"Total Monsters: {self.get_monsters()}")
        self.space_lines()
        time.sleep(2)
        
        print("Inventory")
        self.space_lines()
        time.sleep(1)
        
        for i in range(4):
            print(f"{self.player.get_weapon(i)}: {self.player.get_ammo(i)}")
        self.space_lines()
        time.sleep(2)
        
        print("Neighborhood")
        self.space_lines()
        print(f"\n{self.neighborhood.get_house(0).is_active()}{self.neighborhood.get_house(1).is_active()}")
        print(f"{self.neighborhood.get_house(2).is_active()}{self.neighborhood.get_house(3).is_active()}")
        time.sleep(1)

        input("\nSave all homes (H)! Input any key to begin!")
        self.space_lines()
        self.gameplay()

    def gameplay(self):
        house = 0
        print("NOTE: Enemies have different defensive attributes!")
        time.sleep(2)
        print("Zombies take 2x damage from SourStraws")
        print("Vampires take 0x damage from ChocolateBars")
        print("Ghouls take 5x damage from NerdBombs")
        print("Werewolves take 0x damage from ChocolateBars and SourStraws")
        self.space_lines()
        time.sleep(2)
        print("Arriving at first home!")
        time.sleep(1)
        while self.continue_game == 1:
            if self.neighborhood.get_house(house).is_active() == 'H':
                self.player_turn(house)
            if self.neighborhood.get_house(house).is_active() == 'H':
                self.enemy_turn(house)
            elif house == 3:
                self.win()
            else:
                house += 1
                print("It's Empty... Attempting to move to next home...")
                time.sleep(1)

    def player_turn(self, house):
        time.sleep(2)
        self.space_lines()
        print(f'What would you like to do?')
        print("1 = Attack")
        print("2 = Heal")
        print("3 = Reload")
        print("4 = Inventory")
        self.space_lines()
        action = input()
        self.space_lines()
        if action == '1':
            print("Please select a weapon:")
            self.space_lines()
            for i in range(4):
                print(f'({i}){self.player.get_weapon(i)}: {self.player.get_ammo(i)} uses left')
                print(f'DMG: {self.player.get_dmg(i)}')

            self.space_lines()
            w = int(input())
            if w == 0 or w == 1 or w == 2 or w == 3:
                y = self.player.get_weapon(w)
                x = self.player.attack(w)
                for i in range(self.neighborhood.get_house(house).get_count()):
                    self.neighborhood.get_house(house).get_occupant(i)
                    self.neighborhood.get_house(house).occupant_def(i, x, y)
            else:
                print("Bad input! Try again!")
                self.space_lines()
                self.player_turn(house)

        elif action == '2':
            for i in range(self.neighborhood.get_house(house).get_total()):
                if self.neighborhood.get_house(house).get_occupant(i) == "Person":
                    self.player.defend(self.neighborhood.get_house(house).occupant_atk(i))
            print(f"Attempting Heal...")
            time.sleep(1)
            print(f"HP: {self.player.get_hp()}")
            time.sleep(1)

        elif action == '3':
            weapon = randint(1, 3)
            self.player.reload(weapon)
            print(f"{self.player.get_weapon(weapon)} reloaded!")
            time.sleep(1)

        elif action == '4':
            print("Inventory")
            self.space_lines()
            time.sleep(1)
            for i in range(4):
                print(f'{self.player.get_weapon(i)}: {self.player.get_ammo(i)} uses left')
                print(f'DMG: {self.player.get_dmg(i)}')
            time.sleep(1)
            self.player_turn(house)

        else:
            print("Invalid Input! Try Again!")
            time.sleep(1)
            self.player_turn(house)

    def enemy_turn(self, value):
        self.space_lines()
        c = self.neighborhood.get_house(value).get_count()

        print("Enemies remaining in this house:")
        time.sleep(1)
        for i in range(c):
            print(self.neighborhood.get_house(value).get_occupant(i))
        time.sleep(1)
        print("Enemy Turn... Attacking...")
        time.sleep(2)
        self.space_lines()

        total_atk = 0
        for i in range(c):
            j = randint(0, 6)
            if j == 0:
                total_atk += self.neighborhood.get_house(value).occupant_atk(i)

        if self.player.defend(total_atk) < 0:
            self.loss()
