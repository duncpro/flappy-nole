# Represents the state of the game during a single tick.
# For every tick that passes the state object is progressed by tick(game_state) in tick.py.
class FlappyNoleGameState:
    def __init__(self):
        self.screen_width = 576
        self.screen_height = 1024
        self.character_vpos = self.screen_height / 2
        # Speed at which the character is currently moving downwards, measured in pixels per tick.
        self.character_downward_speed = 0
        self.is_game_running = True

    def character_jump(self):
        self.character_downward_speed = -10    

        