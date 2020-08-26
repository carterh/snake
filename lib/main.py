#!/usr/bin/env python3

from engine import *
import threading
from draw_board import *

"""
Steps to implement:

    1.  Build game engine
    2.  Build rendering
    3.  Build async event listener on stdin?

"""

def process_keypress(key, game):
    if key == 'w':
        game.change_direction(Direction.UP)
    elif key == 's':
        game.change_direction(Direction.DOWN)
    elif key == 'a':
        game.change_direction(Direction.LEFT)
    elif key == 'd':
        game.change_direction(Direction.RIGHT)

currentGame = Game(20,20)

def step(f_stop):
    playing = currentGame.tick()
    draw(currentGame)
    if not playing:
        f_stop.set()
    if not f_stop.is_set():
        threading.Timer(0.5, step, [f_stop]).start()

f_stop = threading.Event()
step(f_stop)
while not f_stop.is_set():
    keypress = input()
    process_keypress(keypress, currentGame)
