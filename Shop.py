import sys
import pygame
from load_image import load_image
from get_clicked import clicked_shop
from to_grayscale import to_grayscale
from Stats import draw_Hp, draw_Mana
from get_MousePos import get_MousePos


buy_group = pygame.sprite.Group()


class BuyBtn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(buy_group)
        self.image = pygame.transform.scale(load_image('купить-кнопка.png'), (256,51))
        self.rect = self.image.get_rect()
        self.uses = 1


def draw_shop(screen, character, group):
    group.empty()
    screen.fill((0,0,0))
    up_hp = BuyBtn()
    up_hp.rect = up_hp.rect.move(150, 400)
    up_mana = BuyBtn()
    up_mana.rect = up_mana.rect.move(575, 400)
    fill_hp = BuyBtn()
    fill_hp.rect = fill_hp.rect.move(1000, 400)
    draw_upgrades(screen)
    group.draw(screen)
    font = pygame.font.Font(None, 50)
    text = font.render(f'Монеты: {character.coins}', True, (255, 255, 255))
    screen.blit(text, (40, 140))
    draw_Hp(screen, character)
    draw_Mana(screen, character)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_upgrades(screen)
                clicked_shop(screen, group, character, get_MousePos())
                running = clicked_continue(get_MousePos())
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def clicked_continue(mouse_pos):
    if pygame.Rect(570, 650, 256, 90).collidepoint(mouse_pos[0], mouse_pos[1]):
        return False
    return True

def draw_upgrades(screen):
    screen.fill((0,0,0))
    fon = load_image('фон-меню.png')
    screen.blit(fon, (0, 0))
    fon = pygame.transform.scale(load_image('продолжить.png'), (256, 90))
    screen.blit(fon, (570, 650))
    font = pygame.font.Font(None, 50)
    text = font.render('Увеличить макс. ХП на 1', True, (255, 255, 255))
    screen.blit(text, (70, 290))
    text = font.render('Стоимость: 30 монет', True, (255, 255, 255))
    screen.blit(text, (120, 340))
    text = font.render('Увеличить макс. Ману на 1', True, (255, 255, 255))
    screen.blit(text, (500, 260))
    text = font.render('Стоимость: 30 монет', True, (255, 255, 255))
    screen.blit(text, (520, 340))
    text = font.render('Восполнить ХП на 2', True, (255, 255, 255))
    screen.blit(text, (960, 290))
    text = font.render('Стоимость: 30 монет', True, (255, 255, 255))
    screen.blit(text, (960, 340))
    pygame.display.flip()
