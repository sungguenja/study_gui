from tkinter import *

def inspect_check():
    print("숙박여부",var1.get())
    print("조식여부",var2.get())
    print("가이드 투어 여부",var3.get())

win = Tk()
win.geometry('200x150')
fra=LabelFrame(win, text='여행상품선택',labelanchor = 'nw', font='굴림 10 bold')
fra.pack(fill='both',padx=20,ipady=10)
var1=BooleanVar()
var2=BooleanVar()
var3=BooleanVar()
# variabel 뒤에 onvalue를 적을시 on은 어떤 값인지 변화시키는게 가능 하지만 여기선 var값들은 boolean 타입이기에 그짓은 하면안된다
chk1 = Checkbutton(fra, text='숙 박', variable=var1, command=inspect_check)
chk1.pack()
chk2 = Checkbutton(fra, text='숙 박', variable=var2, command=inspect_check)
chk2.pack()
chk3 = Checkbutton(fra, text='숙 박', variable=var3, command=inspect_check)
chk3.pack()
btn=Button(fra,text='선택완료',command=inspect_check)
btn.pack()
mainloop()