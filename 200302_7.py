from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('350x200')

def comb1_selected(e):
    v=var.get()
    comb2.config(values=data[v])
    var2.set(data[v][0])

data = {'1 반': ('홍','최','박'),'2 반': ('김','이','성'), '3 반': ('이','오','폰')}

var = StringVar()
comb1 = ttk.Combobox(root, textvariable=var)
comb1.config(values=tuple(data.keys()))
comb1.grid(row=0,column=0)
var2 = StringVar()
comb2 = ttk.Combobox(root, textvariable=var2)
comb2.grid(row=0,column=1)

comb1.bind('<<ComboboxSelected>>', comb1_selected)
comb1.current(0)
comb1.event_generate('<<ComboboxSelected>>')  # 맨 처음에 강제로 발생시키기 위해
root.mainloop()