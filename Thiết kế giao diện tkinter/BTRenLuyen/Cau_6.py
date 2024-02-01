from tkinter import *

root = Tk()
root.title('Enter New Password')
root.resizable(height=True, width=True)
root.minsize(height=200, width=300)

Label(root, text='Old Password:', font=('Arial', 12)).grid(row=0, column=0)
Entry(root, width=30, show='*').grid(row=0, column=1)

Label(root, text='New Password:', font=('Arial', 12)).grid(row=1, column=0)
Entry(root, width=30, show='*').grid(row=1, column=1)

Label(root, text='Enter New Password Again:', font=('Arial', 12)).grid(row=2, column=0)
Entry(root, width=30, show='*').grid(row=2, column=1)

frameButton = Frame()
Button(frameButton, text='OK', padx=5, pady=5).pack(side=LEFT, fill=X)
Button(frameButton, text='Cannel', padx=5, pady=5).pack(side=LEFT, fill=X)
frameButton.grid(row=3, columnspan=2)

root.mainloop()