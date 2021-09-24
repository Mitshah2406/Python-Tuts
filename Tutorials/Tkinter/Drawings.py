# -------------------------Drawings----------------------
from tkinter import *
root = Tk()
canvas = Canvas(root, height= 200,width=200) #for drawings,we need Canvas class
line = canvas.create_line(0,0,50,100) # coordinates of start to end in form of x1,y1,x2,y2
rectangle = canvas.create_rectangle(52,52,85,105)
oval = canvas.create_oval(95,7,35,45)
#in this way we can create drawings.
canvas.pack()
root.mainloop()