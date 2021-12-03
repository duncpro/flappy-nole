from character import draw_character
import pygame
from pipes import draw_pipes
from constants import FSU_BLACK, FSU_GOLD, FSU_GARNET
from state import FlappyNoleGameState

pygame.font.init()

background_img = pygame.image.load("assets/Wescott.png")
# menu_img = pygame.image.load("assets/")

# Styles
title_font = pygame.font.Font("assets/noles.ttf", 65)
# Simply draws the given game state on to the given screen.
# Makes no changes to the given game state. 
def draw(screen, manager, game_state: FlappyNoleGameState):
    screen.blit(background_img, (0, 0))
    if game_state.is_main_menu:
        draw_main_menu(screen, manager, game_state)
    elif game_state.is_game_over:
        draw_game_over(screen, manager, game_state)
    else:
        draw_character(screen, game_state)
        draw_pipes(screen, game_state)
        score = title_font.render(str(game_state.score), True, FSU_GOLD)
        screen.blit(score, (10, 10))
    pygame.display.update()

def draw_main_menu(screen, manager, game_state: FlappyNoleGameState):
    # manager.draw_ui(screen)
    alert = title_font.render("Main Menu", True, FSU_GARNET)
    manager.draw_ui(screen)

    screen.blit(alert, (horizontally_centered(game_state.screen_width, alert), game_state.screen_height/5))

def draw_game_over(screen, manager,game_state: FlappyNoleGameState):
    manager.draw_ui(screen)
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
        