import pygame
import sys
from Card import *
from Character import *
from Enemy import *
from Kirpich import *
from sqlite3 import *
from Menu import *
from CharacterD import create_effect
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
        self.character.generate_permanent_cards()
        self.character.generate_cards()
        self.ui_group = ui_group
        self.skills = skillusageeffects_group
        self.character_group = character_group
        self.back_group = back_group
        self.player = PlayerD(self.character)
        self.enemyD = EnemyD(self.enemy)
        self.back = Background(element)
        self.shield_p = Shield('щит.png', self.player)
        self.shield_e = Shield('щит.png', self.enemyD)

    def start(self, screen):
        enemy_live = True
        charecter_live = True
        clock = pygame.time.Clock()
        clockn = pygame.time.Clock()
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
                self.skills.draw(screen)
                ui_group.draw(screen)
                draw_allstats(screen, self.character, self.enemy)
                sprite_change_time += clockn.get_time() / 1000.0  # Получаем время с последнего кадра в секундах
                if sprite_change_time >= sprite_change_interval:
                    self.enemyD.update()
                    self.player.update()  # Смена спрайта
                    sprite_change_time = 0
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clicked = clicked_sprite(self.ui_group, get_MousePos())
                        if clicked != False:
                            create_effect(self.character.cards[int(clicked)], self.character, self.enemyD)
                            self.character.attack(clicked, self.enemy)
                            load_skills(self.character.cards)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            running = False
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                for sprite in self.skills:
                    sprite.update(clock, self.enemyD)
                pygame.display.flip()
                if not self.enemy.is_live():
                    break
                clockn.tick(60)
                clock.tick(165)
            self.character.generate_cards()
            if not self.enemy.is_live():
                enemy_live = self.enemy.is_live()
                break
            self.enemy.attack(self.character)
            self.player.get_hit()
            charecter_live = self.character.is_live()
            enemy_live = self.enemy.is_live()
        return self.game_over(screen, enemy_live)


    def game_over(self,screen, enemy_live):
        next = False
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 170)
        if enemy_live:
            fon = pygame.transform.scale(load_image('экран-поражения.png'), (1366, 768))
            screen.blit(fon, (0, 0))
            self.character.level, self.character.stage = 1, 1
            self.character.set_progress()
        else:
            fon = pygame.transform.scale(load_image('экран-победы.png'), (1366, 768))
            screen.blit(fon, (0, 0))
            next = True
            self.character.set_progress()
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
        self.skills.empty()
        # self.character.generate_permanent_cards()

        print(ui_group,
              back_group,
              character_group,
              skillusageeffects_group)
        return next
