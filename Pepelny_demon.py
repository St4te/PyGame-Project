from random import randint

class Pepelny_demon:
    def __init__(self, curse, artifacts):
        super().__init__(20, 20, 0, 4, curse, artifacts, 'werewolf-clipart-lg.png')

    def attack(self, character):
        character.mana = character.max_mana
        self.shield = 0
        a = randint(1, 100)
        if a <= 20:
            self.pattern1(character)
        elif a <= 60:
            self.pattern2(character)
        else:
            self.pattern3(character)

    def pattern1(self, character):
        pass