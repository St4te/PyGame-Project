import pygame
from to_grayscale import to_grayscale
from Stats import draw_Hp, draw_Mana


def clicked_shop(screen, group, character, mouse_pos):
    index = -1
    for sprite in group:
        index += 1
        rect = sprite.rect
        if rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            if index == 0:
                if sprite.uses:
                    sprite.uses -= 1
                    character.buy(30, 1, 0, 0)
            elif index == 1:
                if sprite.uses:
                    sprite.uses -= 1
                    character.buy(30, 0, 0, 1)
            elif index == 2:
                if sprite.uses:
                    sprite.uses -= 1
                    character.buy(30, 0, 2, 0)
    group.draw(screen)
    font = pygame.font.Font(None, 50)
    text = font.render(f'Монеты: {character.coins}', True, (255, 255, 255))
    screen.blit(text, (40, 140))
    draw_Hp(screen, character)
    draw_Mana(screen, character)
    pygame.display.flip()


def clicked_sprite(group, mouse_pos):
    index = -1
    for sprite in group:
        index += 1
        rect = sprite.rect
        if rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            print(index)
            return str(index)
    return False


def clicked_endBtn():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True
    return False
