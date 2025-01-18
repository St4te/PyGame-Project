import sqlite3
from random import choices


class Character:
    def __init__(self, curse, artifacts, mana, card1_id, card2_id, card3_id, card4_id):
        self.curse = curse
        self.artifacts = artifacts
        self.max_mana = mana
        self.mana = mana
        self.permanent_cards = [Card(card1_id), Card(card2_id), Card(card3_id), Card(card4_id)]
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
        return [self.permanent_cards, [Card(c[0]), Card(c[1]), Card(c[2])]]

    def attack(self, card, enemy, cards):
        if card.mana > self.mana:
            return cards
        card.apply_card(self, enemy)
        a = [[], []]
        for i in cards[0]:
            if i.id != card.id:
                a[0].append(i)
        for i in cards[1]:
            if i.id != card.id:
                a[1].append(i)
        return a

    def is_live(self):
        if self.hp <= 0:
            return False
        return True
