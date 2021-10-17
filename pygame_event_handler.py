from pygame import QUIT, KEYDOWN, K_SPACE, VIDEORESIZE, RESIZABLE, display

from state import FlappyNoleGameState
from character import character_jump

# Applies the given event to the given game state.
def handle_pygame_event(event, game_state: FlappyNoleGameState):
    if event.type == QUIT: 
        game_state.is_app_running = False
    if event.type == KEYDOWN:
        handle_keyboard_event(event, game_state)

# Responsible for converting keyboard input to changes in game state.
def handle_keyboard_event(event, game_state: FlappyNoleGameState):
    if event.key == K_SPACE: 
        if game_state.is_game_over:
            game_state.new_game()
        else:
            character_jump(game_state)