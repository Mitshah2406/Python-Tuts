# -----------------------Drop Down Menu------------------------------

from tkinter import *


def New_file():
    print("New File is created.")


def New_window():
    print("New Window is created.")


def Open_file():
    print("File has opened.")


def Open_folder():
    print("Folder has opened.")


def Open_workspace():
    print("Workspace has opened.")


def Open_recent():
    print("Recent Files are opened.")


def Addf_workspace():
    print("File has been added to workspace.")


def Save_workspace():
    print("Workspace has been saved.")


def Duplicate_workspace():
    print("Workspace has been duplicated.")


def Save():
    print("Saved")


def Save_as():
    print("Saved")


def Save_all():
    print("Saved")


def Exit():
    print("Exited")


def undoredo():
    print("Action Performed")


def toolbar_btn():
    print("Button Clicked")


root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)

submenu = Menu(mainmenu)
# add_cascade is for menu name
mainmenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="New File", command=New_file)
# add_command is for menu items
submenu.add_command(label="New Window", command=New_window)
submenu.add_separator()  # add_separator is for seperating line

submenu.add_command(label="Open File", command=Open_file)
submenu.add_command(label="Open Folder", command=Open_folder)
submenu.add_command(label="Open Workspace", command=Open_workspace)
submenu.add_command(label="Open Recent", command=Open_recent)
submenu.add_separator()

submenu.add_command(label="Add Folder To Workspace", command=Addf_workspace)
submenu.add_command(label="Save Workspace As", command=Save_workspace)
submenu.add_command(label="Duplicate Workspace", command=Duplicate_workspace)
submenu.add_separator()

submenu.add_command(label="Save", command=Save)
submenu.add_command(label="Save As", command=Save_as)
submenu.add_command(label="Save All", command=Save_all)
submenu.add_separator()

submenu.add_command(label="Exit", command=Exit)
editmenu = Menu(mainmenu)
mainmenu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=undoredo)
editmenu.add_command(label="Redo", command=undoredo)

# ---------------------ToolBar----------------------------------
# It is a frame.
toolbar = Frame(root, bg="grey")

insert = Button(toolbar, text="Insert Files", command=toolbar_btn)
# padx means padding on x-axis and similiarly pady means on y-axis.
insert.pack(side=LEFT, padx=3, pady=5)

printbtn = Button(toolbar, text="Print", command=toolbar_btn)
printbtn.pack(side=LEFT, padx=3, pady=5)

toolbar.pack(side=TOP, fill=X)


# --------------------------------Status Bar------------------------------
# It is a label.
#bd means border, relief =SUNKEN means it will give nice look to status bar , anchor =W means text will align to left hand side and W means west
statusbar = Label(root, text="This is a Status Bar", bd=2, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
root.mainloop()
