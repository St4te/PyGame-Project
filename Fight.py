class Fight:

    def __init__(self, max_mana, curse, enemy_id, card1_id, card2_id, card3_id, card4_id, artifacts):
        self.enemy = get_enemy(enemy_id, curse, artifacts)
        self.character = Character(curse, artifacts, max_mana, card1_id, card2_id, card3_id, card4_id)

    def start(self):
        enemy_live = True
        charecter_live = True
        while enemy_live == True and charecter_live == True:
            cards = self.character.generate_cards()
            d = int(input())
            while d != 10:
                self.character.attack(cards[d], self.enemy, cards)
                d = int(input())
            self.enemy.attack(self.character)
            charecter_live = self.character.is_live()
            enemy_live = self.enemy.is_live()
        self.game_over()


    def game_over(self):
        print('Game over')

