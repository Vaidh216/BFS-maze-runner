import curses
from curses import wrapper
import queue
import time

maze = [
    [" ", " ", " ", "#", "#", "O", "#", "#", "#", "#"],
    [" ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
    [" ", " ", "#", "#", " ", " ", "#", " ", "#", "#"],
    [" ", " ", "#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", " ", " ", " ", "#", "#", "#", " ", "#", "#"],
    ["#", " ", "#", "#", " ", " ", "#", " ", "#", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#", "#"],
    ["#", "X", "#", " ", "#", "#", "#", "#", "#", "#"],
    [" ", " ", " ", " ", "#", " ", "#", "#", "#", "#"],
]

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    # stdscr.clear()
    # stdscr.addstr(5, 5, "hello world!",blue_and_black)
    # stdscr.refresh()
    # stdscr.getch()

wrapper(main)