import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser

win = tk.Tk()

def open_click():
    s = (('텍스트파일','txt'),)
    fname = filedialog.askopenfilename(filetype = s)
    if fname != '':
        f=open(fname, 'r')
        data=f.read()
        tx.insert('insert',data)

def color_click():
    color = colorchooser.askcolor()
    tx['bg']=color[1]

tx=tk.Text(win,width=80,height=20)
tx.pack(side='top',fill='both',expand=True)
btn=tk.Button(win,text='파일불러오기',command=open_click)
btn.pack()

btn2=tk.Button(win,text='바탕색 병경', command=color_click)
btn2.pack()
win.mainloop()