import pygame


def get_clicked(group, mouse_pos):
    pass


'''def clicked_sprite(group, mouse_pos):
    for sprite in group:
        rect = sprite.rect
        if rect.collidepoint(mouse_pos[0], mouse_pos[1]) and sprite.used == False:
            sprite.image = to_grayscale(sprite.image)
            sprite.used = True'''


'''def clicked_sprite(group, mouse_pos):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in group:
                rect = sprite.rect
                if rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    return sprite.obj
    return False



def clicked_endBtn():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True
    return False'''


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