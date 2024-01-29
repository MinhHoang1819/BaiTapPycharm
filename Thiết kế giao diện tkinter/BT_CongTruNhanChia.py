from tkinter import *

def congAction():
    a = float(string_A.get())
    b = float(string_B.get())
    string_KQ.set(a + b)

def truAction():
    a = float(string_A.get())
    b = float(string_B.get())
    string_KQ.set(a - b)

def nhanAction():
    a = float(string_A.get())
    b = float(string_B.get())
    string_KQ.set(a * b)

def chiaAction():
    a = float(string_A.get())
    b = float(string_B.get())
    string_KQ.set(a / b)

root = Tk()

string_A = StringVar()
string_B = StringVar()
string_KQ = StringVar()

root.title('Cong_Tru_Nhan_Chia')
root.resizable(height=True, width=True)
root.minsize(height=200, width=230)

Label(root, text='Cộng Trừ Nhân Chia', fg='blue', font=('tahoma', 16)).grid(row=0, columnspan=3)

flameButton = Frame(root)
Button(flameButton, text='Cộng', command=congAction).pack(side=TOP, fill=X)
Button(flameButton, text='Trừ', command=truAction).pack(side=TOP, fill=X)
Button(flameButton, text='Nhân', command=nhanAction).pack(side=TOP, fill=X)
Button(flameButton, text='Chia', command=chiaAction).pack(side=TOP, fill=X)
flameButton.grid(row=1, column=0, rowspan=4)

Label(root, text='Hệ số a: ').grid(row=1, column=1)
Entry(root, width=12, textvariable=string_A).grid(row=1, column=2)

Label(root, text='Hệ số b: ').grid(row=2, column=1)
Entry(root, width=12, textvariable=string_B).grid(row=2, column=2)

Label(root, text='Kết quả: ').grid(row=3, column=1)
Entry(root, width=12, textvariable=string_KQ).grid(row=3, column=2)

Button(root, text='Thoát', command=root.quit).grid(row=4, column=2)

root.mainloop()