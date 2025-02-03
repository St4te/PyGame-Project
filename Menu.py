import sys
import pygame
from load_image import load_image


menu_sprites = pygame.sprite.Group()


class MenuUi(pygame.sprite.Sprite):
    def __init__(self, obj):
        super().__init__(menu_sprites)
        self.obj = obj
        self.image = load_image(obj)
        self.rect = self.image.get_rect()


def draw_menu(screen):
    fon = MenuUi('фон-меню.png')
    fon.image = pygame.transform.scale(load_image(fon.obj), (1366,768))
    fon.rect = fon.image.get_rect().move(0,0)
    name = MenuUi('название.png')
    name.image = pygame.transform.scale(load_image(name.obj), (864, 488))
    name.rect = name.image.get_rect().move(250, -150)
    play = MenuUi('играть.png')
    play.image = pygame.transform.scale(load_image(play.obj), (379,107))
    play.rect = play.image.get_rect().move(500,200)
    exit = MenuUi('выйти.png')
    exit.image = pygame.transform.scale(load_image(exit.obj), (379,107))
    exit.rect = exit.image.get_rect().move(500,350)
    menu_sprites.draw(screen)


def clicked_menuBtn(screen, mouse_pos):
    ind = -1
    for sprite in menu_sprites:
        ind += 1
        if sprite.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            if ind == 2:
                print('Start')
                return False
            if ind == 3:
                print('End')
                return sys.exit()
    return True
