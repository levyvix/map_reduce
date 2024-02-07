import random

class Village:
    def __init__(self) -> None:
        self.Village = random.uniform(1000, 5000)
        self.cheat_rate = random.uniform(0.05, 0.15)

    def go_fishing(self):
        if random.uniform(0,1) < self.cheat_rate:
            cheat = 1
            fish_taken = self.population * 2
        else:
            cheat = 0
            fish_taken = self.population * 1

        return fish_taken, cheat