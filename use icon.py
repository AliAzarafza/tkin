from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('lern for your self')
root.iconbitmap('C:/Users/Ali/Pictures/gigapixel.ico')

myimege = ImageTk.PhotoImage(Image.open('fe96b10857930eefdf79d682bff35c50.jpg'))
mylabel =Label(image=myimege )
mylabel.pack()




ButtonQuit= Button(root, text='exit', command=root.quit)
ButtonQuit.pack()



root.mainloop()
