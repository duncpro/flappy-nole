from state import FlappyNoleGameState
import pygame

# This file contains all functionality related to the movement, positioning,
# and rendering of the game character.

def character_jump(game_state: FlappyNoleGameState):
    game_state.character_downward_speed = -9 

def character_vmove(game_state: FlappyNoleGameState):
    GRAVITY = .20
    # Simulate gravity by increasing the speed at which the character is falling every tick.
    # To simulate a jump just set the downward speed to some negative value.
    # This will cause the character to begin moving upwards until is overtaken by gravity oncemore.
    game_state.character_downward_speed += GRAVITY
    # Shift the character's current postion by the character's current speed.
    game_state.character_vpos += game_state.character_downward_speed

CHARACTER_IMAGE = pygame.image.load("assets/character.png") 

def draw_character(screen, game_state: FlappyNoleGameState):  
    screen.blit(CHARACTER_IMAGE, character_relative_position(game_state)) 

def character_hitbox(game_state: FlappyNoleGameState):
    surface = pygame.Surface((CHARACTER_IMAGE.get_width(), CHARACTER_IMAGE.get_height()))
    surface.blit(CHARACTER_IMAGE, (0, 0))
    mask = pygame.mask.from_surface(surface)
    return mask

def character_relative_position(game_state: FlappyNoleGameState):
    return ((game_state.screen_width - CHARACTER_IMAGE.get_width()) / 2, game_state.character_vpos)