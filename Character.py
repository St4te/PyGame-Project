import sqlite3
from random import choices
from Card import *


class Character:
    def __init__(self, curse, artifacts, mana, card1_id, card2_id, card3_id, card4_id):
        self.curse = curse
        self.location = 'warrior-clipart-lg.png'
        self.artifacts = artifacts
        self.max_mana = mana
        self.mana = mana
        self.card_1 = card1_id
        self.card_2 = card2_id
        self.card_3 = card3_id
        self.card_4 = card4_id
        #self.permanent_cards = [Card(card1_id), Card(card2_id), Card(card3_id), Card(card4_id)]
        self.hp = 50
        self.max_hp = 50
        self.shield = 0
        self.protection = 0

    def generate_cards(self):
        con = sqlite3.connect("cards_bd1.sqlite")
        cur = con.cursor()
        res = cur.execute("SELECT id, rare FROM cards WHERE permanent = 1").fetchall()
        a = []
        b = []
        for i in res:
            a.append(i[0])
            b.append(4 - i[1])
        con.close()
        c = choices(a, weights=b, k=3)
        return [Card(self.card_1), Card(self.card_2), Card(self.card_3), Card(self.card_4), Card(c[0]), Card(c[1]), Card(c[2])]

    def attack(self, card_index, enemy, cards):
        card_index = int(card_index)
        print(card_index)
        if cards[card_index].mana > self.mana:
            return cards
        cards[card_index].apply_card(self, enemy)
        cards[card_index].use()
        return cards

    def is_live(self):
        if self.hp <= 0:
            return False
        return True



    '''def attack(self, card_index, enemy, cards):
        if cards[card_index].mana > self.mana:
            return cards
        cards[card_index].apply_card(self, enemy)
        cards[card_index].use()
        return cards'''

    '''def attack(self, card, enemy, cards):
        if card.mana > self.mana:
            return cards
        card.apply_card(self, enemy)
        for i in cards:
            if card.id == i.id:
                i.use()
        return cards'''
