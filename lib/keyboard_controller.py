from engine import *
from pynput import keyboard


def process_keypress(key, game):
    try:
        k = key.char
    except:
        k = key.name
    if k == 'w' or k == 'up':
        game.change_direction(Direction.UP)
    elif k == 's' or k == 'down':
        game.change_direction(Direction.DOWN)
    elif k == 'a' or k == 'left':
        game.change_direction(Direction.LEFT)
    elif k == 'd' or k == 'right':
        game.change_direction(Direction.RIGHT)

def listen_for_keypress(game):
    def on_press(key):
        process_keypress(key,game)
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
