import pygame
from to_grayscale import to_grayscale


def get_clicked(group, mouse_pos):
    pass


def clicked_sprite(group, mouse_pos):
    for sprite in group:
        rect = sprite.rect
        if rect.collidepoint(mouse_pos[0], mouse_pos[1]) and sprite.used == False:
            sprite.image = to_grayscale(sprite.image)
            sprite.used = True
        #return [True, sprite.id]


def clicked_endBtn(mouse_pos):
    pass