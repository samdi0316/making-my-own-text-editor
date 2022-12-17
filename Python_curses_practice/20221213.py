import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)     ##글자 색상 페어를 미리 지정해준다. 
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_RED)     ##글자는 검은색으로, 배경은 빨간색을 한다. 
    RB_color=curses.color_pair(1)
    BR_color=curses.color_pair(2)

    counter_win=curses.newwin(1,10,9,10)   ##새로운 윈도우를 생성한다. 크기는 10,1으로 화면의 9,10 지점에 위치한다. 

    stdscr.clear()  ##이전에 있던 화면을 다 지워준다.  만약 화면이 깜빡인다면 .clear 대신 .erase를 사용한다. 
    stdscr.refresh()

    for i in range(50):
        
        if i%2==0:
            color=RB_color
        else:
           color=BR_color
   
        stdscr.addstr(10,10,f"{i}눈뽕!{i}",color)
        stdscr.refresh()
        counter_win.clear()
        counter_win.addstr("난 별도!")
        counter_win.refresh()   ##stdscr.refresh를 하면 창의 내용도 전부 지워지므로 창을 다시 갱신해줌
        time.sleep(0.1)
        stdscr.clear()
    
    stdscr.refresh()
    
    counter_win.clear()
    counter_win.addstr("끝!")
    counter_win.refresh()

     
    stdscr.addstr(10,10,"프로그램을 종료하려면 아무키나 누르시오...")   ##글자를 표시해준다.
    stdscr.addstr(11,10,"싫으면 말구",BR_color|curses.A_BOLD)      ##11줄10칸부터 글자를 색상페어 2번,볼드처리해서 표시한다. 
    stdscr.refresh()    ##화면을 새로고침해준다. 새로고침하기 전까지는 화면이 변하지 않는다.
    stdscr.getch()  ##입력을 받는 부분

wrapper(main)