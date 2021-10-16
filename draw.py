import pygame

from state import FlappyNoleGameState

background_img = pygame.image.load("assets/background.xcf")

character_img = pygame.image.load("assets/character.png") # 300x306
character_rect = character_img.get_rect() 

# Simply draws the given game state on to the given screen.
# Makes no changes to the given game state. 
def draw(screen, game_state: FlappyNoleGameState):
    # Draw Background
    screen.blit(background_img, (0, 0))

    # Draw Character
    character_rect.centerx = game_state.screen_width / 2
    character_rect.centery = game_state.character_vpos; 
    screen.blit(character_img, character_rect)

    pygame.display.update()