import pygame
import sqlite3
from random import randint
import sys
from Card import *
from Character import *
from Enemy import *
from Kirpich import *
from sqlite3 import *
from Menu import *
from Shop import buy_group, draw_shop
from get_enemy import *
from get_clicked import clicked_endBtn, clicked_sprite
from load_image import *
from Background import *
from CharacterD import *
from Stats import *
from get_MousePos import *
from Fight import *
from Shop import *
from Progress import draw_progress


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('Music/музяка.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('KAT (Knight And Throne)')
    size = WIDTH, HEIGHT = 1366, 768
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.display.flip()

    game = True

    while game:

        running = True

        menu_sprites = menu_sprites

        draw_menu(screen)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = clicked_menuBtn(screen, get_MousePos())
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        character = Character(0, 0, 3, 35, 35)
        a = []
        element = randint(1, 4)
        qwerty24 = True
        while qwerty24:
            if character.stage % 2 == 1:
                if character.stage == 5:
                    monster = det_rand_enemy_id(a, True)
                    a.append(monster)
                    fight = Fight(3, None, monster, character, None, element)
                    qwerty24 = fight.start(screen)
                    character.coins += 50
                    if qwerty24:
                        draw_progress(screen, character)
                    character.stage += 1
                else:
                    monster = det_rand_enemy_id(a, False)
                    a.append(monster)
                    fight = Fight(3, None, monster, character, None, element)
                    qwerty24 = fight.start(screen)
                    character.coins += 50
                    if qwerty24:
                        draw_progress(screen, character)
                    character.stage += 1
            else:
                buy_group = buy_group
                draw_shop(screen, character, buy_group)
                draw_progress(screen, character)
                character.stage += 1
            if character.stage == 6:
                a = []
                character.level += 1
                character.stage = 1
                element = randint(1, 4)
    pygame.quit()
