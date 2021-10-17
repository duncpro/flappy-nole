from constants import FSU_BLACK, SIDESCROLL_SPEED
from state import FlappyNoleGameState
from math import ceil
from random import randint

# The width of the pipes in pixels
PIPE_WIDTH: int = 100

# The distance between two neighboring pipes in pixels
PIPE_FREQUENCY: int = 500

# The length of the gap (in pixels) which exists between the upper and lower sections of a single pipe.
PIPE_GAP_HEIGHT: int = 250

# Represents a "Pipe", like the ones in Flappy Bird.
# This class represents a pipe spatially, not stylistically.
class Pipe():
    def __init__(self, left_bound_abs_pos: int, gap_start_pos: int):
        # The absolute location of this pipe within the world measured in pixels from the starting line.
        self.left_bound_abs_pos = left_bound_abs_pos 
        # The position of the topmost pixel in the gap of this pipe.
        # In this case, position is defined as the distance from the topmost edge of the screen to the pixel, in pixels.
        self.gap_start_pos = gap_start_pos

    # Calculates the relative location (distance in pixels from leftmost side of window) of the leftbound
    # of this pipe during the given tick.
    def left_bound_relative(self, tick: int):
        return int(self.left_bound_abs_pos - (tick / SIDESCROLL_SPEED))

    # Calculates the relative location (distance in pixels from leftmost side of window) of the outer rightbound
    # of this pipe during the given tick. Exclusive, meaning the pipe is not visible at this pixel.
    def right_bound_relative(self, tick: int):
        return self.left_bound_relative(tick) + PIPE_WIDTH

    # Calculates the range of pixels on the screen which are occupied by this pipe.
    def visible_range(self, tick: int):
        return range(self.left_bound_relative(tick), self.right_bound_relative(tick))

# Draws all pipes present in the given game state on to the given screen.
def draw_pipes(screen, game_state: FlappyNoleGameState):
    for pipe in game_state.pipes:
        for pixel in pipe.visible_range(game_state.game_tick):
            upper_pipe_len: int = pipe.gap_start_pos
            screen.fill(FSU_BLACK, ((pixel, 0), (1, pipe.gap_start_pos - 1)))        
            screen.fill(FSU_BLACK, ((pixel, pipe.gap_start_pos + PIPE_GAP_HEIGHT),
                (1, game_state.screen_height - upper_pipe_len - PIPE_GAP_HEIGHT)))      

# Called once per tick, this function is responsible for spawning and despawning pipes based 
# on the player's current horizontal position.
def pipe_tick(game_state: FlappyNoleGameState):
    spawn_pipe = game_state.game_tick % (SIDESCROLL_SPEED * (PIPE_FREQUENCY + PIPE_WIDTH)) == 0
    if spawn_pipe:
        pos = int((game_state.game_tick + game_state.segment_visibility_window) / SIDESCROLL_SPEED)
        gap_start_pos = randint(0, game_state.screen_height - PIPE_GAP_HEIGHT)
        game_state.pipes.append(Pipe(pos, gap_start_pos))
    if len(game_state.pipes) > (max_visible_pipes(game_state.screen_width) + 1): 
        del game_state.pipes[0]
        
# Calculates an upperbound for the number of pipes which may be visible on the screen at once.
def max_visible_pipes(screen_width: int):
    intervals_per_window = ceil(screen_width / (PIPE_WIDTH + PIPE_FREQUENCY))
    if intervals_per_window < 1:
        return 1
    else:
        return intervals_per_window    