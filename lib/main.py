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

currentGame = Game( )

def step(f_stop):
    playing = currentGame.tick()
    draw(currentGame)
    if not playing:
        f_stop.set()
    if not f_stop.is_set():
        threading.Timer(2, step, [f_stop]).start()

f_stop = threading.Event()
step(f_stop)
print('Ran successfully')
