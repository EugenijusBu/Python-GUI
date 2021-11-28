from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.grid()

myButton1 = Button(root, text="Start", command=myClick, bg="black", fg="cyan")
myButton1.pack()

root.mainloop()