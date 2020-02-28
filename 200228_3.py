from tkinter import *
win = Tk()
win.geometry('300x200')
v=IntVar()

def value_change(va1):
    print('스케일콤맨트',va1)

s2 = Scale(win,from_=10,to=100, orient=HORIZONTAL, command = value_change, tickinterval=10,variable=v)
s2.pack(fill='x')
win.mainloop()