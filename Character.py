import sqlite3
from random import choices
from Card import *


class Character:
    def __init__(self, curse, artifacts, mana, max_hp, hp):
        self.curse = curse
        self.level = 1
        self.stage = 1
        #self.get_progress()
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
        self.coins = 0

    def generate_cards(self):
        self.mana = self.max_mana
        #self.shield = 0
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

    def buy(self, price, delta_max_hp, delta_hp, delta_max_mana):
        if price <= self.coins:
            self.coins -= price
            self.max_hp += delta_max_hp
            self.hp += delta_hp
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.max_mana += delta_max_mana

    def get_record(self):
        con = sqlite3.connect("saves_bd.sqlite")
        cur = con.cursor()
        res = cur.execute("SELECT level, stage FROM saves WHERE id = 2").fetchall()
        return res[0][:]

    def get_progress(self):
        con = sqlite3.connect("saves_bd.sqlite")
        cur = con.cursor()
        res = cur.execute("SELECT level, stage FROM saves WHERE id = 1").fetchall()
        self.level, self.stage = res[0][:]

    def set_progress(self):
        con = sqlite3.connect("saves_bd.sqlite")
        cur = con.cursor()
        res_record = cur.execute("SELECT level, stage FROM saves WHERE id = 2").fetchall()
        s1 = '''UPDATE saves
    SET level = '''
        s2 = ''', stage = '''
        s3 = '''
    WHERE id = '''
        s = s1 + str(self.level) + s2 + str(self.stage)
        if res_record[0][0] < self.level or res_record[0][0] == self.level and res_record[0][1] < self.stage:
            cur.execute(s)
        else:
            cur.execute(s + s3 + '1')
        con.commit()
