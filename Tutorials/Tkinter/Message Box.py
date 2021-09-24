# -------------------------Message Box-----------------------
from tkinter import * 
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Error", "Error 404")

response=tkinter.messagebox.askquestion("Question","Do you like Cricket? ")
if response == "yes":
    print("Great! ")
root.mainloop()