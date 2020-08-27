from engine import Direction
from curses import KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT

def process_keypress(key, game):
    if key  == ord('w') or key  == KEY_UP:
        game.change_direction(Direction.UP)
    elif key  == ord('s') or key  == KEY_DOWN:
        game.change_direction(Direction.DOWN)
    elif key  == ord('a') or key  == KEY_LEFT:
        game.change_direction(Direction.LEFT)
    elif key  == ord('d') or key  == KEY_RIGHT:
        game.change_direction(Direction.RIGHT)

def listen_for_keypress(game, stdscr):
    key = stdscr.getch()
    #While the ESC key is not pressed
    while key != 27:
        process_keypress(key, game)
        key = stdscr.getch()
