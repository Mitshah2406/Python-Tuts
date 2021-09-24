# ---------------------Grid Layout-------------------
# grid is in the form of rows and columns.
# it is just another way of designing in the form of grid 
# i.e. you could actually place your elements depending upon the room number and the column numbers.


# Creating a form using Grid Layout.
from tkinter import *

root =Tk()

label1 = Label(root,text="First Name: ")
label2 = Label(root, text="Last Name: ")

#here, textfields are called as entry (text box)
name1= Entry(root)
name2= Entry(root)

#alligning the elemnts using grid by giving them row and column number

label1.grid(row = 0, column = 0)
name1.grid(row= 0, column = 1)

label2.grid(row = 1, column = 0)
name2.grid(row= 1, column = 1)
root.mainloop()