from tkinter import *

root = Tk()

def open():
    top = Toplevel()
    label = Label(top, text="Hello world").pack()


btn = Button(root, text="Open second window!", command=open).pack()



mainloop()