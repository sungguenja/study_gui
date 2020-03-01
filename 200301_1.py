from tkinter import *
basedata = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
win=Tk()
lbl = Label(win, text='이름',relief=RAISED,bg='white')
lbl.pack(fill=X)

lst=Listbox(win)
lst.pack(side=LEFT,fill=Y)

for data in basedata:
    lst.insert(END, data)

win.mainloop()