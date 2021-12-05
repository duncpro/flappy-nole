from styles import BRIGHT_RED
from constants import DEBUG_MODE_ENABLED
from state import FlappyNoleGameState
import pygame

# This file contains all functionality related to the movement, positioning,
# and rendering of the game character.

def character_jump(game_state: FlappyNoleGameState):
    game_state.character_downward_speed = -16

def character_vmove(game_state: FlappyNoleGameState):
    GRAVITY = 1.2

    # Simulate gravity by increasing the speed at which the character is falling every tick.
    # To simulate a jump just set the downward speed to some negative value.
    # This will cause the character to begin moving upwards until is overtaken by gravity oncemore.
    game_state.character_downward_speed += GRAVITY
    # Shift the character's current postion by the character's current speed.
    game_state.character_vpos += game_state.character_downward_speed

CHARACTER_IMAGE = pygame.image.load("assets/character.xcf") 
CHARACTER_HITBOX = pygame.mask.from_surface(CHARACTER_IMAGE)  

def draw_character(screen, game_state: FlappyNoleGameState):  
    screen.blit(CHARACTER_IMAGE, character_relative_position(game_state)) 
    if DEBUG_MODE_ENABLED:
        draw_character_hitbox(screen, game_state)    

def draw_character_hitbox(screen, game_state: FlappyNoleGameState):
    character_pos = character_relative_position(game_state)
    for point in CHARACTER_HITBOX.outline():
        offset_point = (round(point[0] + character_pos[0]), round(point[1] + character_pos[1]))
        screen.set_at(offset_point, BRIGHT_RED)
     

def character_relative_position(game_state: FlappyNoleGameState):
    return ((game_state.screen_width - CHARACTER_IMAGE.get_width()) / 2, game_state.character_vpos)