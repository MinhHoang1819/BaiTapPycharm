from tkinter import *

def Chuyen():
    duong = int(nam_duong.get())
    a = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    b = ['Tí', 'Sửu', 'Dần', 'Mẹo', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
    nam_am.set(f'{a[duong%10]} {b[duong%12]}')

root = Tk()
root.title('Chuyển năm')
root.resizable(height=True, width=True)
root.minsize(height=200, width=300)

nam_duong = StringVar()
nam_am = StringVar()

Label(root, text='Nhập năm dương:').grid(row=0, column=0)
Entry(root, width=30, textvariable=nam_duong).grid(row=0, column=1)

Button(root, text='Chuyển', command=Chuyen).grid(row=1, column=1)

Label(root, text='Năm âm:').grid(row=2, column=0)
Entry(root, width=30, textvariable=nam_am).grid(row=2, column=1)

root.mainloop()