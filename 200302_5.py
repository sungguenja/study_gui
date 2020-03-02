import tkinter

data=['a','v','c','b','d','e','q',';']

def select_one(e):
    try:
        sel = lst.curselction()
        one=lst.get(sel)
        lbl['text'] = str('선택한 번호' + str(sel[0]) + '선택된 알파벳' + one)
    except:
        return

wint=tkinter.Tk()
lbl=tkinter.Label(wint, text='        ',bg='green',width=20)
lbl.pack(side='top',anchor='w')
lst=tkinter.Listbox(wint)
lst.pack(side='left',fill='y')

for d in data:
    lst.insert(tkinter.END, d)

lst.bind('<<ListboxSelect>>', select_one)
wint.mainloop()