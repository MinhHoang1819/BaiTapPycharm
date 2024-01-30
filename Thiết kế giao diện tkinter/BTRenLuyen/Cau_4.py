from tkinter import *

root = Tk()
root.title('Calculator')
root.resizable(height=True, width=True)
root.minsize(height=200, width=200)

entry = StringVar()

Entry(root, textvariable=entry, justify='right', font=('Arial', 12)).grid(row=0, columnspan=3)

frameButton_1 = Frame()
Button(frameButton_1, text='1', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_1, text='2', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_1, text='3', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
frameButton_1.grid(row=1, column=1)

frameButton_2 = Frame()
Button(frameButton_2, text='4', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_2, text='5', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_2, text='6', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
frameButton_2.grid(row=2, column=1)

frameButton_3 = Frame()
Button(frameButton_3, text='7', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_3, text='8', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_3, text='9', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
frameButton_3.grid(row=3, column=1)

frameButton_4 = Frame()
Button(frameButton_4, text='-', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_4, text='0', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
Button(frameButton_4, text='.', font=('Arial', 12), height=1, width=4).pack(side=LEFT, fill=X)
frameButton_4.grid(row=4, column=1)

frameButton_5 = Frame()
Button(frameButton_5, text='+', font=('Arial', 12), height=1, width=2).pack(side=LEFT, fill=X)
Button(frameButton_5, text='-', font=('Arial', 12), height=1, width=2).pack(side=LEFT, fill=X)
Button(frameButton_5, text='*', font=('Arial', 12), height=1, width=2).pack(side=LEFT, fill=X)
Button(frameButton_5, text='/', font=('Arial', 12), height=1, width=2).pack(side=LEFT, fill=X)
Button(frameButton_5, text='=', font=('Arial', 12), height=1, width=2).pack(side=LEFT, fill=X)
frameButton_5.grid(row=5, column=1)

Button(root, text='Clr', font=('Arial', 12), height=1, width=14).grid(row=6, column=1)

root.mainloop()