from pipes import draw_pipes
import pygame

from state import FlappyNoleGameState

pygame.font.init()

background_img = pygame.image.load("assets/background.xcf")

character_img = pygame.image.load("assets/character.png") # 300x306

# Styles
title_font = pygame.font.Font("assets/noles_glades_bold.ttf", 80)
fsu_garnet = (120, 47, 64)
fsu_gold = (206, 184, 136)
fsu_black = (44, 42, 41)

# Simply draws the given game state on to the given screen.
# Makes no changes to the given game state. 
def draw(screen, game_state: FlappyNoleGameState):
    # Draw Background
    screen.blit(background_img, (0, 0))

    # Draw Character
    character_rect = character_img.get_rect() 
    character_rect.centerx = game_state.screen_width / 2
    character_rect.centery = game_state.character_vpos; 
    screen.blit(character_img, character_rect)

    draw_pipes(screen, game_state)  

    if game_state.is_game_over:
        draw_game_over(screen, game_state)  
     

    pygame.display.update()

def draw_game_over(screen, game_state: FlappyNoleGameState):
    alert = title_font.render("Game Over", True, fsu_gold, fsu_black)
    screen.blit(alert, centered(game_state.screen_size, alert))   


# Drawing Utilities    

def horizontally_centered(screen_width, surface):
    return (screen_width - surface.get_width()) / 2

def vertically_centered(screen_height, surface):
    return (screen_height - surface.get_height()) / 2        
    
def centered(screen_size, surface):
    x: int = horizontally_centered(screen_size[0], surface)
    y: int = vertically_centered(screen_size[1], surface)

    return (x, y)
        