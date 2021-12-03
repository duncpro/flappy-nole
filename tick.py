from pipes import pipe_tick
from state import FlappyNoleGameState
from character import character_vmove
from score import score_tick

# In-game time is measured in ticks. This function is responsible for shifing
# the game state forward by a single tick. In other words, this function is responsible
# for the passage of time inside the game.
def tick(game_state: FlappyNoleGameState):
    if game_state.is_game_over == False:
        if game_state.is_main_menu == False:
            character_vmove(game_state)
            # Document the passage of time by incrementing the game tick timestamp by 1
            game_state.game_tick += 1
            pipe_tick(game_state)
            score_tick(game_state)