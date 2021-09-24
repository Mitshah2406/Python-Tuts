from tkinter import * 
from module_compress import *

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)



window = Tk()
window.title("Compression Engine")
window.geometry("600x400")

# -----------------for compression----------------------------
input_comp = Label(window,text="Enter The file name to be compressed: ")
comp_ient = Entry(window)

output_comp = Label(window,text="Enter the compressed file name: ")
comp_oent = Entry(window)

comp_btn = Button(window,text= "Submit",command=lambda:compression(comp_ient.get(), comp_oent.get()))

input_comp.grid(row = 0,column = 0)
comp_ient.grid(row = 0,column = 1)
output_comp.grid(row = 1,column = 0)
comp_oent.grid(row = 1,column = 1)
comp_btn.grid(row=2,column=1)


# -----------------for decompression----------------------------

input_decomp = Label(window,text="Enter The file name to be decompressed: ")
decomp_ient = Entry(window)

output_decomp = Label(window,text="Enter the decompressed file name: ")
decomp_oent = Entry(window)

decomp_btn = Button(window,text= "Submit",command=lambda:decompression(decomp_ient.get(),decomp_oent.get()))

input_decomp.grid(row = 3,column = 0)
decomp_ient.grid(row = 3,column = 1)
output_decomp.grid(row = 4,column = 0)
decomp_oent.grid(row = 4,column = 1)
decomp_btn.grid(row=5,column=1)

window.mainloop()