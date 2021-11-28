from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")

frame = LabelFrame(root, text="Frame...", padx= 50, pady=50)
frame.pack(pady=10,padx=10)

button = Button(frame, text="Hello", command=root.quit)
button.grid(row=0,column=0)

root.mainloop()