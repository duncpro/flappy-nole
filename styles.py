import pygame

pygame.font.init()

title_font = pygame.font.Font("assets/noles.ttf", 65)

# Colors
FSU_GARNET = (120, 47, 64)
FSU_GOLD = (206, 184, 136)
FSU_BLACK = (44, 42, 41)
BLACK = (0, 0, 0)
BRIGHT_RED = (255, 0, 0)

def horizontally_centered(screen_width, surface):
    return (screen_width - surface.get_width()) / 2

def vertically_centered(screen_height, surface):
    return (screen_height - surface.get_height()) / 2        
    
def centered(screen_size, surface):
    x: int = horizontally_centered(screen_size[0], surface)
    y: int = vertically_centered(screen_size[1], surface)

    return (x, y)
        