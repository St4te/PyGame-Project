import sqlite3
from random import choices
from Card import *


class Character:
    def __init__(self, curse, artifacts, mana, max_hp, hp):
        self.curse = curse
        self.location = 'warrior-clipart-lg.png'
        self.artifacts = artifacts
        self.max_mana = mana
        self.mana = mana
        self.card_1 = None
        self.card_2 = None
        self.card_3 = None
        self.card_4 = None
        self.generate_permanent_cards()
        self.cards = []
        self.prev_cards = []
        self.generate_cards()

        #self.permanent_cards = [Card(card1_id), Card(card2_id), Card(card3_id), Card(card4_id)]
        self.hp = hp
        self.max_hp = max_hp
        self.shield = 0
        self.protection = 0

    def generate_cards(self):
        con = sqlite3.connect("cards_bd1.sqlite")
        cur = con.cursor()
        res = cur.execute("SELECT id, rare FROM cards WHERE anpermanent = 1").fetchall()
        a = []
        b = []
        for i in res:
            a.append(i[0])
            b.append(4 - i[1])
        con.close()
        c = choices(a, weights=b, k=3)
        self.prev_cards = self.cards[:]
        self.cards = [Card(self.card_1), Card(self.card_2), Card(self.card_3), Card(self.card_4), Card(c[0]), Card(c[1]), Card(c[2])][:]

    def generate_permanent_cards(self):
        con = sqlite3.connect("cards_bd1.sqlite")
        cur = con.cursor()
        res = cur.execute("SELECT id, rare FROM cards WHERE permanent = 1").fetchall()
        a = []
        b = []
        for i in res:
            a.append(i[0])
            b.append(4 - i[1])
        con.close()
        c = choices(a, weights=b, k=4)
        self.card_1 = c[0]
        self.card_2 = c[1]
        self.card_3 = c[2]
        self.card_4 = c[3]

    def attack(self, card_index, enemy):
        card_index = int(card_index)
        if self.cards[card_index].mana <= self.mana:
            self.cards[card_index].apply_card(self, enemy)
            self.cards[card_index].use()

    def is_live(self):
        if self.hp <= 0:
            return False
        return True
