import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import os
import os.path
import time


#def findfile(name, path):
#    for dirpath, dirname, finding_name in os.walk(path):
#        if name in finding_name:
#            return os.path.join(dirpath, name)

def main(stdscr):
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)     
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)     
    WB_color=curses.color_pair(1)
    BW_color=curses.color_pair(2)

    ##파일 검색 함수
    def findfile(name, path):
        for dirpath, dirname, finding_name in os.walk(path):
            if name in finding_name:
                return os.path.join(dirpath, name)
    
    ##터미널 사이즈 조사
    R_row,R_coulumn=os.popen('stty size', 'r').read().split()
    row=int(R_row)
    coulmns=int(R_coulumn)
    
    ##첫번쨰 화면: 검색할 파일 이름 입력
    stdscr.addstr(row//2-1,coulmns//2-15,"수정을 원하는 파일명을 적으시오.")
    win1=curses.newwin(1,9,row//2+1,coulmns//2-5)
    box1=Textbox(win1)
    rectangle(stdscr,row//2,coulmns//2-6,row//2+2,coulmns//2+4)
    stdscr.refresh()
    box1.edit()
    stdscr.clear()

    ##입력된 이름 검색
    text1=box1.gather()+".txt"
    filename=str(text1).replace(" ","")
    filepath=findfile(f"{filename}","/")
    
    ##
    if filepath==None:
        stdscr.addstr(row//2-1,coulmns//2-12,"파일을 찾을 수 없습니다.")
        stdscr.addstr(row//2,coulmns//2-8,"새로 생성합니다.")
        stdscr.refresh()
        time.sleep(3)
    else:
        openfile=open(f"{filepath}","r")
        filetext=openfile.read()
        openfile.close()

   
    ##두번째 화면: 파일 수정하는 화면
    win2=curses.newwin(row-5,coulmns-3,2,1)
    box2=Textbox(win2)
    rectangle(stdscr,1,0,row-3,coulmns-2)
    box2.addstr(0,0,f"{filetext}")
    stdscr.addstr(0,0,"편집!".center(coulmns-2),BW_color)
    stdscr.addstr(row-2,0,"편집을 끝낼려면 Ctrl + G를 누르시오.".center(coulmns-12),BW_color)
    stdscr.refresh()
    box2.edit()

    ##수정된 내용을 파일에 저장
    text2=box2.gather().strip()
    openfile=open(f"{filename}",'w')
    openfile.write(f"{text2}")
    openfile.close()
    

    ##마지막 화면: 종료화면
    win2.clear()
    win2.refresh()
    stdscr.clear()
    stdscr.addstr(row//2-1,coulmns//2-4,"저장되었습니다.")
    stdscr.addstr(row//2+1,coulmns//2-16,"프로그램을 종료하려면 아무키나 누르시오.")
    stdscr.refresh()
    
    stdscr.getch()

wrapper(main)