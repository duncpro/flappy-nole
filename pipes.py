from character import CHARACTER_HITBOX, character_relative_position
from constants import BLACK, SIDESCROLL_SPEED
from state import FlappyNoleGameState
from math import ceil
from random import randint
import pygame

# The width and height of the pipes in pixels
PIPE_WIDTH: int = 100

# load top and bottom images used for pipes
TOP_PIPE = pygame.image.load('assets/Pipe_Inv.png')
BOTTOM_PIPE = pygame.image.load('assets/Pipe.png')

# The distance between two neighboring pipes in pixels
PIPE_FREQUENCY: int = 500

# The length of the gap (in pixels) which exists between the upper and lower sections of a single pipe.
PIPE_GAP_HEIGHT: int = 300

# Represents a "Pipe", like the ones in Flappy Bird.
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
        return self.left_bound_abs_pos - (tick / SIDESCROLL_SPEED)

    # Calculates the leftmost pixel (relative) of this pipe which is still visible in the window.
    def visible_left_bound(self, tick: int):
        leftbound = self.left_bound_relative(tick)
        # if leftbound < 0: leftbound = 0
        return leftbound

    # Calculates the width of this column which is still visible inside the user.
    def visible_width(self, tick: int):
        if self.left_bound_relative(tick) < 0:
            return PIPE_WIDTH - abs(self.left_bound_relative(tick))
        else:
            return PIPE_WIDTH

    def hitbox(self, screen_height):
        surface = pygame.Surface((PIPE_WIDTH, screen_height))
        # represents pixels which count as collision points.
        # Only used to compute the mask, not actual styling.
        surface.blit(TOP_PIPE, (0, -TOP_PIPE.get_height() + self.gap_start_pos))
        surface.blit(BOTTOM_PIPE, (0, self.gap_start_pos + PIPE_GAP_HEIGHT))
        return pygame.mask.from_surface(surface)

    def is_colliding(self, game_state: FlappyNoleGameState):
        character_pos = character_relative_position(game_state)
        # This is the distance in pixels away the pipe is from the player. A positive value indicates
        # the player has yet to pass through the pipe and a negative value indicates the pipe is behind the player.
        x_offset: int = round(self.visible_left_bound(game_state.game_tick) - character_pos[0])
        y_offset: int = round(character_pos[1] * -1)
        return CHARACTER_HITBOX.overlap(self.hitbox(game_state.screen_height), (x_offset, y_offset)) != None

    # need to take into account the height of the image
    def tophalf(self, tick: int):
        return pygame.Rect((self.visible_left_bound(tick), 0), (self.visible_width(tick), self.gap_start_pos))

    def bottomhalf(self, tick: int, screen_height: int):
        return pygame.Rect((self.visible_left_bound(tick), self.gap_start_pos + PIPE_GAP_HEIGHT), (self.visible_width(tick), screen_height))

# Draws all pipes present in the given game state on to the given screen.
def draw_pipes(screen, game_state: FlappyNoleGameState):
    for pipe in game_state.pipes:
        screen.blit(TOP_PIPE, pipe.tophalf(game_state.game_tick).move(0, -TOP_PIPE.get_height() + pipe.gap_start_pos))
        screen.blit(BOTTOM_PIPE, pipe.bottomhalf(game_state.game_tick, game_state.screen_height))

def pipe_tick(game_state: FlappyNoleGameState):
    try_spawn_pipe(game_state)
    trim_pipes(game_state)

# Checks to see if a new pipe should be spawned this tick, and if so, spawns it.
def try_spawn_pipe(game_state: FlappyNoleGameState):
    spawn_pipe = game_state.game_tick % (SIDESCROLL_SPEED * (PIPE_FREQUENCY + PIPE_WIDTH)) == 0
    if spawn_pipe:
        pos = int((game_state.game_tick + game_state.segment_visibility_window) / SIDESCROLL_SPEED)
        gap_start_pos = randint(0, game_state.screen_height - PIPE_GAP_HEIGHT)
        game_state.pipes.append(Pipe(pos, gap_start_pos))

# Despawns pipes that exit the visible world.
def trim_pipes(game_state: FlappyNoleGameState):
    if len(game_state.pipes) > (max_visible_pipes(game_state.screen_width) + 1):
        del game_state.pipes[0]

# Calculates an upperbound for the number of pipes which may be visible on the screen at once.
def max_visible_pipes(screen_width: int):
    intervals_per_window = ceil(screen_width / (PIPE_WIDTH + PIPE_FREQUENCY))
    if intervals_per_window < 1: intervals_per_window = 1
    return intervals_per_window
