#!/usr/bin/env python3

from engine import Game
import threading
from draw_board import draw
from keyboard_controller import listen_for_keypress
from curses import wrapper

def step(f_stop, currentGame, stdscr):
    playing = currentGame.tick()
    draw(currentGame, stdscr)
    if not playing:
        f_stop.set()
    if not f_stop.is_set():
        threading.Timer(0.3, step, [f_stop, currentGame, stdscr]).start()

def main(stdscr):
    currentGame = Game(20,40)
    f_stop = threading.Event()
    step(f_stop, currentGame, stdscr)
    listen_for_keypress(currentGame, stdscr)

if __name__ == '__main__':
    wrapper(main)
