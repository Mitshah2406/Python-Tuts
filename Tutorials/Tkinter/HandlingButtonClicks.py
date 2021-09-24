# Handling Button Clicks
# when user clicks what should be displayed, we will control that.

from tkinter import *

root = Tk()

def clicked():
    print("You clicked this button.")

button1= Button(root, text="Click Here",command= clicked)
button1.pack()
root.mainloop()