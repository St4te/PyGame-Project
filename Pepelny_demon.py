from random import randint
from Enemy import *
from Character import *

class Pepelny_demon(Enemy):
    def __init__(self, curse, artifacts, element):
        super().__init__(60, 60, 0, 3, curse, artifacts, 'werewolf-clipart-lg.png', element)

    def attack(self, character):
        self.shield = 0
        a = randint(1, 100)
        if a <= 40:
            self.pattern1(character)
        elif a <= 80:
            self.pattern2(character)
        else:
            self.pattern3(character)

    def pattern1(self, character):
        damage = 7
        if damage <= character.shield:
            character.shield -= damage
        else:
            character.hp += character.shield - damage
            character.shield = 0
        self.shield = 4

    def pattern2(self, character):
        damage = 0
        for i in range(4):
            if character.prev_cards[i].can_use:
                damage += character.prev_cards[i].damage
        if damage != 0:
            if damage <= character.shield:
                character.shield -= damage
            else:
                character.hp += character.shield - damage
                character.shield = 0
        else:
            self.pattern1(character)

    def pattern3(self, character):
        heal = 0
        for i in character.cards:
            heal += i.mana
        heal *= 2
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        self.shield = 4
