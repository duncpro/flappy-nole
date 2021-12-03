import sqlite3

import pygame
import pygame_gui
from pygame import threads

SCREEN_WIDTH = 576
SCREEN_HEIGHT = 780

# starting menu size is relative to game window
MENU_SIZE = (SCREEN_WIDTH/1.5,SCREEN_HEIGHT/2)

# offset to place menu in the middle of the menu
MENU_OFFSET = (SCREEN_WIDTH/2-MENU_SIZE[0]/2,SCREEN_HEIGHT/2-MENU_SIZE[1]/2)


# textbox information
TEXTBOX_SIZE = ((MENU_SIZE[0]/5*3)-6-8,12)
TEXTBOX_LABEL_SIZE = (MENU_SIZE[0]/5,33)
TEXTBOX_LABEL_OFFSET = (MENU_SIZE[0]/6)/2
# CENTER_BOX = ((MENU_SIZE[0]/2)-(TEXTBOX_SIZE[0]/2), 0) #MENU_SIZE[1]/2-TEXTBOX_SIZE[1]/2)

# button information
BUTTON_SIZE = (150,50)
BUTTON_PADDING = (MENU_SIZE[0]-(2*BUTTON_SIZE[0]))/3 -7 -  3  # horizontal padding
BUTTON_OFFSET = -(BUTTON_SIZE[0]/2 + 7 + 3)


# variable to store the offset caused by styling in menu.json
CONTAINER_OFFSET = 14

TITLE_SPACE_Y = 60

