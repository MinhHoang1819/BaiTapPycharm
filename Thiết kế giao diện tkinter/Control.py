from tkinter import *

root = Tk()
root.title('Hoc control co ban.')
root.resizable(height=True, width=True)
root.minsize(height=200, width=300)

Label(root, text = 'Hello Tkinter!', fg='red').pack()
Button(root, text='Click me!', command=root.quit).pack()
e = StringVar()
e.set('hppt://communityuni.com')
Entry(root, textvariable = e, width=30).pack()

root.mainloop()