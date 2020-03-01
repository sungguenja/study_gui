import tkinter

def read_from_file():
    f=open('전화번호.txt', 'rt', encoding='UTF8')
    basedata=f.read()
    f.close()
    data = basedata.split('\n')
    for j in range(len(data)):
        person = data[j].split(',')
        lst.insert(tkinter.END, person)

def form_setting():
    global lst, lbl

    win = tkinter.Tk()
    lbl = tkinter.Label(win, text= ' 전화번호 ', relief=tkinter.RAISED, bg='yellow')
    lbl.pack(fill=tkinter.X)

    lst = tkinter.Listbox(win, width=60, bg='blue', fg='white')
    lst.pack(side=tkinter.LEFT, fill=tkinter.Y)
    btn=tkinter.Button(win, text='선택완료', bg='black',fg='white',command=select_one)
    btn.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    return  win

def select_one():
    try:
        sel = lst.curselection()
        one = lst.get(sel)
        s=str(sel[0]+1)+' 번 -->' + str(one)
        lbl['text'] = s
    except:
        return

main = form_setting()
read_from_file()
main.mainloop()