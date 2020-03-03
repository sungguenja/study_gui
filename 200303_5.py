from tkinter import *

def trace_mouse(e):
    lbl['text']= '(' + str(e.x) + ',' + str(e.y) + ')'

def inter_zone(e):
    but1['text'] = t1

def outer_zone(e):
    but1['text'] = t2

win = Tk()
win.geometry('300x180+500+500')

t1 = '버튼 위에 있음'
t2 = '버튼 밖에 있음'
lbl = Label(win,font='굴림 14 bold')
lbl.pack()

but1=Button(win, font='굴림 14 bold', text = t2)
but1.pack()

but1.bind('<Enter>', inter_zone)
but1.bind('<Leave>', outer_zone)
win.bind('<Motion>', trace_mouse)
win.mainloop()