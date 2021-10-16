from pygame import QUIT, KEYDOWN, K_SPACE
from sys import exit

from state import FlappyNoleGameState

# Applies the given event to the given game state.
def handle_pygame_event(event, game_state: FlappyNoleGameState):
    if event.type == QUIT: 
        game_state.is_game_running = False
    if event.type == KEYDOWN:
        handle_keyboard_event(event, game_state)

# Responsible for converting keyboard input to changes in game state.
def handle_keyboard_event(event, game_state: FlappyNoleGameState):
    if event.key == K_SPACE: 
        game_state.character_jump()