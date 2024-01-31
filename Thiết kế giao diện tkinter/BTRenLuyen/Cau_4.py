from tkinter import *

exp = ''
def nhap(num):
    global exp
    exp = exp + str(num)
    entry.set(exp)

def bang():
    global exp
    try:
        result = str(eval(exp))
        entry.set(result)
        exp = ''
    except:
        entry.set('Loi')
        exp = ''

def xoa():
    global exp
    exp = ''
    entry.set('')

root = Tk()
root.title('Calculator')
root.resizable(height=True, width=True)
root.minsize(height=200, width=200)

entry = StringVar()
entry.set('')

Entry(root, textvariable=entry, justify='right', font=('Arial', 12)).grid(row=0, columnspan=3)

frameButton_1 = Frame()
Button(frameButton_1, text='1', font=('Arial', 12), height=1, width=4, command=lambda : nhap(1)).pack(side=LEFT, fill=X)
Button(frameButton_1, text='2', font=('Arial', 12), height=1, width=4, command=lambda : nhap(2)).pack(side=LEFT, fill=X)
Button(frameButton_1, text='3', font=('Arial', 12), height=1, width=4, command=lambda : nhap(3)).pack(side=LEFT, fill=X)
frameButton_1.grid(row=1, column=1)

frameButton_2 = Frame()
Button(frameButton_2, text='4', font=('Arial', 12), height=1, width=4, command=lambda : nhap(4)).pack(side=LEFT, fill=X)
Button(frameButton_2, text='5', font=('Arial', 12), height=1, width=4, command=lambda : nhap(5)).pack(side=LEFT, fill=X)
Button(frameButton_2, text='6', font=('Arial', 12), height=1, width=4, command=lambda : nhap(6)).pack(side=LEFT, fill=X)
frameButton_2.grid(row=2, column=1)

frameButton_3 = Frame()
Button(frameButton_3, text='7', font=('Arial', 12), height=1, width=4, command=lambda : nhap(7)).pack(side=LEFT, fill=X)
Button(frameButton_3, text='8', font=('Arial', 12), height=1, width=4, command=lambda : nhap(8)).pack(side=LEFT, fill=X)
Button(frameButton_3, text='9', font=('Arial', 12), height=1, width=4, command=lambda : nhap(9)).pack(side=LEFT, fill=X)
frameButton_3.grid(row=3, column=1)

frameButton_4 = Frame()
Button(frameButton_4, text='-', font=('Arial', 12), height=1, width=4, command=lambda : nhap('-')).pack(side=LEFT, fill=X)
Button(frameButton_4, text='0', font=('Arial', 12), height=1, width=4, command=lambda : nhap(0)).pack(side=LEFT, fill=X)
Button(frameButton_4, text='.', font=('Arial', 12), height=1, width=4, command=lambda : nhap('.')).pack(side=LEFT, fill=X)
frameButton_4.grid(row=4, column=1)

frameButton_5 = Frame()
Button(frameButton_5, text='+', font=('Arial', 12), height=1, width=2, command=lambda : nhap('+')).pack(side=LEFT, fill=X)
Button(frameButton_5, text='-', font=('Arial', 12), height=1, width=2, command=lambda : nhap('-')).pack(side=LEFT, fill=X)
Button(frameButton_5, text='*', font=('Arial', 12), height=1, width=2, command=lambda : nhap('*')).pack(side=LEFT, fill=X)
Button(frameButton_5, text='/', font=('Arial', 12), height=1, width=2, command=lambda : nhap('/')).pack(side=LEFT, fill=X)
Button(frameButton_5, text='=', font=('Arial', 12), height=1, width=2, command=bang).pack(side=LEFT, fill=X)
frameButton_5.grid(row=5, column=1)

Button(root, text='Clr', font=('Arial', 12), height=1, width=14, command=xoa).grid(row=6, column=1)

root.mainloop()