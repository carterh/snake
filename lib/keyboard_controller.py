from engine import *
from pynput import keyboard


def process_keypress(key, game):
    if key == 'w':
        game.change_direction(Direction.UP)
    elif key == 's':
        game.change_direction(Direction.DOWN)
    elif key == 'a':
        game.change_direction(Direction.LEFT)
    elif key == 'd':
        game.change_direction(Direction.RIGHT)
