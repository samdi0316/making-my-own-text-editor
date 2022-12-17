import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import os
import os.path
import time

def main(stdscr):
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)     
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)     
    WB_color=curses.color_pair(1)
    BW_color=curses.color_pair(2)
    

    R_row,R_coulumn=os.popen('stty size', 'r').read().split()
    row=int(R_row)
    coulmns=int(R_coulumn)
    
    stdscr.addstr(row//2-1,coulmns//2-15,"수정을 원하는 파일명을 적으시오.")
    win1=curses.newwin(1,9,row//2+1,coulmns//2-5)
    box1=Textbox(win1)
    rectangle(stdscr,row//2,coulmns//2-6,row//2+2,coulmns//2+4)
    stdscr.refresh()
    box1.edit()
    text1=box1.gather()+".txt"
    filename=str(text1.replace(" ",""))

    try:
        stdscr.clear()
        file=open(f"{text1}",'r')
        
    except:
        stdscr.clear()
        stdscr.addstr(row//2-1,coulmns//2-12,"파일을 찾을 수 없습니다.")
        stdscr.addstr(row//2,coulmns//2-8,"새로 생성합니다.")
        stdscr.refresh()
        time.sleep(3)
        
   

    win2=curses.newwin(row-5,coulmns-3,2,1)
    box2=Textbox(win2)
    rectangle(stdscr,1,0,row-3,coulmns-2)
    if os.path.isfile(filename):
        box2.addstr(0,0,filename.read())
    else:
        pass
    stdscr.addstr(0,0,"편집!".center(coulmns-2),BW_color)
    stdscr.addstr(row-2,0,"편집을 끝낼려면 Ctrl + G를 누르시오.".center(coulmns-12),BW_color)
    stdscr.refresh()

    box2.edit()
    text2=box2.gather().strip()

    filename=open(f"{text1}",'w')
    filename.write(text2)
    filename.close()

    win2.clear()
    win2.refresh()
    stdscr.clear()
    stdscr.addstr(row//2-1,coulmns//2-4,"저장되었습니다.")
    stdscr.addstr(row//2+1,coulmns//2-16,"프로그램을 종료하려면 아무키나 누르시오.")
    stdscr.refresh()
    
    stdscr.getch()

wrapper(main)