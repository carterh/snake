#!/usr/bin/env python3

from engine import *
import threading
from draw_board import *
from keyboard_controller import *

def step(f_stop, currentGame):
    playing = currentGame.tick()
    draw(currentGame)
    if not playing:
        f_stop.set()
    if not f_stop.is_set():
        threading.Timer(0.5, step, [f_stop, currentGame]).start()

def main():
    currentGame = Game(20,20)
    f_stop = threading.Event()
    step(f_stop, currentGame)
    listen_for_keypress(currentGame)

if __name__ == '__main__':
    main()
