from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="sheeeeeesh!")
    myLabel.pack()

myButton1 = Button(root, text="Start", command=myClick, bg="black", fg="cyan")
myButton1.pack()

root.mainloop()