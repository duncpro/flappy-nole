# Represents the state of the game during a single tick.
# For every tick that passes the state object is progressed by tick(game_state) in tick.py.
class FlappyNoleGameState:
    def __init__(self):
        self.screen_width = 576
        self.screen_height = 780
        self.is_app_running = True
        self.new_game()

    def character_jump(self):
        self.character_downward_speed = -10      

    def new_game(self):
        # Speed at which the character is currently moving downwards, measured in pixels per tick.
        self.character_downward_speed = 0
        self.character_vpos = self.screen_height / 2

    @property
    def is_game_over(self):
        did_character_fall = self.character_vpos > self.screen_height
        return did_character_fall 

    @property
    def screen_size(self):
        return (self.screen_width, self.screen_height)