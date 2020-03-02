import tkinter
from tkinter import ttk

def press_handler(e):
    lbl['text'] = '키보드가 눌렸습니다'
    lbl2['text'] = '눌림'

def press_handler_2(e):
    lbl['background'] = 'yellow'
    lbl2['text'] = '눌림'
 
win = tkinter.Tk()

lbl=ttk.Label(win, text='키보드를 누르세요', font='굴림 20')
lbl2=tkinter.Label(win,text='두번째 창', font='굴림 20')
lbl.pack()
lbl2.pack()
lbl.bind('b', press_handler)
lbl.bind('b', press_handler_2, '+')
lbl.bind('a', press_handler)
lbl.focus()
# lbl2.focus()
win.mainloop()