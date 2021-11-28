from tkinter import *


root = Tk()
root.geometry("400x400")

verticalslider = Scale(root, from_=0, to=600)
verticalslider.pack()

horizontalslider = Scale(root, from_=0, to= 600, orient = HORIZONTAL)
horizontalslider.pack()

#label= Label(root, text=horizontalslider.get()).pack()

def status():
    label= Label(root, text=horizontalslider.get()).pack()
    root.geometry(str(horizontalslider.get())+"x"+str(verticalslider.get()))

btn = Button(root, text="Slider status", command=status).pack()

mainloop()