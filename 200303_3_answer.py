point = 0

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
    dt[0]['text'] = data[p][0]
    dt[1]['text'] = data[p][1]
    dt[2]['text'] = data[p][2]
    dt[3]['text'] = data[p][3]
    dt[4]['text'] = data[p][4]

data = '''김동현, 010-2203-4000, 상계동 437, 한일양행, abc@abc.co.kr
박은애, 010-0900-9988, 동작동 456, 삼가전자, ㄱㄴㄷ@ㄱㄴㄷ.co.kr
최은주, 010-2200-4499, 마장동 444, 무한양행, 123@123.co.kr
후아유, 010-5566-6688, 독산동 222, 열국전자, ㅋㅌ@ㅋㅌ.co.kr'''

data = data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split(',')

from tkinter import *
win=Tk()
win.geometry('400x200+500+500')
win.title('명단')
f1 = Frame(win)
f1.pack(side='right',ipadx=50)
label_texts=('이름 :', '번호 :', '주소 :', '소속 :', '이멜 :')

dt = []
for r in range(5):
    Label(f1, text = label_texts[r], font='굴림 12').grid(column=0,row=r,sticky=E)

    dt.append(Label(f1,text='...',font='굴림 12'))
    dt[r].grid(column=1,row=r,sticky=W)
move(point)
win.bind('<Right>',right_)
win.bind('<Left>',left_)
win.mainloop()