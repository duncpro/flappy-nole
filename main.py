import sys

import pygame
# import pygame_gui
from draw import draw
from pygame_event_handler import handle_pygame_event
from state import FlappyNoleGameState
from tick import tick
from menu import Menu

game_state = FlappyNoleGameState()

pygame.init()

clock = pygame.time.Clock() 
screen = pygame.display.set_mode((game_state.screen_width, game_state.screen_height))

# set up UIManager object for gui
menu = Menu(game_state.screen_width, game_state.screen_height)
import sqlite3

conn = sqlite3.connect('data.db')
try:
    conn.execute('CREATE TABLE Users (Username TEXT, Password TEXT, RememberMe INTEGER, HighScore INTEGER)')
except:
    print("table already exists")
conn.close()

while game_state.is_app_running:
    for event in pygame.event.get():
        handle_pygame_event(event, menu, game_state)
        # menu.manager.process_events(event)

    tick(game_state)
    menu.manager.update(clock.tick())
    draw(screen, menu.manager, game_state)
    # clock.tick()


pygame.quit()
sys.exit()
