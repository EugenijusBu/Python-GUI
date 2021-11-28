from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

#frame = LabelFrame(root, text="frame", padx=5, pady=5).grid(column=0, row=0)

def select():
    
    global images    
    root.filename = filedialog.askopenfilename(initialdir="/GUI/images", title="Select A File", filetypes=(("png files","*.png"),("all files","*.*")))
    images = ImageTk.PhotoImage(Image.open(root.filename))
    location_label = Label(root, text=root.filename)
    #location_label.pack_forget()
    location_label.grid(column=1, row=1)
    
    my_label = Label(root, image=images)
    #my_label.pack_forget()
    my_label.grid(column=1,row=2)
    

button = Button(root, text="Select image", command=select).grid(column=1,row=0)

mainloop()