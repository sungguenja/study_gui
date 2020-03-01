import tkinter

def read_from_file():
    f=open('전화번호.txt','rt',encoding='UTF8')
    basedata = f.read()
    f.close()
    data = basedata.split('\n')
    for j in range(len(data)):
        person = data[j].split(',')
        lst.insert(tkinter.END,person)

def form_setting():
    global lst, lbl
    win = tkinter.Tk()
    lbl = tkinter.Label(win,text=' 전화번호 ', relief=tkinter.RAISED, bg='white')
    lbl.pack(fill=tkinter.BOTH)

    lst=tkinter.Listbox(win,width=60)
    lst.pack(side=tkinter.LEFT,fill=tkinter.Y)
    return win

main = form_setting()
read_from_file()
main.mainloop()