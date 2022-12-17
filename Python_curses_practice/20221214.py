import curses
from curses import wrapper
import time
import random

def main(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)     ##글자 색상 페어를 미리 지정해준다. 
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_RED)     ##글자는 검은색으로, 배경은 빨간색을 한다. 
    RB_color=curses.color_pair(1)
    BR_color=curses.color_pair(2)

    counter_win=curses.newwin(1,10,9,10)   ##새로운 윈도우를 생성한다. 크기는 10,1으로 화면의 9,10 지점에 위치한다. 
    pad=curses.newpad(100,100)  ##새로운 패드를 생성한다. 크기가 100*100이다.

    stdscr.clear()  ##이전에 있던 화면을 다 지워준다.  만약 화면이 깜빡인다면 .clear 대신 .erase를 사용한다. 
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char=chr(65+j)  ##chr(65)는 A이다. 이를 이용하여 알파벳을 전부 적어준다.
            pad.addstr(char)
            ##try:
            ##    pad.addstr(char)
            ##except curses.error:
            ##    pass
   
    ##pad.refresh(0,0,3,3,8,9)    ##패드의 0,0지점에서부터 보여주고 화면의 3,3지점에서 시작하여 9,8지점까지 보여준다. 
    
    for i in range(5):
        pad.refresh(i,i,2,i,8+i,8+i)
        time.sleep(0.3)
        stdscr.clear()
        stdscr.refresh()

    counter_win.clear()
    counter_win.addstr("난 별도!")
    counter_win.refresh()   ##stdscr.refresh를 하면 창의 내용도 전부 지워지므로 창을 다시 갱신해줌
    time.sleep(1)
    
    stdscr.clear()
    stdscr.refresh()
    
    counter_win.clear()
    counter_win.addstr("끝!")
    counter_win.refresh()

     
    stdscr.addstr(10,10,"프로그램을 종료하려면 아무키나 누르시오...")   ##글자를 표시해준다.
    stdscr.addstr(11,10,"싫으면 말구",BR_color|curses.A_BOLD)      ##11줄10칸부터 글자를 색상페어 2번,볼드처리해서 표시한다. 
    stdscr.refresh()    ##화면을 새로고침해준다. 새로고침하기 전까지는 화면이 변하지 않는다.
    time.sleep(1)
    #key = stdscr.getkey()  ##입력을 받는 부분
    
    stdscr.clear()
    #stdscr.addstr(10,10,f"왜 {key}라고 하는거야! 난 싫어!")
    stdscr.refresh()

    stdscr.nodelay(True)    ##입력값이 없더라도 줄을 넘어가게 해주는 특수한 명령어
    x,y=0,0

    while True:
        try:
            key = stdscr.getkey()   ##입력값을 본래의 값으로 받는다. ex) esc => ^[
        except:
            key = 0

        if key == "KEY_LEFT":
            x-=1
        elif key == "KEY_RIGHT":
            x+=1
        elif key == "KEY_UP":
            y-=1
        elif key == "KEY_DOWN":
            y+=1
        else:
            pass

        stdscr.clear()

        for i in range(random.randrange(5,10)):
            stdscr.addstr(random.randrange(0,10),random.randrange(0,10),"*")
        
        stdscr.addstr(y,x,"@",RB_color)
        stdscr.refresh()
        time.sleep(1)

    time.sleep(1)
    stdscr.getch()


wrapper(main)