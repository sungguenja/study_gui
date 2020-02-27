import tkinter

win = tkinter.Tk()
win.geometry("300x300")

hello = tkinter.Label(win, text='Hello', relief='ridge')
hello.pack(side='left', anchor='n') # 왼쪽 할당된 공간에서 북쪽으로 가라

hello2 = tkinter.Label(win, text='Hello2', relief='ridge')
hello2.pack(side='right', fill='y')  # 오른쪽 할당된 공간을 y방향으로 채우자

hello3 = tkinter.Label(win, text='Hello3', relief='ridge')
hello3.pack(side='bottom', ipadx=40)    # 위젯자체가 커짐

hello4 = tkinter.Label(win, text='Hello4', relief='ridge')
hello4.pack(side='top', padx=40)    # 외부에 40만큼 여유를 줌 (띄어쓰기 생각)

win.mainloop()