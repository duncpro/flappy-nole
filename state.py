from constants import SIDESCROLL_SPEED

# Represents the state of the game during a single tick.
# For every tick that passes the state object is progressed by tick(game_state) in tick.py.
class FlappyNoleGameState:
    def __init__(self):
        self.screen_width = 576
        self.screen_height = 780
        self.is_app_running = True
        self.title_text = "MAIN MENU"
        self.username = None

        self.new_game()

        # The number of elapsed ticks since the game was started.
        # While the player is on the main menu, before the game has actually started
        # this field will have a value of -1.
        self.game_tick = -1

    def new_game(self):
        # Speed at which the character is currently moving downwards, measured in pixels per tick.
        self.character_downward_speed = 0
        self.character_vpos = self.screen_height / 2
        self.game_tick = 0
        self.pipes = []
        # The number of pipes which have been added to the game world.
        # Not necessarily the number of pipes currently in the pipes array, as pipes are despawned after
        # they exit the view port.
        self.total_pipes_spawned = 0

    @property
    def is_main_menu(self):
        return self.game_tick == -1

    @property
    def is_colliding(self):
        for pipe in self.pipes:
            if pipe.is_colliding(self):
                return True 
        return False

    @property
    def is_game_over(self):
        if self.is_main_menu:
            return False
        # Allow the player to move off the bottom edge of the screen slightly
        # to make hitting gaps on the bottom edge of the pipe easier.
        did_character_fall = self.character_vpos > (self.screen_height + 100)
        return did_character_fall or self.is_colliding


    @property
    def screen_size(self):
        return (self.screen_width, self.screen_height) 

    # The number of ticks for which a unique segment of the world is visible.
    @property
    def segment_visibility_window(self):
        return self.screen_width * SIDESCROLL_SPEED

    @property
    def is_logged_in(self):
        return self.username != None

    # Simple setter for the username property of this class.
    # In general assigning directly to username is probably more clear.
    # But this function remains useful for scenarios in which assigment to the username property needs
    # to be encapsulated within a lambda function / callback.
    def set_username(self, username):
        self.username = username