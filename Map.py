import pygame
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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Игра')
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
        coins = 0
        stage = 1
        level = 1
        a = []
        element = 1
        qwerty24 = True
        while qwerty24:
            if stage % 2 == 1:
                monster = det_rand_enemy_id(a, False)
                a.append(monster)
                fight = Fight(3, None, monster, character, None, 1)
                qwerty24 = fight.start(screen)
                coins += 50
                stage += 1
                if stage == 6:
                    a = []
                    stage = 1
                    level += 1
                print(stage)
            else:
                buy_group = buy_group
                draw_shop(screen, character, coins, buy_group)
                stage += 1
    pygame.quit()