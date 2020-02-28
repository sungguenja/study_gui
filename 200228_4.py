from tkinter import *

def font_control(ev):
    label.config(font='HY헤드라인M {0} bold'.format(v.get()))
    if v.get()==40:
        label['text']='wa sans~'
        label['font']='굴림체 40 bold'
    else:
        label['text']='안녕 파이썬~'

win=Tk()
v=IntVar()
win.geometry('300x150')
label = Label(win, text='안녕 파이썬~')
label.pack(fill='y',expand=1)
sc = Scale(win, from_=10,to=40, orient=HORIZONTAL, variable=v, command=font_control)
sc.pack(fill='x',expand=1)
qbtn = Button(win,text='끝내기',command=win.quit, font='굴림 10 bold')
qbtn.pack()
win.mainloop()