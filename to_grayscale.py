import pygame


def to_grayscale(image):
    width, height = image.get_size()
    grayscale_image = pygame.Surface((width, height))

    for x in range(width):
        for y in range(height):
            r, g, b, *alpha = image.get_at((x, y))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_image.set_at((x, y), (gray, gray, gray))

    return grayscale_image