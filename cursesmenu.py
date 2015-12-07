import curses
import curses.textpad
import pypodder

__VERSION__ = 'v0.1.0'

def main(stdscr):
    stdscr.addstr('Please enter rss url: ')
    tb = curses.textpad.Textbox(stdscr)
    url = tb.edit()

    stdscr.clear()

curses.wrapper(main)
