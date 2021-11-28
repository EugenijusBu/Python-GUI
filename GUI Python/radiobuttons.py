from tkinter import *

root = Tk()


#r = IntVar()
#r.set("2")


MODES = [
    ("Treniruote","Treniruote"),
    ("Planas","Planas"),
    ("Mityba","Mityba"),
    ("Asmenine","Asmenine"),
    ("Lauko","Lauko"),
    ("Sudas kazkoks","Sud"),
]

treniruote = StringVar()
treniruote.set("Treniruote")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=treniruote, value=mode).pack()

def clicked(value):
    label = Label(root, text=value)
    label.pack()


#Radiobutton(root, text="option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

button = Button(root, text="sheesh!", command=lambda: clicked(treniruote.get()))
button.pack()

label = Label(root, text=treniruote.get())
label.pack()



mainloop()