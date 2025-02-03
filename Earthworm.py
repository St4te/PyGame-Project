from random import randint
from Enemy import *
from Character import *

class Earthworm(Enemy):
    def __init__(self, curse, artifacts, element):
        super().__init__(80, 80, 0, 3, curse, artifacts, 'werewolf-clipart-lg.png', element)
        self.hidden = 0
        self.lost_hp = 0

    def attack(self, character):
        self.shield = 0
        self.lost_hp = 0
        for i in character.prev_cards:
            if not i.can_use:
                self.lost_hp += i.damage
        if self.hidden > 0:
            self.hp += 3
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.hidden -= 1
            for i in character.cards:
                i.damage = 0
        elif self.lost_hp >= 8:
            a = randint(1, 100)
            if a <= 20:
                self.pattern1(character)
            elif a <= 50:
                self.pattern2(character)
            else:
                self.pattern3(character)
        else:
            a = randint(1, 100)
            if a <= 40:
                self.pattern2(character)
            else:
                self.pattern3(character)

    def pattern1(self, character):
        self.hidden = 3
        for i in character.cards:
            i.damage = 0

    def pattern2(self, character):
        self.shield = self.lost_hp / 2

    def pattern3(self, character):
        damage = 4
        if damage <= character.shield:
            character.shield -= damage
        else:
            character.hp += character.shield - damage
            character.shield = 0