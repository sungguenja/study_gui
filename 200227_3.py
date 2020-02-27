from tkinter import *

win = Tk()
ent = Entry(win).grid(row=0,column=0,columnspan=3)

f='굴림', 10
btn1=Button(win,font=f,text='1-0',width=4,height=2)
btn1.grid(row=1,column=0)
btn2=Button(win,font=f,text='1-1',width=4,height=2)
btn2.grid(row=1,column=1)
btn3=Button(win,font=f,text='1-2',width=4,height=2)
btn3.grid(row=1,column=2)

win.mainloop()