from tkinter import *
from tkinter import messagebox

win = Tk()
v=StringVar()
def ok_click():
    na=v.get()
    lbl2.configure(text='당신의 이름은....'+na+'입니다')
    messagebox.showinfo('이름', na)

lbl=Label(win,text='이   름 :')
lbl.grid(row=0,column=0)
txt=Entry(win, bg='yellow', textvariable=v)
txt.grid(row=0,column=1)

btn = Button(win, text='완  료', command=ok_click)
btn.grid(row=0,column=2)

lbl2=Label(win, text='당신의 이름은.....')
lbl2.grid(row=2,column=0,columnspan=2,sticky='W')
win.mainloop()