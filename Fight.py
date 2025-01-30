import pygame
import sys
from Card import *
from Character import *
from Enemy import *
from Kirpich import *
from sqlite3 import *
from Menu import *
from get_enemy import *
from get_clicked import clicked_endBtn, clicked_sprite
from load_image import *
from Background import *
from CharacterD import *
from Stats import *
from get_MousePos import *


class Fight:

    def __init__(self, max_mana, curse, enemy_id, character, artifacts, element):
        self.enemy = get_enemy(enemy_id, curse, artifacts, element)
        self.character = character
        self.ui_group = ui_group
        self.character_group = character_group
        self.back_group = back_group
        self.player = PlayerD(self.character)
        self.enemyD = EnemyD(self.enemy)
        self.back = Background('задник_Монтажная область 1.png')
        Element('1314')
        self.shield_p = Shield('щит.png', self.player)
        self.shield_e = Shield('щит.png', self.enemyD)

    def start(self, screen):
        enemy_live = True
        charecter_live = True
        clock = pygame.time.Clock()
        sprite_change_time = 0
        sprite_change_interval = 1 / 6
        while enemy_live == True and charecter_live == True:
            screen.fill((0,0,0))
            load_skills(self.character.cards)
            self.back_group.draw(screen)
            self.character_group.draw(screen)
            self.ui_group.draw(screen)
            draw_allstats(screen, self.character, self.enemy)
            running = True
            while running:
                screen.fill((0, 0, 0))
                back_group.draw(screen)
                character_group.draw(screen)
                ui_group.draw(screen)
                draw_allstats(screen, self.character, self.enemy)
                sprite_change_time += clock.get_time() / 1000.0  # Получаем время с последнего кадра в секундах
                if sprite_change_time >= sprite_change_interval:
                    self.enemyD.update()
                    self.player.update()  # Смена спрайта
                    sprite_change_time = 0
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clicked = clicked_sprite(self.ui_group, get_MousePos())
                        if clicked != False:
                            self.character.attack(clicked, self.enemy)
                            load_skills(self.character.cards)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            running = False
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                pygame.display.flip()
                if not self.enemy.is_live():
                    break
                clock.tick(60)
            self.character.generate_cards()
            self.enemy.attack(self.character)
            charecter_live = self.character.is_live()
            enemy_live = self.enemy.is_live()
        return self.game_over(screen, enemy_live)


    def game_over(self,screen, enemy_live):
        next = False
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 170)
        if enemy_live:
            text = font.render('GAME OVER!', True, (255, 0, 0))
            pygame.draw.rect(screen, (255, 0, 0), (270, 270, 810, 170), 15)
            screen.blit(text, (300, 300))
        else:
            text = font.render('WINNER!', True, (0, 255, 0))
            pygame.draw.rect(screen, (0, 255, 0), (270, 270, 810, 170), 15)
            screen.blit(text, (420, 300))
            next = True
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        self.ui_group.empty()
        self.back_group.empty()
        self.character_group.empty()

        print(self.ui_group.empty(),
        self.back_group.empty(),
        self.character_group.empty())
        return next
