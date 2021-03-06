from character import draw_character
import pygame
from pipes import draw_pipes
from styles import FSU_BLACK, FSU_GOLD, FSU_GARNET, horizontally_centered, title_font, centered
from state import FlappyNoleGameState
from score import draw_score, draw_high_scores

background_img = pygame.image.load("assets/Wescott.png")

# Simply draws the given game state on to the given screen.
# Makes no changes to the given game state. 
def draw(screen, manager, game_state: FlappyNoleGameState):
    screen.blit(background_img, (0, 0))
    if game_state.is_main_menu:
        draw_main_menu(screen, manager, game_state)
    elif game_state.is_game_over:
        draw_game_over(screen, manager, game_state)
        draw_score(screen, game_state)
    else:
        draw_character(screen, game_state)
        draw_pipes(screen, game_state)
        draw_score(screen, game_state)
    pygame.display.update()

def draw_main_menu(screen, manager, game_state: FlappyNoleGameState):
    alert = title_font.render(game_state.title_text, True, FSU_GARNET)
    manager.draw_ui(screen)
    screen.blit(alert, (horizontally_centered(game_state.screen_width, alert), game_state.screen_height/3.5))

def draw_game_over(screen, manager,game_state: FlappyNoleGameState):
    manager.draw_ui(screen)
    alert = title_font.render("Game Over", True, FSU_GARNET)
    title_font.set_underline(True)
    alert_2 = title_font.render("High Scores", True, FSU_BLACK)
    title_font.set_underline(False)

    draw_high_scores(game_state, screen, 160)
    screen.blit(alert, (horizontally_centered(game_state.screen_width, alert), 10))
    screen.blit(alert_2, (horizontally_centered(game_state.screen_width, alert_2), 20 + alert_2.get_height()))