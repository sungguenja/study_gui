import tkinter as tk

def Modif_event(e):
    ln = len(text.get('1.0','end'))-1
    lbl['text'] = str(ln) + '글자'
    text.edit_modified(False)       # if this is gone this function can't work

win = tk.Tk()
text = tk.Text(win,width=40,height=20)
text.pack(side='top',fill='both',expand=True)

lbl = tk.Label(win, anchor='w', bg='green', fg='white')
lbl.pack(side='bottom',fill='x')

text.bind('<<Modified>>', Modif_event)
win.mainloop()