import tkinter
from tkinter import messagebox

win = tkinter.Tk()

def ok_click():
    na=txt.get()
    lbl2['text'] = '당신의 이름은 ....' + na + '입니다!'
    messagebox.showinfo('이름',na)

lbl = tkinter.Label(win, text='이   름 :')
lbl.grid(row=0, column=0)
txt=tkinter.Entry(win, bg='blue')
txt.grid(row=0, column=1)

btn = tkinter.Button(win, text='입력완료', command = ok_click)
btn.grid(row=0,column=2)

lbl2 = tkinter.Label(win, text='알려줘', fg='black')
lbl2.grid(row=1,columnspan=2)
win.bind('<Return>', lambda e : ok_click())
txt.focus()
win.mainloop()