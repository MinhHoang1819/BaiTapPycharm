from tkinter import *

def nextAction():
    string_a.set('')
    string_b.set('')
    string_kp.set('')

def giaiAction():
    a = float(string_a.get())
    b = float(string_b.get())
    if a == 0 and b == 0:
        string_kp.set('Vo so nghiem.')
    elif a == 0 and b != 0:
        string_kp.set('Vo nghiem.')
    else:
        string_kp.set('x = '+str(-b/a))

root = Tk()

string_a = StringVar()
string_b = StringVar()
string_kp = StringVar()

root.title('Phuong trinh bac 1')
root.resizable(height=True, width=True)
root.minsize(height=130, width=250)

Label(root, text='Phuong trinh bac 1', fg='red', font=('tahoma', 16), justify=CENTER).grid(row=0, columnspan=2)

Label(root, text='He so a: ').grid(row=1, column=0)
Entry(root, width=30, textvariable=string_a).grid(row=1, column=1)

Label(root, text='He so b: ').grid(row=2, column=0)
Entry(root, width=30, textvariable=string_b).grid(row=2, column=1)

frameButton = Frame()
Button(frameButton, text='Giai', command=giaiAction).pack(side=LEFT)
Button(frameButton, text='Tiep', command=nextAction).pack(side=LEFT)
Button(frameButton, text='Thoat', command=root.quit).pack(side=LEFT)
frameButton.grid(row=3, columnspan=2)

Label(root, text='Ket qua: ').grid(row=4, column=0)
Entry(root, width=30, textvariable=string_kp).grid(row=4, column=1)

root.mainloop()