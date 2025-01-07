import sqlite3


class Card:
    def __init__(self, card_id):
        con = sqlite3.connect("cards_bd1.sqlite")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cards WHERE id = " + str(card_id)).fetchall()
        print(res)
        self.name = res[0][1]
        self.element = res[0][2]
        self.mana = res[0][3]
        self.damage = res[0][4]
        self.rare = res[0][5]
        self.heal = res[0][6]
        self.shield = res[0][7]
        self.duration = res[0][8]
        self.anhit = res[0][9]
        self.hit = res[0][10]
        self.permanent = res[0][11]
        self.special = res[0][12]
        con.close()