from tkinter import *


root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topFrame, text="nowy folder", fg="Black")
button2 = Button(topFrame, text="lewo" , fg= "Black")
button3 = Button(topFrame, text="prawo" , fg="Black")
button4 = Button(topFrame, text="zdjęcie" , fg="Black")
button5 = Button(topFrame, text="wycinanie punktowe", fg="Black")
button6 = Button(topFrame, text="wycinanie większych obszarów", fg="Black")



button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()


root.mainloop()

