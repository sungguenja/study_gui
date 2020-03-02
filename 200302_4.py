import tkinter

win = tkinter.Tk()
sv=tkinter.StringVar()

def focus_event(e):
    ent.select_range(0,len(sv.get()))

ent=tkinter.Entry(win, textvariable = sv)
ent.pack()
ent.bind('<FocusIn>', focus_event)

ent2=tkinter.Entry(win, textvariable = sv)
ent2.pack()

ent3=tkinter.Entry(win, textvariable = sv)
ent3.pack()

ent4=tkinter.Entry(win, textvariable = sv)
ent4.pack()

win.mainloop()