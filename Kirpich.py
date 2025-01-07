from random import randint


class Kirpich(Enemy):
    def __init__(self, curse, artifacts):
        super().__init__(20, 20, 0, 4, curse, artifacts)

    def attack(self, character):
        self.shield = 0
        a = randint(1, 100)
        if a <= 60:
            self.pattern1()
        elif a < 100:
            self.pattern2()
        else:
            self.pattern3()

    def pattern1(self):
        pass

    def pattern2(self):
        self.hp += 1
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        self.shield = 3

    def pattern3(self):
        pass