class UI_Manager():
    def __init__(self, width, height):
        self.manager = pygame_gui.UIManager((width, height), 'assets/menu.json')
        self.menu_container = pygame_gui.elements.UIPanel(pygame.Rect((MENU_OFFSET),MENU_SIZE),manager=self.manager, starting_layer_height=1)

        # text labels
        self.user_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((TEXTBOX_LABEL_OFFSET,TEXTBOX_LABEL_OFFSET+TITLE_SPACE_Y),(TEXTBOX_LABEL_SIZE)),
            text="USERNAME",manager=self.manager, container=self.menu_container, object_id="label")
        self.user_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((TEXTBOX_LABEL_OFFSET, 1.5*TEXTBOX_LABEL_OFFSET+TEXTBOX_LABEL_SIZE[1]+TITLE_SPACE_Y),
            TEXTBOX_LABEL_SIZE),text="PASSWORD", manager=self.manager, container=self.menu_container, object_id="label")
        # self.toggle_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((2*TEXTBOX_LABEL_OFFSET, TITLE_SPACE_Y+3*TEXTBOX_LABEL_OFFSET+TEXTBOX_LABEL_SIZE[1]),
        #      (TEXTBOX_LABEL_SIZE[0]*1.2, TEXTBOX_LABEL_SIZE[1]/1.7)),text="Remember Me", manager=self.manager, container=self.menu_container, object_id="text_only")

        # text boxes used to login and create new user
        self.username_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((TEXTBOX_LABEL_OFFSET+TEXTBOX_LABEL_SIZE[0], TITLE_SPACE_Y+TEXTBOX_LABEL_OFFSET), TEXTBOX_SIZE),
              container=self.menu_container,manager=self.manager)
        self.password_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((TEXTBOX_LABEL_OFFSET+TEXTBOX_LABEL_SIZE[0],
              1.5*TEXTBOX_LABEL_OFFSET+TEXTBOX_LABEL_SIZE[1]+TITLE_SPACE_Y), TEXTBOX_SIZE), container=self.menu_container,manager=self.manager)

        # Buttons used on the log in screen
        # self.toggle_button = pygame_gui.elements.UIButton(
        #     relative_rect=pygame.Rect((TEXTBOX_LABEL_OFFSET, TITLE_SPACE_Y+3*TEXTBOX_LABEL_OFFSET+TEXTBOX_LABEL_SIZE[1]), (15, 15)), text="", container=self.menu_container, manager=self.manager,
        #     object_id="toggle")

        self.login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((BUTTON_PADDING,MENU_SIZE[1]-BUTTON_PADDING+BUTTON_OFFSET), BUTTON_SIZE),
              text='LOGIN',container=self.menu_container,manager=self.manager)
        self.create_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((BUTTON_PADDING*2+BUTTON_SIZE[0], MENU_SIZE[1]-BUTTON_PADDING+BUTTON_OFFSET),
              BUTTON_SIZE),text='CREATE ACCOUNT',container=self.menu_container,manager=self.manager)

        # Buttons used on the create user screen
        self.submit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((BUTTON_PADDING, MENU_SIZE[1] - BUTTON_PADDING +
              BUTTON_OFFSET), BUTTON_SIZE),text='SUBMIT',container=self.menu_container,manager=self.manager)
        self.cancel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((BUTTON_PADDING * 2 + BUTTON_SIZE[0], MENU_SIZE[1] -
             BUTTON_PADDING + BUTTON_OFFSET),BUTTON_SIZE),text='CANCEL',container=self.menu_container, manager=self.manager)

        # hide the user screen buttons when program first starts
        self.submit_button.hide()
        self.cancel_button.hide()


        # login error messages
        self.user_label = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((TEXTBOX_LABEL_OFFSET,MENU_SIZE[1]/2),(MENU_SIZE[0],80)),wrap_to_height=True,
            html_text="<font color='#FF0000'>INVALID LOGIN INFORMATION PROVIDED</font>",manager=self.manager, container=self.menu_container, object_id="text_box")
        self.error_label = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((TEXTBOX_LABEL_OFFSET, MENU_SIZE[1] / 2), (MENU_SIZE[0], 80)),
            wrap_to_height=True,html_text="<font color='#FF0000'>BOTH USERNAME AND PASSWORD MUST BE<br>PROVIDED. USERNAME MUST BE UNIQUE</font>", manager=self.manager,
            container=self.menu_container, object_id="text_box")

        self.user_label.hide()
        self.error_label.hide()
        # buttons for game over
        # self.manager = pygame_gui.UIManager((width, height), 'assets/menu.json')
        # self.menu_container = pygame_gui.elements.UIPanel(pygame.Rect((MENU_OFFSET), MENU_SIZE), manager=self.manager,
        #                                                   starting_layer_height=1)

    def username_exists(self, username):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        try:
            cur.execute("SELECT 1 FROM Users where Username = ?", (username,))
        except:
            conn.rollback()  # rollback when an error occurs
        finally:
            match = cur.fetchone() != None
            conn.close()

        if match:
            return True
        else:
            return False

    def try_login(self,username, password):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        try:
            cur.execute("SELECT 1 FROM Users where Username = ? and Password = ?", (username, password))
        except:
            conn.close()
            return False
        if cur.fetchone() is None:
            conn.close()
            return False
        conn.close()
        return True

    def create_user(self, username, password):
        if self.username_exists(username):
            print("that username exists. Please choose a different one")
            self.clear_text()
            return False                            # do I want to do boolean here??
        elif len(username) is int(0) or len(password) is int(0):
            print("please provide a username AND a password")
            return False
        else:
            try:
                with sqlite3.connect('data.db') as conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO Users (Username,Password,RememberMe,HighScore) "
                            "VALUES(?,?,?,?)", (username, password, int(0), int(0)))
                    conn.commit()
            except:
                conn.rollback()
            finally:
                conn.close()
                return True

    def message(self, num):
        if num == 1:
            self.user_label.show()
        if num == 2:
            self.error_label.show()
        elif num == 3:
            self.user_label.hide()
            self.error_label.hide()



    def clear_text(self):
        self.username_input.set_text("")
        self.password_input.set_text("")

    def create_user_buttons(self):
        self.login_button.hide()
        self.create_button.hide()
        self.submit_button.show()
        self.cancel_button.show()

    def login_screen_buttons(self):
        self.login_button.show()
        self.create_button.show()
        self.submit_button.hide()
        self.cancel_button.hide()

    def disable_buttons(self):
        self.login_button.disable()
        self.create_button.disable()
        self.submit_button.disable()
        self.cancel_button.disable()
        self.menu_container.hide()