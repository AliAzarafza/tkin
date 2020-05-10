from tkinter import *

root = Tk()

def myclick():
    mylabel = Label(root, text='look!!!  click!')
    mylabel.pack()


mybotton = Button(root, text='click', command=myclick)
mybotton.pack()

root.mainloop()
