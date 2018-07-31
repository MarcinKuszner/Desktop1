from tkinter import *


root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)


button1 = Button(root, text="nowy folder", fg="Black")
button2 = Button(root, text="lewo" , fg= "Black")
button3 = Button(root, text="prawo" , fg="Black")
button4 = Button(root, text="zdjęcie" , fg="Black")
button5 = Button(bottomframe, text="wycinanie punktowe", fg="Black")
button6 = Button(bottomframe, text="wycinanie większych obszarów", fg="Black")

root.geometry("1000x700")


button1.pack(fill = X)
button2.pack(side = RIGHT )
button3.pack(side=LEFT, fill = X)
button4.pack(fill = BOTH)
button5.pack( fill = X)
button6.pack(fill = X)


root.mainloop()

