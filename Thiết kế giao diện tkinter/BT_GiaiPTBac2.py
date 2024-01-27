from tkinter import *

def continues():
    string_A.set('')
    string_B.set('')
    string_C.set('')
    string_KQ.set('')

def giai():
    a = float(string_A.get())
    b = float(string_B.get())
    c = float(string_C.get())
    if a == 0:
        if b == 0 and c == 0:
            string_KQ.set('Vo so nghiem')
        elif b == 0 and  c != 0:
            string_KQ.set('Vo nghiem')
        else:
            x = -c / b
            string_KQ.set('x = '+str(x))
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            string_KQ.set('Vo nghiem')
        elif delta == 0:
            string_KQ.set('Nghiem kep x1 = x2 = '+str((-b/(2*a))))
        else:
            x1 = (-b - sqrt(delta)) / (2*a)
            x2 = (-b + sqrt(delta)) / (2*a)
            string_KQ.set('x1 = '+str(x1)+'; x2 = '+str(x2))

root = Tk()

string_A = StringVar()
string_B = StringVar()
string_C = StringVar()
string_KQ = StringVar()

root.title('Phuong trinh bac 2')
root.resizable(height=True, width=True)
root.minsize(height=150, width=250)

Label(root, text='Phuong trinh bac 2', fg='red', font=('tahoma', 16)).grid(row=0, column=0, columnspan=2)

Label(root, text='He so A: ').grid(row=1, column=0)
Entry(root, width=30, textvariable=string_A).grid(row=1, column=1)

Label(root, text='He so B: ').grid(row=2, column=0)
Entry(root, width=30, textvariable=string_B).grid(row=2, column=1)

Label(root, text='He so C: ').grid(row=3, column=0)
Entry(root, width=30, textvariable=string_C).grid(row=3, column=1)

frameButton = Frame()
Button(frameButton, text='Giai', command=giai).pack(side=LEFT)
Button(frameButton, text='Tiep', command=continues).pack(side=LEFT)
Button(frameButton, text='Thoat', command=root.quit).pack(side=LEFT)

frameButton.grid(row=4, column=1)

Label(root, text='Ket qua: ').grid(row=5, column=0)
Entry(root, width=30, textvariable=string_KQ).grid(row=5, column=1)

root.mainloop()