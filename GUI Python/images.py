from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image tutorial")


my_img1 = ImageTk.PhotoImage(Image.open('images/logo2.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/linkus1.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/linkus2.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/linkus3.png'))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0,column=1, columnspan=3,padx= 30, pady=30)

status = Label(root, text="Image 1 of "+str(len(image_list)), anchor=E)

status.grid(row=2,column=1,columnspan=3,sticky=W+E)
    
def right(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=1, columnspan=3)
    button_right = Button(root, text=">>", command=lambda: right(image_number+1))
    button_left = Button(root, text="<<",command=lambda: left(image_number-1))
    if image_number == 4:
        button_right = Button(root,text=">>",state=DISABLED)

    status = Label(root, text="Image "+str(image_number)+ " of "+str(len(image_list)), anchor=E)
    status.grid(row=2,column=1,columnspan=3, sticky=W+E)

    button_left.grid(row=1,column=0)
    button_right.grid(row=1,column=2)


def left(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=1, columnspan=3)
    button_right = Button(root, text=">>", command=lambda: right(image_number+1))
    button_left = Button(root, text="<<",command=lambda: left(image_number-1))
    if image_number == 1:
        button_left = Button(root,text="<<",state=DISABLED)

    #x= image_number
    #if x==0:
     #   x=1
    status = Label(root, text="Image "+ str(image_number) + " of "+str(len(image_list)),anchor=E)
    status.grid(row=2,column=1,columnspan=3, sticky=W+E)

    button_left.grid(row=1,column=0)
    button_right.grid(row=1,column=2)

button_quit = Button(root, text="quit the program", command=root.quit)
button_left = Button(root, text="<<",command=left, state=DISABLED)
button_right = Button(root, text=">>", command=lambda: right(2))

button_quit.grid(row=1,column=1)
button_left.grid(row=1,column=0)
button_right.grid(row=1,column=2, pady=10)

root.mainloop()