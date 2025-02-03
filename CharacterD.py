import pygame
from load_image import load_image
from to_grayscale import to_grayscale

character_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
ui_group = pygame.sprite.Group()
skillusageeffects_group = pygame.sprite.Group()


class PlayerD(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(character_group, all_sprites)
        self.obj = obj
        self.name = obj.location
        self.frames = [load_image('позиция1.png'), load_image('позиция2.png'), load_image('позиция3.png'), load_image('позиция4.png'), load_image('позиция5.png'), load_image('позиция6.png'), load_image('позиция6.png'), load_image('позиция5.png'), load_image('позиция4.png'), load_image('позиция3.png'), load_image('позиция2.png'), load_image('позиция1.png'), ]
        self.cur_image = 0
        self.image = pygame.transform.scale(self.frames[self.cur_image], (333, 222))
        self.rect = self.image.get_rect().move(20,216)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.cur_image = (self.cur_image + 1) % len(self.frames)
        self.image = pygame.transform.scale(self.frames[self.cur_image], (333, 222))

    def get_hit(self):
        self.image = pygame.transform.scale(load_image('урон-игрок.png'), (333, 222))


class EnemyD(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(character_group, all_sprites)
        self.obj = obj
        self.name = obj.location
        self.frames = [load_image('враг-поз1.png'), load_image('враг-поз2.png'), load_image('враг-поз3.png'), load_image('враг-поз4.png'),
                       load_image('враг-поз5.png'), load_image('враг-поз5.png'), load_image('враг-поз4.png'), load_image('враг-поз3.png'),
                       load_image('враг-поз2.png'), load_image('враг-поз1.png'), ]
        self.cur_image = 0
        self.image = pygame.transform.scale(self.frames[self.cur_image], (365, 243))
        self.rect = self.image.get_rect().move(1048,216)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.cur_image = (self.cur_image + 1) % len(self.frames)
        self.image = pygame.transform.scale(self.frames[self.cur_image], (365, 243))

    def get_hit(self):
        self.image = pygame.transform.scale(load_image('урон-враг.png'), (365, 243))


class UiSkils(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(ui_group, all_sprites)
        self.obj = obj
        self.id = obj.id
        self.image = load_image(obj.location)
        self.rect = self.image.get_rect()


class SkillUsageEffects(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__(skillusageeffects_group)
        self.id = id
        self.base = {2 : ['скил-2.png', 232, 237, 180, 220], 3 : ['скил-3.png', 276, 154, 190, 250], 5 : ['скил-5.png', 460, 325, 1200, -325],
                     7 : ['скил-7.png', 322, 178, 240, 220], 8 : ['скил-8.png', 160, 160, 160, 230], 10 : ['скил-10.png', 230, 128, 180, 250],
                     11 : ['скил-11.png', 198, 119, 160, 250]}
        self.image = pygame.transform.scale(load_image(self.base[id][0]), (self.base[id][1], self.base[id][2]))
        self.rect = self.image.get_rect().move(self.base[id][3], self.base[id][4])
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2000
        self.fps = 165

    def update(self, clock, enemyD): #character, enemy):
        if not pygame.sprite.collide_mask(self, enemyD):
            if not self.id == 5:
                self.rect.x += self.speed * clock.tick(self.fps) / 1000
            else:
                self.rect.y += self.speed * clock.tick(self.fps) / 1000
                self.rect.x -= self.speed * clock.tick(self.fps) / 1000
        else:
            self.kill()

def load_skills(spisok):
    distance = 25
    for i in ui_group:
        i.kill()
    ui_group.empty()
    place, not_inf = 0, 0
    for card in spisok:
        skilui = UiSkils(card)
        skil = card
        if not skil.can_use:
            skilui.image = to_grayscale(skilui.image)
        place += 1
        not_inf += 1
        skilui.rect = skilui.image.get_rect().move(30 + 149 * (not_inf - 1) + distance * (place - 1), 520)
        if place == 4:
            place += 5


def create_effect(card, character, enemyD):
    if card.can_use and character.mana >= card.mana:
        if card.id in [2, 3, 5, 7, 8, 10, 11]:
            enemyD.get_hit()
            effect = SkillUsageEffects(card.id)
            
