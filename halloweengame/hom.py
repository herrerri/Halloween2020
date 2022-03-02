from random import randint
import npc
# Home File - Once again all things Home (really just Home)


class Home:  # Home initializer
    def __init__(self):
        self.games = []
        self.occupants = []
        self.total_count = randint(0, 10)
        self.monster_count = self.total_count
        for i in range(self.monster_count):
            monster = npc.Person()
            monster_type = randint(0, 3)
            if monster_type == 0:
                monster = npc.Zombie()
            elif monster_type == 1:
                monster = npc.Vampire()
            elif monster_type == 2:
                monster = npc.Ghoul()
            elif monster_type == 3:
                monster = npc.Werewolf()
            monster.add_house(self)
            self.occupants.append(monster)

    #  Returns total occupants, not just monsters
    def get_total(self):
        return self.total_count

    #  Returns current total monster count
    def get_count(self):
        return self.monster_count

    #  Returns whether house has monsters residing or not
    def is_active(self):
        if self.monster_count > 0:
            return 'H'
        else:
            return 'X'

    #  Returns a specific occupant within the house
    def get_occupant(self, value):
        return self.occupants[value].get_name()

    # Attack with a specific occupant in the house
    def occupant_atk(self, value):
        return self.occupants[value].attack()

    # Defend with a specific occupant in the house
    def occupant_def(self, value, weapon, atk):
        self.occupants[value].defend(weapon, atk)

    # Observer method called by NPC class when updating
    # a monster that has been defeated
    def replace_monster(self, monster, name):
        self.monster_count -= 1
        print(f'{name} defeated!')
        self.occupants.remove(monster)
        p = npc.Person()
        self.occupants.append(p)

        if self.monster_count < 1:
            print("House has been saved!\n")
            self.house_update()

    # Observable methods that should have interacted
    # with game (ran out of time before implementing)
    def house_update(self):
        for game in self.games:
            game.update_houses(self)

    def add_game(self, observer):
        if observer not in self.games:
            self.games.append(observer)

    def remove_game(self, observer):
        if observer in self.games:
            self.games.remove(observer)

    def remove_all_games(self):
        self.games = []
