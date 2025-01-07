import sqlite3


class Character:
    def __init__(self, curse, artifacts, mana, card1_id, card2_id, card3_id, card4_id):
        self.curse = curse
        self.artifacts = artifacts
        self.mana = mana
        self.permanent_cards = [Card(card1_id), Card(card2_id), Card(card3_id), Card(card4_id)]
        self.hp = 50
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
        

    def is_live(self):
        if self.hp <= 0:
            return False
        return True