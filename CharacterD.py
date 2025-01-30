import pygame
from load_image import load_image
from to_grayscale import to_grayscale

character_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
ui_group = pygame.sprite.Group()


class PlayerD(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(character_group, all_sprites)
        self.obj = obj
        self.name = obj.location
        self.frames = [load_image('позиция1.png'), load_image('позиция2.png'), load_image('позиция3.png'), load_image('позиция4.png'), load_image('позиция5.png'), load_image('позиция6.png'), load_image('позиция6.png'), load_image('позиция5.png'), load_image('позиция4.png'), load_image('позиция3.png'), load_image('позиция2.png'), load_image('позиция1.png'), ]
        self.cur_image = 0
        self.image = pygame.transform.scale(self.frames[self.cur_image], (333, 222))
        self.rect = self.image.get_rect().move(20,216)

    def update(self):
        self.cur_image = (self.cur_image + 1) % len(self.frames)
        self.image = pygame.transform.scale(self.frames[self.cur_image], (333, 222))


class EnemyD(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(character_group, all_sprites)
        self.obj = obj
        self.name = obj.location
        self.frames = [load_image('враг-поз1.png'), load_image('враг-поз2.png'), load_image('враг-поз3.png'), load_image('враг-поз4.png'), load_image('враг-поз5.png'), load_image('враг-поз5.png'), load_image('враг-поз4.png'), load_image('враг-поз3.png'), load_image('враг-поз2.png'), load_image('враг-поз1.png'), ]
        self.cur_image = 0
        self.image = pygame.transform.scale(self.frames[self.cur_image], (365, 243))
        self.rect = self.image.get_rect().move(1048,216)

    def update(self):
        self.cur_image = (self.cur_image + 1) % len(self.frames)
        self.image = pygame.transform.scale(self.frames[self.cur_image], (365, 243))


class UiSkils(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(ui_group, all_sprites)
        self.obj = obj
        self.image = load_image(obj.location)
        self.rect = self.image.get_rect()


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
