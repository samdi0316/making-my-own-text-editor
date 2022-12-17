import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)     ##글자 색상 페어를 미리 지정해준다. 
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_RED)     ##글자는 검은색으로, 배경은 빨간색을 한다. 
    RB_color=curses.color_pair(1)
    BR_color=curses.color_pair(2)

    win=curses.newwin(10,10,1,1)
    box=Textbox(win)
    rectangle(stdscr, 0,0,11,11)
           
    stdscr.refresh()
    box.edit()
    text=box.gather().strip()
    win.clear()
    win.addstr(5,5,text)
    stdscr.getch()

wrapper(main)