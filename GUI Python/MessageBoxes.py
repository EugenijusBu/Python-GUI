from tkinter import *
from tkinter import messagebox

root = Tk()



def popup():
    response = messagebox.askokcancel("This is my popup","Hello world!")
    #Label(root, text=response).pack()
    if response ==1:
        Label(root, text="you clicked yes!").pack()
    elif response==0:
         Label(root, text="you clicked no!").pack()
Button(root, text="Message box!",command=popup).pack()


mainloop()