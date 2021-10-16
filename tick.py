from state import FlappyNoleGameState

gravity = .20

# In-game time is measured in ticks. This function is responsible for shifing
# the game state forward by a single tick. In other words, this function is responsible
# for the passage of time inside the game.
def tick(game_state: FlappyNoleGameState):
    # Simulate gravity by increasing the speed at which the character is falling every tick.
    # To simulate a jump just set the downward speed to some negative value.
    # This will cause the character to begin moving upwards until is overtaken by gravity oncemore.
    game_state.character_downward_speed += gravity

    # Shift the character's current postion by the character's current speed.
    game_state.character_vpos += game_state.character_downward_speed