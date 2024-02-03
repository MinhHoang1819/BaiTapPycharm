from tkinter import *

def Nhap():
    nam_duong.set('')
    nam_am.set('')

root = Tk()
root.title('Chuyển năm')
root.resizable(height=True, width=True)
root.minsize(height=200, width=300)

nam_duong = StringVar()
nam_am = StringVar()

Label(root, text='Nhập năm dương:').grid(row=0, column=0)
Entry(root, width=30, textvariable=nam_duong).grid(row=0, column=1)

Button(root, text='Chuyển').grid(row=1, column=1)

Label(root, text='Năm âm:').grid(row=2, column=0)
Entry(root, width=30, textvariable=nam_am).grid(row=2, column=1)

root.mainloop()