import pygame
import pygame_gui
from pygame import QUIT, KEYDOWN, K_SPACE, USEREVENT, VIDEORESIZE, RESIZABLE, display

# from menu import try_login
from state import FlappyNoleGameState
from character import character_jump

# Applies the given event to the given game state.
def handle_pygame_event(event, menu, game_state: FlappyNoleGameState):
    if event.type == QUIT: 
        game_state.is_app_running = False
    if event.type == KEYDOWN:
        handle_keyboard_event(event, game_state)
    if event.type == USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == menu.login_button:
                if menu.try_login(menu.username_input.get_text(), menu.password_input.get_text()):
                    game_state.new_game()
                    menu.disable_buttons()
            if event.ui_element == menu.create_button:
                menu.clear_text()
                menu.create_user_buttons()
            if event.ui_element == menu.cancel_button:
                # clear text entry boxes
                menu.clear_text()

                # call this to essentially "return" to the login screen
                menu.login_screen_buttons()
            if event.ui_element == menu.submit_button:
                if menu.create_user(menu.username_input.get_text(),menu.password_input.get_text()):
                    menu.clear_text()
                    menu.login_screen_buttons()

    menu.manager.process_events(event)


# Responsible for converting keyboard input to changes in game state.
def handle_keyboard_event(event, game_state: FlappyNoleGameState):
    if event.key == K_SPACE: 
        if game_state.is_game_over:
            game_state.new_game()
        else:
            character_jump(game_state)