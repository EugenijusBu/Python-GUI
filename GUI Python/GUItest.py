from tkinter import *

root = Tk()

#  Creating a widget
myLabel1 = Label(root, text= "Hello world!")
myLabel2 = Label(root, text= "Edga yra duhas toki lesi gaidi ramu gaidosika i lesyklele")

#idedam My label i ekrana (nebutina rasyt apacioj galima iskart)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

root.mainloop()