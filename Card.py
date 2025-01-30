import sqlite3


class Card:
    def __init__(self, card_id):
        con = sqlite3.connect("cards_bd1.sqlite")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cards WHERE id = " + str(card_id)).fetchall()
        self.id = card_id
        self.location = res[0][1]
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
        self.anpermanent = res[0][12]
        self.special = res[0][13]
        self.uses = res[0][14]
        self.can_use = True

    def use(self):
        self.uses -= 1
        if self.uses <= 0:
            self.can_use = False

    def apply_card(self, character, enemy):
        if self.can_use:
            character.shield += self.shield
            character.hp += self.heal
            if character.hp > character.max_hp:
                character.hp = character.max_hp
            character.mana -= self.mana
            if self.damage <= enemy.shield:
                enemy.shield -= self.damage
            else:
                enemy.hp += enemy.shield - self.damage
                enemy.shield = 0
        else:
            print('Использованно')
