from tkinter import *

def Chuyen():
    f = float(do_f.get())
    c = (f-32) * 5/9
    do_c.set(f'{c:.2f} °C')

root = Tk()
root.title('Chuyển độ')
root.resizable(height=True, width=True)
root.minsize(height=200, width=300)

do_f = StringVar()
do_c = StringVar()

Label(root, text='Nhập độ F:').grid(row=0, column=0)
Entry(root, width=30, textvariable=do_f).grid(row=0, column=1)

Button(root, text='Chuyển', command=Chuyen).grid(row=1, column=1)

Label(root, text='Độ C:').grid(row=2, column=0)
Entry(root, width=30, textvariable=do_c).grid(row=2, column=1)

root.mainloop()