import sys
import sqlite3
import pygame
from draw import draw
from pygame_event_handler import handle_pygame_event
from state import FlappyNoleGameState
from tick import tick
from ui import UI_Manager
from score import create_score_table

game_state = FlappyNoleGameState()

pygame.init()

clock = pygame.time.Clock() 
screen = pygame.display.set_mode((game_state.screen_width, game_state.screen_height))

# set up UIManager object for gui
menu = UI_Manager(game_state.screen_width, game_state.screen_height)

create_score_table()


conn = sqlite3.connect('data.db')
try:
    conn.execute('CREATE TABLE IF NOT EXISTS Users (Username TEXT, Password TEXT, RememberMe INTEGER, HighScore INTEGER)')
    conn.execute('CREATE TABLE IF NOT EXISTS CurrentUser (Username TEXT, Password TEXT, RememberMe INTEGER, HighScore INTEGER)')
    conn.execute('CREATE TABLE IF NOT EXISTS score (username TEXT, score INTEGER)')
except:
    conn.rollback()
finally:
    conn.close()

while game_state.is_app_running:
    for event in pygame.event.get():
        handle_pygame_event(event, menu, game_state)
        # menu.manager.process_events(event)

    tick(game_state)
    menu.on_login = game_state.set_username
    menu.manager.update(clock.tick())
    draw(screen, menu.manager, game_state)
    clock.tick(35)


pygame.quit()
sys.exit()
