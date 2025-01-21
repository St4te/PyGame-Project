import pygame
from CharacterD import PlayerD



def draw_Hp(screen, character):
    #max_hp = character.max_hp
    #hp = character.hp
    max_hp = 10
    hp = 10
    if isinstance(character, PlayerD) is False:
        pygame.draw.rect(screen, (200, 200, 200), (1096, 10, 250, 20), 100)
        pygame.draw.rect(screen, (255, 0, 0), (1096, 10, 250 * (hp / max_hp), 20), 100)
        pygame.draw.rect(screen, (0, 0, 0), (1096, 10, 250, 20), 3)
        font = pygame.font.Font(None, 25)
        text = font.render(f"{hp}", True, (240, 228, 0))
        screen.blit(text, (1100, 12))
    else:
        pygame.draw.rect(screen, (200, 200, 200), (20, 10, 250, 20), 100)
        pygame.draw.rect(screen, (255, 0, 0), (20, 10, 250 * (hp / max_hp), 20), 100)
        pygame.draw.rect(screen, (0, 0, 0), (20, 10, 250, 20), 3)
        font = pygame.font.Font(None, 25)
        text = font.render(f"{hp}", True, (240, 228, 0))
        screen.blit(text, (24, 12))


def draw_Mana(screen, character):
    #max_mana = character.max_mana
    #mana = character.mana
    max_mana = 5
    mana = 5
    pygame.draw.rect(screen, (200, 200, 200), (20, 50, 180, 20), 100)
    pygame.draw.rect(screen, (30, 30, 255), (20, 50, 180 * (mana / max_mana), 20), 100)
    pygame.draw.rect(screen, (0, 0, 0), (20, 50, 180, 20), 3)
    font = pygame.font.Font(None, 25)
    text = font.render(f"{mana}", True, (240, 228, 0))
    screen.blit(text, (24, 52))


def draw_Shield(screen, character):
    #shield = character.shield
    shield = 22
    if isinstance(character, PlayerD) is False:
        font = pygame.font.Font(None, 30)
        text = font.render(f"{shield}", True, (255, 255, 255))
        screen.blit(text, (1314 - 4 * (len(str(shield)) - 1), 115 - 4 * (len(str(shield)) - 1)))
    else:
        font = pygame.font.Font(None, 30)
        text = font.render(f"{shield}", True, (255, 255, 255))
        screen.blit(text, (44 - 4  * (len(str(shield)) - 1), 115 - 4 * (len(str(shield)) - 1)))