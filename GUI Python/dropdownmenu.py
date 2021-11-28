from tkinter import *

root = Tk()
root.geometry("500x500")


def show():
    label = Label(root, text=clicked.get()).pack()



options = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday"
]

clicked = StringVar()
clicked.set(options[0])

dropbox = OptionMenu(root, clicked, *options)
#dropbox =OptionMenu(root, clicked, "Monday", "Tuesday","Wednesday","Thursday","Friday") 
dropbox.pack()


btn = Button(root,text="Selected", command=show).pack()

mainloop()