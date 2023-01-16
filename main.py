import curses
import time
import random
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to Speed Typing Test. WPM(Words Per Minute)") 
    stdscr.addstr(1, 0, "Press any key to enter to start :)")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(f"{target}") 
    stdscr.addstr(1, 0,f"WPM={wpm}") 
    stdscr.addstr(4, 0,f"Press ESC to exit!") 
    
    for idx, char in enumerate(current):
            if target[idx] == current[idx]:
                stdscr.addstr(0, idx, char, curses.color_pair(2)) 
            else:
                stdscr.addstr(0, idx, char, curses.color_pair(3)) 
    stdscr.refresh()

def random_text():
    try:
        with open("./test_sentence.txt", 'r') as f:
            sentences = f.readlines()
            return random.choice(sentences)
    except: 
        return "Error Occured"
        
def wpm_test(stdscr):
    target_text = random_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    while True:        
        time_elapsed = max(time.time() - start_time, 1)
        avg_word_size = 5
        wpm = round((len(current_text) / (time_elapsed / 60)) / avg_word_size)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        
        if len(current_text) == len(target_text): 
                stdscr.addstr(2, 0, "Done")
                break
        key = stdscr.getkey()
        
        if key in ("\e", "\x1B"):
            break
        
        elif key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:      
            current_text.append(key)
                
    stdscr.getkey()
            


def main(stdscr):
    #Color choice
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    
    start_screen(stdscr)    
    wpm_test(stdscr)

wrapper(main)
