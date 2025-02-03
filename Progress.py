import pygame
import sys


def draw_progress(screen, character):
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 60)
    text = font.render(f'Level {character.level}   Stage {character.stage}', True, (255, 255, 255))
    screen.blit(text, (520, 290))
    text = font.render(f'COMPLETED!', True, (0, 255, 0))
    screen.blit(text, (540, 450))
    level, stage = character.get_record()
    text = font.render(f'Record: Level {level}   Stage {stage}', True, (255, 0, 0))
    screen.blit(text, (0, 0))
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