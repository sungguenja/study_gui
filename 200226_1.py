import tkinter

win = tkinter.Tk()
win.title('윈도우 생성하기')

lbl = tkinter.Label(win, text='안녕하세요')
lbl.pack()
lbl2 = tkinter.Label(win, text='hello python', bg='red', fg='white')
lbl2.pack()
win.mainloop()