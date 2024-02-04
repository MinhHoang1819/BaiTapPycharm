from tkinter import *
from Xu_Ly_File import *

def Them():
    line = ma_sach.get() + ';' + ten_sach.get() + ';' + nam.get()
    LuuFile(line)
    ma_sach.set('')
    ten_sach.set('')
    nam.set('')
    ShowFile()

def ShowFile():
    arrSach = DocFile()
    list_box.delete(0, END)
    for item in arrSach:
        list_box.insert(END, item)

def Tim():
    arrSach = []
    ma = ma_sach.get()
    found = False
    for sach in arrSach:
        if sach[0] == ma:
            found = True
            break

    if found:
        pass
    else:
        pass

def SapXep():
    arrSach = DocFile()
    for i in range(len(arrSach)):
        for j in range(len(arrSach)):
            a = arrSach[i]
            b = arrSach[j]
            if a[2] > b[2]:
                arrSach[i] = b
                arrSach[j] = a
    list_box.delete(0, END)
    for item in arrSach:
        list_box.insert(END, item)

root = Tk()
root.title('Quản lý sách')
root.resizable(height=True, width=True)
root.minsize(height=300, width=305)

ma_sach = StringVar()
ten_sach = StringVar()
nam = StringVar()

Label(root, text='Quản Lý Sách', fg='blue', font=('Cambria', 16)).grid(row=0, columnspan=2)
list_box = Listbox(root, width=50)
list_box.grid(row=1, columnspan=2)
ShowFile()

Label(root, text='Mã sách:').grid(row=2, column=0)
Entry(root, width=30, textvariable=ma_sach).grid(row=2, column=1)

Label(root, text='Tên sách:').grid(row=3, column=0)
Entry(root, width=30, textvariable=ten_sach).grid(row=3, column=1)

Label(root, text='Năm xuất bản:').grid(row=4, column=0)
Entry(root, width=30, textvariable=nam).grid(row=4, column=1)

frameButton = Frame()
Button(frameButton, text='Thêm', command=Them).pack(side=LEFT)
Button(frameButton, text='Tìm', command=Tim).pack(side=LEFT)
Button(frameButton, text='Sắp xếp', command=SapXep).pack(side=LEFT)
Button(frameButton, text='Thoát', command=root.quit).pack(side=LEFT)
frameButton.grid(row=5, column=1)

root.mainloop()