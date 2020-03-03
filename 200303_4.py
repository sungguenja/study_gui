from tkinter import *
from tkinter import ttk

def move_object(e):
    e.widget.place(x=e.x_root-win.winfo_x()-8,y=e.y_root-win.winfo_y()-30)

win = Tk()
win.geometry('600x380+500+500')
for c in range(6):
    lab = ttk.Button(win,text=str(c))
    lab.place(x=0,y=30*c)
    lab.bind('<B1-Motion>', move_object)

win.mainloop()