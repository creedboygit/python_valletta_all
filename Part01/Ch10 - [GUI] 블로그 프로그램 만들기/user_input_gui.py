from tkinter import *


def btn_click(event):
    print(f"사용자 입력 값은 : \n{text.get(1.0, END)} 입니다")


data = '''여러 줄의 데이터를 입력하고 버튼을 클릭해주세요.'''

root = Tk()
root.geometry('500x500')

text = Text(root)  # root 창에 Text 컴포넌트(위젯) 추가
text.insert(1.0, data)  # 첫번째 데이터에 Text 입력값 저장
text.pack()

b1 = Button(root, text='결과값 확인')
b1.bind('<Button-1>', btn_click)
b1.pack()

root.mainloop()
