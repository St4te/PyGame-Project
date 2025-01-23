from random import randint
from Enemy import *



class Kirpich(Enemy):
    def __init__(self, curse, artifacts):
        super().__init__(20, 20, 0, 4, curse, artifacts, 'werewolf-clipart-lg.png')

    def attack(self, character):
        character.mana = character.max_mana
        self.shield = 0
        a = randint(1, 100)
        if a <= 60:
            self.pattern1(character)
        elif a < 100:
            self.pattern2()
        else:
            self.pattern3(character)

    def pattern1(self, character):
        character.hp -= 10

    def pattern2(self):
        self.hp += 1
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        self.shield = 3

    def pattern3(self, character):
        character.hp -= 100
