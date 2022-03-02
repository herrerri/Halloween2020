from hom import Home
# Neighborhood File - Short and Sweet


class Neighborhood:  # Neighborhood initializer
    def __init__(self):
        self.houses = 4
        self.grid = []

        for i in range(self.houses):
            h = Home()
            if h.get_count() < 1:
                self.houses -= 1
            self.grid.append(h)

    # Returns total number of monsters in neighborhood
    def get_monsters(self):
        count = 0
        for i in range(self.houses):
            count += self.grid[i].monster_count
        return count

    # Returns total number of houses in neighborhood
    def get_houses(self):
        return self.houses

    # Subtracts a house from the neighborhood count
    def sub_houses(self):
        self.houses -= 1

    # Gets a specific house from the neighborhood
    def get_house(self, value):
        return self.grid[value]
