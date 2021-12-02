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
                # if menu.try_login(menu.username_input.get_text(), menu.password_input.get_text()):
                #     print("login worked")
                game_state.new_game()
                menu.login_button.disable()
                # menu.submit_button_button.disable()
                # menu.cancel_button_button.disable()
                menu.create_button.disable()

                # else:
                #     # menu.username_input.set_text("incorrect login")
                #     print("login did not work")
            if event.ui_element == menu.create_button:
                menu.username_input.set_text("")
                menu.password_input.set_text("")
                menu.login_button.hide()
                menu.create_button.hide()
                menu.submit_button.show()
                menu.cancel_button.show()
            # if event.ui_element == menu.cancel_button:
            #     menu.username_input.set_text("")
            #     menu.password_input.set_text("")
            #     menu.login_button.show()
            #     menu.create_button.show()
            #     menu.submit_button.hide()
            #     menu.cancel_button.hide()
            # if event.ui_element == menu.submit_button:
            #     username = menu.username_input.get_text()
            #     password = menu.password_input.get_text()
            #     if menu.username_exists(username):
            #         print("username already exists")
            #     else:
            #         # menu.new_user(username,password)
            #         print("submit")



    menu.manager.process_events(event)


# Responsible for converting keyboard input to changes in game state.
def handle_keyboard_event(event, game_state: FlappyNoleGameState):
    if event.key == K_SPACE: 
        if game_state.is_game_over:
            print("SPACE")
            game_state.new_game()
        else:
            character_jump(game_state)