from tkinter import *

root = Tk()
root.title('Các loại style của Button')
root.resizable(height=True, width=True)
root.minsize(height=200, width=350)

Label(root, text='borderwidth = 0').grid(row=0, column=0)
Button(root, text='raised', borderwidth=0, relief='raised').grid(row=0, column=1)
Button(root, text='sunken', borderwidth=0, relief='sunken').grid(row=0, column=2)
Button(root, text='flat', borderwidth=0, relief='flat').grid(row=0, column=3)
Button(root, text='ridge', borderwidth=0, relief='ridge').grid(row=0, column=4)
Button(root, text='groove', borderwidth=0, relief='groove').grid(row=0, column=5)
Button(root, text='solid', borderwidth=0, relief='solid').grid(row=0, column=6)

Label(root, text='borderwidth = 1').grid(row=1, column=0)
Button(root, text='raised', borderwidth=1, relief='raised').grid(row=1, column=1)
Button(root, text='sunken', borderwidth=1, relief='sunken').grid(row=1, column=2)
Button(root, text='flat', borderwidth=1, relief='flat').grid(row=1, column=3)
Button(root, text='ridge', borderwidth=1, relief='ridge').grid(row=1, column=4)
Button(root, text='groove', borderwidth=1, relief='groove').grid(row=1, column=5)
Button(root, text='solid', borderwidth=1, relief='solid').grid(row=1, column=6)

Label(root, text='borderwidth = 2').grid(row=2, column=0)
Button(root, text='raised', borderwidth=2, relief='raised').grid(row=2, column=1)
Button(root, text='sunken', borderwidth=2, relief='sunken').grid(row=2, column=2)
Button(root, text='flat', borderwidth=2, relief='flat').grid(row=2, column=3)
Button(root, text='ridge', borderwidth=2, relief='ridge').grid(row=2, column=4)
Button(root, text='groove', borderwidth=2, relief='groove').grid(row=2, column=5)
Button(root, text='solid', borderwidth=2, relief='solid').grid(row=2, column=6)

Label(root, text='borderwidth = 3').grid(row=3, column=0)
Button(root, text='raised', borderwidth=3, relief='raised').grid(row=3, column=1)
Button(root, text='sunken', borderwidth=3, relief='sunken').grid(row=3, column=2)
Button(root, text='flat', borderwidth=3, relief='flat').grid(row=3, column=3)
Button(root, text='ridge', borderwidth=3, relief='ridge').grid(row=3, column=4)
Button(root, text='groove', borderwidth=3, relief='groove').grid(row=3, column=5)
Button(root, text='solid', borderwidth=3, relief='solid').grid(row=3, column=6)

Label(root, text='borderwidth = 4').grid(row=4, column=0)
Button(root, text='raised', borderwidth=4, relief='raised').grid(row=4, column=1)
Button(root, text='sunken', borderwidth=4, relief='sunken').grid(row=4, column=2)
Button(root, text='flat', borderwidth=4, relief='flat').grid(row=4, column=3)
Button(root, text='ridge', borderwidth=4, relief='ridge').grid(row=4, column=4)
Button(root, text='groove', borderwidth=4, relief='groove').grid(row=4, column=5)
Button(root, text='solid', borderwidth=4, relief='solid').grid(row=4, column=6)

root.mainloop()