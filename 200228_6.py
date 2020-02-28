from tkinter import *

def change():
    print('station = ', charge[var.get()])

win=Tk()
stations='대구','부산','광주','여수'
charge=[25000,40000,40000,50000]

f=Frame(relief=RAISED, borderwidth=5)
var = IntVar()
for i, station in enumerate(stations):
    radio = Radiobutton(f, text=station,variable=var,value=i,command=change)
    radio.pack(side='top')

f.pack(pady=10)
var.set('대구')
win.mainloop()