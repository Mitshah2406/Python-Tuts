#--------------Building Graphical user Interface(GUI) using Tkinter--------------------
#Tkinter is a module
#printing hello world
from tkinter import *
#here, Tk() is a class and after writing it, a window is created.
root = Tk() 
#label is a function which needs an object and the label belongs to that object and the content to be written in that object. so, we have created a label.
label1 =Label(root, text= "Hello world")
#But, after creating it we need to add it to the window so we pack
label1.pack() 
#mainloop is used for holding the window on screen until we close it manuallly. Without it, window will open and close automatically very fast.
root.mainloop()