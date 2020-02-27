import tkinter

win = tkinter.Tk()
win.geometry("300x300")

hello = tkinter.Label(win, text='Hello', relief='ridge')
hello.pack(side='left')     #왼쪽에 할당이 된다 사용이 안되보이는 장소도 할당이 되있는 상태!

hello2 = tkinter.Label(win, text='Hello2', relief='ridge')
hello2.pack(side='bottom')  # 아래쪽에 할당됨. 여기서 앵커를 걸거나 fill을 써 채울 수가 있다

# 앵커는 다음 창에서 확인해보자

win.mainloop()