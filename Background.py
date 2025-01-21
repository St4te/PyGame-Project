from CharacterD import all_sprites, PlayerD
from load_image import load_image
import pygame

all_sprites = all_sprites
back_group = pygame.sprite.Group()


class Background(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__(back_group, all_sprites)
        self.image = pygame.transform.scale(load_image(id), (1366, 768))
        self.rect = self.image.get_rect().move(0,0)


class Shield(pygame.sprite.Sprite):
    def __init__(self, id, character):
        super().__init__(back_group, all_sprites)
        self.image = pygame.transform.scale(load_image(id), (100, 50))
        if isinstance(character, PlayerD) is False:
            self.rect = self.image.get_rect().move(1270, 100)
        else:
            self.rect = self.image.get_rect().move(0, 100)

class EndStep(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(back_group, all_sprites)
        #self.image =
        pass


