from tkinter import *
from tkinter import messagebox as m

def btn_click():
    lbl['text'] = 'have a good day~~'
    m.showinfo('인사완료','인사를 마쳤습니다')

win=Tk()
win.geometry("300x60")

lbl=Label(win,text="안녕하세요 파이썬~", font='HY헤드라인M 20')
lbl.pack()

btn = Button(win, text="눌러주세요", command=btn_click,bg='red',fg='white')
btn.pack(fill='x')

win.mainloop()