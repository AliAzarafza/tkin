from tkinter import *

root = Tk()

entr = Entry(root)
entr.pack()



def myclick():
    mylabel = Label(root, text='look!!!  click!')
    mylabel.pack()


mybotton = Button(root, text='click', command=myclick, fg='green', bg='#008FFF')
mybotton.pack()

root.mainloop()
