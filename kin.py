from tkinter import *

root = Tk()

#creat a label widget
mylabel1 = Label(root, text="hello")
mylabel2 = Label(root, text="my name is ali")
#shoving it on to screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)

root.mainloop()
