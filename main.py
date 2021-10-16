import sys, pygame
from draw import draw

from pygame_event_handler import handle_pygame_event
from state import FlappyNoleGameState
from tick import tick

game_state = FlappyNoleGameState()

pygame.init()

clock = pygame.time.Clock() 
screen = pygame.display.set_mode((game_state.screen_width, game_state.screen_height))

while game_state.is_game_running:
    for event in pygame.event.get():
        handle_pygame_event(event, game_state)
    tick(game_state)    
    draw(screen, game_state)    
    clock.tick(120)
