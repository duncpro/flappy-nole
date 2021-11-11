from character import draw_character
import pygame
from pipes import draw_pipes
from constants import FSU_BLACK, FSU_GOLD
from state import FlappyNoleGameState

pygame.font.init()

background_img = pygame.image.load("assets/Wescott.png")

# Styles
title_font = pygame.font.Font("assets/noles_glades_bold.ttf", 80)

# Simply draws the given game state on to the given screen.
# Makes no changes to the given game state. 
def draw(screen, game_state: FlappyNoleGameState):
    screen.blit(background_img, (0, 0))
    draw_character(screen, game_state)
    draw_pipes(screen, game_state) 
    if game_state.is_game_over:
        draw_game_over(screen, game_state)  
    pygame.display.update()

def draw_game_over(screen, game_state: FlappyNoleGameState):
    alert = title_font.render("Game Over", True, FSU_GOLD, FSU_BLACK)
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
        