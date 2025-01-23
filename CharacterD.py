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
        self.image = pygame.transform.scale(load_image(obj.location), (300, 248))
        self.rect = self.image.get_rect().move(20,216)


class EnemyD(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(character_group, all_sprites)
        self.obj = obj
        self.name = obj.location
        self.image = pygame.transform.scale(load_image(obj.location), (300, 248))
        self.rect = self.image.get_rect().move(1048,216)


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

