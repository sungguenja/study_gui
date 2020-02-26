import tkinter

win = tkinter.Tk()
win.title('윈도우 생성하기')

lbl = tkinter.Label(win, text='안녕하세요')
lbl.pack()
lbl2 = tkinter.Label(win, text='hello python', bg='red', fg='white')
lbl2.pack()
# 여기서 바꾸고 싶다면 밑의 두가지 방법이 있다
lbl.config(text='config를 이용해 바꿔버렸어요')
lbl2['text'] = 'key로 접근해서 딕셔너리처럼 소환이 가능해요'
win.mainloop()