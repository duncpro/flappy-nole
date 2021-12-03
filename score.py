from effects import useEffect
from state import FlappyNoleGameState
from character import character_relative_position
from styles import title_font, FSU_GOLD, FSU_GARNET, horizontally_centered
import sqlite3

def calc_score(game_state: FlappyNoleGameState):
    # If no pipes are currently spawned (game_state.pipes is empty), then the player's score is equal
    # to the total number of pipes which have been spawned.
    if len(game_state.pipes) == 0:
        return game_state.total_pipes_spawned

    # Starting from the rightmost pipe, find the first pipe of which the player's x-position
    # is bigger than that of the pipes.
    (x, y) = character_relative_position(game_state)
    for pipe in reversed(game_state.pipes):
        if x > pipe.left_bound_relative(game_state.game_tick):
            return pipe.pipe_no

    # If the player is not past any of the currently spawned pipes...
    return game_state.total_pipes_spawned - len(game_state.pipes)

def create_score_table():
    connection = sqlite3.connect('data.db')
    connection.execute('CREATE TABLE IF NOT EXISTS score (username TEXT, score INTEGER);')   
    connection.commit()
    connection.close()

def persist_score(username, score):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM score where username = ?", (username,))
    user = cursor.fetchone()
    if user is not None:
        if user[1] < score:
            cursor.execute("UPDATE score SET score = ? WHERE username = ?;", (score, username))
    else:
        cursor.execute("INSERT INTO score (username, score) VALUES (?, ?);", (username, score))
    connection.commit()
    connection.close()
    pass

def score_tick(game_state: FlappyNoleGameState):
    score: int = calc_score(game_state)
    username = game_state.username

    # Anytime the game is over, persist the score of the game to the database.
    if (game_state.is_game_over):
        useEffect(lambda: persist_score(username, score), "persist_score", (username, score))    

def draw_score(screen, game_state: FlappyNoleGameState):
    score = title_font.render(str(calc_score(game_state)), True, FSU_GOLD)
    screen.blit(score, (10, 10))

def high_score_row_to_tuple(row):
    return (row[0], row[1])

def pull_high_scores():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT username, score FROM score ORDER BY SCORE DESC LIMIT 10;")
    results = map(high_score_row_to_tuple, cursor.fetchall())
    connection.close
    return results

def render_high_scores():
    rendered_texts = []
    for (username, score) in pull_high_scores():
        rendered_text = title_font.render(username + " " + str(score), True, FSU_GARNET)
        rendered_texts.append(rendered_text)
    return rendered_texts    

def draw_high_scores(game_state: FlappyNoleGameState, screen, vertical_offset: int):
    for rendered_text in render_high_scores():
        screen.blit(rendered_text, (horizontally_centered(game_state.screen_width, rendered_text), vertical_offset))
        vertical_offset += 50