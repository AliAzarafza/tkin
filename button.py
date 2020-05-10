from tkinter import *

root = Tk()

entr = Entry(root, width=50)
entr.pack()
entr.insert(0, "entr your name")


def myclick():
    mylabel = Label(root, text=entr.get())
    mylabel.pack()


mybotton = Button(root, text='click', command=myclick, fg='green', bg='#008FFF')
mybotton.pack()

root.mainloop()
