from tkinter import * 
from module_compress import *
from tkinter import filedialog


def file_open():
    name = filedialog.askopenfilename(initialdir="/",title="Select A File")
    return name

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)



window = Tk()
window.title("Compression Engine")
window.geometry("600x400")

# -----------------for compression----------------------------


comp_btn = Button(window,text= "Compress",command=lambda:compression(file_open(), "compressfile.txt"))

comp_btn.grid(row=2,column=1)


# -----------------for decompression----------------------------

decomp_btn = Button(window,text= "Decompress",command=lambda:decompression(file_open(),"decompressedfile.txt"))

decomp_btn.grid(row=5,column=1)

window.mainloop()