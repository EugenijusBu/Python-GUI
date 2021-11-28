from tkinter import *

root = Tk()
root.title("Calculator")

ans = Entry(root, width=35, borderwidth=5)
ans.grid(column=0,row=0, columnspan=3, padx=10, pady=10)


def click(number):

    current = ans.get()
    ans.delete(0, END)
    ans.insert(0, str(current)+str(number))

def clear():
    ans.delete(0, END)

def add():
    number_1 = ans.get()
    global f_Anum
    global math
    math = "add"
    f_Anum = float(number_1)
    ans.delete(0, END)

def minus():
    number_1 = ans.get()
    global f_Anum
    global math
    math = "subtract"
    f_Anum = float(number_1)
    ans.delete(0, END)

def multiply():
    number_1 = ans.get()
    global f_Anum
    global math
    math = "multiply"
    f_Anum = float(number_1)
    ans.delete(0, END)

def divide():
    number_1 = ans.get()
    global f_Anum
    global math
    math = "divide"
    f_Anum = float(number_1)
    ans.delete(0, END)


def equal():
    number_2 = ans.get()
    ans.delete(0, END)
    if math=="add":
        ans.insert(0, f_Anum+float(number_2))
    if math=="subtract":
        ans.insert(0, f_Anum-float(number_2))
    if math=="multiply":
        ans.insert(0, f_Anum*float(number_2))   
    if math=="divide":
        ans.insert(0, f_Anum/float(number_2))


Button1 = Button(root, text="1", padx=40, pady=20, command= lambda: click(1))
Button2 = Button(root, text="2", padx=40, pady=20, command= lambda: click(2))
Button3 = Button(root, text="3", padx=40, pady=20, command= lambda: click(3))
Button4 = Button(root, text="4", padx=40, pady=20, command= lambda: click(4))
Button5 = Button(root, text="5", padx=40, pady=20, command= lambda: click(5))
Button6 = Button(root, text="6", padx=40, pady=20, command= lambda: click(6))
Button7 = Button(root, text="7", padx=40, pady=20, command= lambda: click(7))
Button8 = Button(root, text="8", padx=40, pady=20, command= lambda: click(8))
Button9 = Button(root, text="9", padx=40, pady=20, command= lambda: click(9))
Button0 = Button(root, text="0", padx=40, pady=20, command= lambda: click(0))
ButtonClear = Button(root, text="Clear", padx=77, pady=20, command= clear)
ButtonPlus = Button(root, text="+", padx=39, pady=20, command= add)
ButtonEqual = Button(root, text="=", padx=87, pady=20, command= equal)
ButtonMinus = Button(root, text="-", padx=41, pady=20, command=minus)
ButtonMultiply = Button(root, text="*", padx=41, pady=20,command=multiply)
ButtonDivision = Button(root, text="/", padx=41, pady=20,command=divide)


Button1.grid(column=0, row=3)
Button2.grid(column=1, row=3)
Button3.grid(column=2, row=3)

Button4.grid(column=0, row=2)
Button5.grid(column=1, row=2)
Button6.grid(column=2, row=2)

Button7.grid(column=0, row=1)
Button8.grid(column=1, row=1)
Button9.grid(column=2, row=1)

Button0.grid(column=0, row=4)

ButtonClear.grid(column=1,row=4, columnspan=2)
ButtonPlus.grid(column=0, row=5)
ButtonEqual.grid(column=1,row=5, columnspan=2)

ButtonMinus.grid(row=6, column=0)
ButtonMultiply.grid(row=6, column=1)
ButtonDivision.grid(row=6, column=2)



mainloop()