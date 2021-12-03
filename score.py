from state import FlappyNoleGameState
from character import character_relative_position
from styles import title_font, FSU_GOLD

def calc_score(game_state: FlappyNoleGameState):
    # If no pipes are currently spawned (game_state.pipes is empty), then the player's score is equal
    # to the pipe number of the last pipe which WAS spawned.
    if len(game_state.pipes) == 0:
        return game_state.total_pipes_spawned

    # Starting from the rightmost pipe, find the first pipe of which the player's x-position
    # is bigger than that of the pipes.
    (x, y) = character_relative_position(game_state)
    for pipe in reversed(game_state.pipes):
        if x > pipe.left_bound_relative(game_state.game_tick):
            return pipe.pipe_no

    # If the player is not past any of the currently spawned pipes...
    return game_state.total_pipes_spawned - len(game_state.pipes)

def draw_score(screen, game_state: FlappyNoleGameState):
    score = title_font.render(str(calc_score(game_state)), True, FSU_GOLD)
    screen.blit(score, (10, 10))