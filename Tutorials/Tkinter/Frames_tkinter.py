# ---------------------------Frames-----------------------
#Used to arrange widgets n a window
# Frames is nothing but a container in which we can add widgets and it is inside another container called window.
from tkinter import *
root=Tk()

#creating a frame
firstframe= Frame(root)  
firstframe.pack()

#alligning a other frame to bottom
secondframe=Frame(root)
secondframe.pack(side=BOTTOM)

#placing buttons on frame
#----------------NOTE: fg means foreground color or text color---------------
button1 = Button(firstframe,text="Click Here",fg="Red")
button2 = Button(secondframe,text="Click Here",fg="Blue")

button1.pack()
button2.pack()

root.mainloop()