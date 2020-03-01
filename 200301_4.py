import tkinter, webbrowser

win=tkinter.Tk()

def m_enter(e):
    print('마우스 들어왔음')
    txt.insert(tkinter.END, '마우스가 들어왔네요')

def m_leave(e):
    print('마우스 떠났음')
    txt.insert(tkinter.END, '마우스가 떠났네요')

def m_click(e):
    print('마우스 클릭')
    txt.insert(tkinter.E, '클cl릭ick')

txt = tkinter.Text(win)
txt.insert(tkinter.INSERT, '고구려 팔만대장경')
txt.insert(tkinter.END, '대한민국 일본 중국 북한 러씨아 혼돈의 동아시아')
txt.tag_add('kor', '1.0', '1.3')
txt.tag_add('start', '1.9', '1.14')
txt.insert(tkinter.INSERT, '네이버_바로가기', 'a')
txt.insert(tkinter.INSERT, '서울특별시', 'b')
txt.pack()
txt.tag_config('kor', background='yellow', foreground='blue', font='굴림 14 bold')
txt.tag_config('start', background='red', foreground='white', font='굴림 18 bold')
txt.tag_config('a', foreground='blue', underline=1)
txt.tag_config('b',  background='black', foreground='yellow')
txt.tag_bind('a', '<Enter>', m_enter)
txt.tag_bind('a', '<Button-1>', lambda e:webbrowser.open('https://www.naver.com'))
txt.tag_bind('kor', '<Enter>', m_enter)
txt.tag_bind('kor', '<Button-1>', m_click)
txt.tag_bind('start', '<Leave>', m_leave)
txt.config(cursor='arrow')
win.mainloop()