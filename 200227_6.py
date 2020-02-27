import tkinter

win = tkinter.Tk()
def menu_click():
    print('메뉴를 선택하셨습니다')

mbar = tkinter.Menu(win)        # win 소속으로 메뉴를 만듬
fmenu = tkinter.Menu(mbar,tearoff=0)    # mbar 소속으로 메뉴를 만듬(서브메뉴)
fmenu.add_command(label='Open',command=menu_click)
fmenu.add_command(label='save',command=menu_click,accelerator='Ctrl+S')#단축키표현
fmenu.add_separator()           # 분리선
fmenu.add_command(label='Exit',command=menu_click)

mbar.add_cascade(label='파일',menu=fmenu)
mbar.add_cascade(label='편집')
mbar.add_cascade(label='도움말')

win['menu'] = mbar  # win.config(menu=mbar) 이런 식으로도 가능

win.mainloop()