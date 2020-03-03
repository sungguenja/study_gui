from tkinter import *
from tkinter import ttk

def label_change(e):
    lbl['text']=e.keysym + ' ' + str(e.keysym_num) + ' ' + str(e.keycode)
win=Tk()
lbl=Label(win,text='키보드를 누르세요', font='굴림 20', width=20)
win.bind('<KeyPress>', label_change)
lbl.pack()
win.mainloop()