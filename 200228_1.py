from tkinter import *
def selected():
    k=v.get()

    if k==1:
        print("복사하기를 선택")
    elif k==2:
        print('붙여넣기를 선택')
    else:
        print('지우기를 선택')

win = Tk()
mb=Menubutton(win,text='편 집', relief=RAISED)
mb.grid()
smenu=Menu(mb)
mb['menu']=smenu
v=IntVar()
smenu.add_radiobutton(label='복사하기',variable=v,value=1, command= selected)
smenu.add_radiobutton(label='붙여넣기',variable=v,value=2, command= selected)
smenu.add_radiobutton(label='지우기',variable=v,value=3, command= selected)
win.mainloop()