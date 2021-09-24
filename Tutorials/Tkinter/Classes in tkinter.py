#in this, we will use classes to make two simple buttons
from tkinter import *

class Mybutton:

    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbtn = Button(frame, text = "Click Here", command=self.printtext)
        self.printbtn.pack()
        #frame.quit is a predefined fn
        self.exitbtn =Button(frame,text="Click to Quit", command = frame.quit)
        self.exitbtn.pack(side=LEFT)

    def printtext(self):
        print("You clicked this button")
root=Tk()
root1=Mybutton(root)
root.mainloop()