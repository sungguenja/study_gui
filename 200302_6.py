import tkinter as tk
from tkinter import ttk

data = ['S회사','W회사','H회사','M회사','HK사','G회사']

root = tk.Tk()

tk.Label(root, text='업체 선택', bd=3).grid(row=0,column=0)
var_data=tk.StringVar()
cb=ttk.Combobox(root, values=data, justify='center', textvariable=var_data)
cb.bind('<<ComboboxSelected>>', lambda ev: lbl.config(text=var_data.get()))
cb.grid(row=0, column=1)
cb.current(0)

lbl=tk.Label(root, text='not selected', width=15,bg='red',fg='white')
lbl.grid(row=0,column=2)

root.mainloop()