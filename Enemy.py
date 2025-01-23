class Enemy:
    def __init__(self, max_hp, hp, shield, protection, curse, artifacts, location):
        self.hp = hp
        self.max_hp = max_hp
        self.protection = protection
        self.shield = shield
        self.curse = curse
        self.artifacts = artifacts
        self.location = location


    def attack(self):
        pass

    def is_live(self):
        if self.hp <= 0:
            return False
        return True
