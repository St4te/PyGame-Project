from random import randint
from Enemy import *



class qw2(Enemy):
    def __init__(self, curse, artifacts, element):
        super().__init__(22, 22, 7, 3, curse, artifacts, 'werewolf-clipart-lg.png', element)

    def attack(self, character):
        self.shield = 0
        a = randint(1, 100)
        if a <= 50:
            self.pattern1(character)
        elif a < 96:
            self.pattern2()
        else:
            self.pattern3(character)

        if self.element == 1:
            damage = 1
            if damage <= character.shield:
                character.shield -= damage
            else:
                character.hp += character.shield - damage
                character.shield = 0
        elif self.element == 2:
            self.hp += 1
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        elif self.element == 3:
            self.shield += 1

    def pattern1(self, character):
        damage = 6
        if damage <= character.shield:
            character.shield -= damage
        else:
            character.hp += character.shield - damage
            character.shield = 0

    def pattern2(self):
        self.hp += 1
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        self.shield = 5

    def pattern3(self, character):
        self.hp += 10
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        self.shield = 2
