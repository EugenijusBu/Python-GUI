from tkinter import *

root = Tk()
root.geometry("600x600")


var = IntVar()

c = Checkbutton(root, text="pirmas pasirinkimas", variable=var, onvalue=3, offvalue=2)
#c.deselect()
c.pack()

def spausdinti():
    label = Label(root, text=var.get()).pack()

btn = Button(root, text="Spausdinti pasirinkima", command=spausdinti).pack()
mainloop()