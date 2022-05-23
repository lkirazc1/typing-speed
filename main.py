import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.getkey()
    stdscr.refresh()


def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text = []
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    wpm = 0
    start_time = time.time()



    while True:
        time_elapsed = max(time.time() - start_time, 1)

        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)


        stdscr.clear()


        display_text(stdscr, target_text, current_text, wpm)

        stdscr.refresh()


        if ''.join(current_text) == target_text:
            return wpm


        key = stdscr.getkey()
        

        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        
        elif ord(key) == 27:
            break


        elif len(current_text) < len(target_text):
            current_text.append(key)

        

def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current_text):
        if current_text[i] == target_text[i]:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        elif current_text[i] != target_text[i]:
            stdscr.addstr(0, i, char, curses.color_pair(2))

    stdscr.refresh()

def main(stdscr):

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    speed = wpm_test(stdscr)

    stdscr.addstr("Your wpm was {}.".format(speed))
        



if __name__ == '__main__':
    wrapper(main)