# -----------------------Self-Adjusting Widgets-----------------
# they change their size according to window size.
from tkinter import *
root = Tk()

label1 = Label(root, text="First Widget", bg="Yellow", fg="Red")
label2 = Label(root, text="Second Widget", bg="Red", fg="White")

label1.pack(fill=X)
label2.pack(side=RIGHT, fill=Y)
root.mainloop()
