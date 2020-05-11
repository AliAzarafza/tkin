from tkinter import *
import numpy

root = Tk()
root.title('Calculator')

f_num = int
entr = Entry(root, width=35, borderwidth=3)
entr.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def ButtonClick(number):
    # entr(0, END)
    curent = entr.get()
    entr.delete(0, END)
    entr.insert(0, str(curent) + str(number))

def ButtonClear():
    entr.delete(0, END)

def ButtonAdd():
    firstnum = entr.get()
    f_num = int(firstnum)
    entr.delete(0,END)
def plus(num1, num2):
    return num1 + num2

def ButtonEqual():
    secontnum = entr.get()
    entr.delete(0,END)
    s_num = int(secontnum)
    ans =  plus(f_num, s_num)
    entr.insert(0, ans)

#buttons
button_1 = Button(root, text="1", padx=35, pady=20, command=lambda: ButtonClick(1))
button_2 = Button(root, text="2", padx=35, pady=20, command=lambda: ButtonClick(2))
button_3 = Button(root, text="3", padx=35, pady=20, command=lambda: ButtonClick(3))
button_4 = Button(root, text="4", padx=35, pady=20, command=lambda: ButtonClick(4))
button_5 = Button(root, text="5", padx=35, pady=20, command=lambda: ButtonClick(5))
button_6 = Button(root, text="6", padx=35, pady=20, command=lambda: ButtonClick(6))
button_7 = Button(root, text="7", padx=35, pady=20, command=lambda: ButtonClick(7))
button_8 = Button(root, text="8", padx=35, pady=20, command=lambda: ButtonClick(8))
button_9 = Button(root, text="9", padx=35, pady=20, command=lambda: ButtonClick(9))
button_0 = Button(root, text="0", padx=35, pady=20, command=lambda: ButtonClick(0))
button_add = Button(root, text="+", padx=34, pady=20, command=ButtonAdd)
button_eqale = Button(root, text="=", padx=80, pady=20, command=ButtonEqual)
button_clear = Button(root, text="clear", padx=68, pady=20, command=ButtonClear)


#put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_eqale.grid(row=5, column=1, columnspan=2)





root.mainloop()
