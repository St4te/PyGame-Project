import pygame
import sys
from Card import *
from Character import *
from Enemy import *
from Kirpich import *
from get_enemy import get_enemy
from get_clicked import clicked_endBtn, clicked_sprite
from load_image import *
from Background import *
from CharacterD import *
from Stats import *
from get_MousePos import *


class Fight:

    def __init__(self, max_mana, curse, enemy_id, card1_id, card2_id, card3_id, card4_id, artifacts):
        self.enemy = get_enemy(enemy_id, curse, artifacts)
        self.character = Character(curse, artifacts, max_mana, card1_id, card2_id, card3_id, card4_id)
        self.ui_group = ui_group
        self.character_group = character_group
        self.back_group = back_group
        self.player = PlayerD(self.character)
        self.enemyD = EnemyD(self.enemy)
        self.back = Background('задник-04.png')
        self.shield_p = Shield('щит.png', self.player)
        self.shield_e = Shield('щит.png', self.enemyD)

    def start(self):
        enemy_live = True
        charecter_live = True
        while enemy_live == True and charecter_live == True:
            cards = self.character.generate_cards()
            screen.fill((0,0,0))
            load_skills(cards)
            self.back_group.draw(screen)
            self.character_group.draw(screen)
            self.ui_group.draw(screen)
            draw_Hp(screen, self.character)
            draw_Hp(screen, self.enemy)
            draw_Mana(screen, self.character)
            draw_Shield(screen, self.enemy)
            draw_Shield(screen, self.character)
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clicked = clicked_sprite(self.ui_group, get_MousePos())
                        if clicked != False:
                            cards = self.character.attack(clicked, self.enemy, cards)
                            screen.fill((0,0,0))
                            load_skills(cards)
                            back_group.draw(screen)
                            character_group.draw(screen)
                            ui_group.draw(screen)
                            draw_Hp(screen, self.character)
                            draw_Hp(screen, self.enemy)
                            draw_Mana(screen, self.character)
                            draw_Shield(screen, self.enemy)
                            draw_Shield(screen, self.character)
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
            self.enemy.attack(self.character)
            charecter_live = self.character.is_live()
            enemy_live = self.enemy.is_live()
        self.game_over()


    def game_over(self):
        print('Game over')



if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('Игра')
    size = WIDTH, HEIGHT = 1366, 768
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.display.flip()

    running = True

    fight = Fight(3, None, 1, 1, 2, 3, 4, None)

    fight.start()

    pygame.quit()

