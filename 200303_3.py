import tkinter

def right_(e):
    global point
    point=(point+1)%len(data)
    move(point)

def left_(e):
    global point
    point-=1
    if point==-1:
        point=len(data)-1
    move(point)

def move(p):
    z1['text'] = data[p][0]
    z3['text'] = data[p][1]
    z5['text'] = data[p][2]
    z7['text'] = data[p][3]
    z9['text'] = data[p][4]

point = 0

data = '''김동현, 010-2203-4000, 상계동 437, 한일양행, abc@abc.co.kr
박은애, 010-0900-9988, 동작동 456, 삼가전자, ㄱㄴㄷ@ㄱㄴㄷ.co.kr
최은주, 010-2200-4499, 마장동 444, 무한양행, 123@123.co.kr
후아유, 010-5566-6688, 독산동 222, 열국전자, ㅋㅌ@ㅋㅌ.co.kr'''

data = data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split(',')

win = tkinter.Tk()
win.geometry('400x200')
win.title('명단')
z = tkinter.Label(win,text='이름',bg='green',fg='white')
z1= tkinter.Label(win,text=data[point][0])
z.grid(row=0,column=0)
z1.grid(row=0,column=1)

z2= tkinter.Label(win,text='번호',bg='red',fg='white')
z3= tkinter.Label(win,text=data[point][1])
z2.grid(row=1,column=0)
z3.grid(row=1,column=1)

z4= tkinter.Label(win,text='주소',bg='black',fg='white')
z5= tkinter.Label(win,text=data[point][2])
z4.grid(row=2,column=0)
z5.grid(row=2,column=1)

z6= tkinter.Label(win,text='회사',bg='white',fg='black')
z7= tkinter.Label(win,text=data[point][3])
z6.grid(row=3,column=0)
z7.grid(row=3,column=1)

z8= tkinter.Label(win,text='이멜')
z9= tkinter.Label(win,text=data[point][4])
z8.grid(row=4,column=0)
z9.grid(row=4,column=1)
win.bind('<Right>', right_)
win.bind('<Left>', left_)
win.mainloop()