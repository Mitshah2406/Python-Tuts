from tkinter import *
import parser

root = Tk()
root.title('Calculator')

# get user input and display it
i = 0


def get_variables(num):
    global i
    # i means index position and num means the number every time user enters a number the index position changes
    display.insert(i, num)
    i += 1


def calculate():
    newstring = display.get()
    try:
        a = parser.expr(newstring).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

# function for clearing display


def clear_all():
    string = display.get()
    if len(string) > 0:
        display.delete(0, END)
    else:
        display.insert(0, "Error")


def undo():
    string = display.get()
    if len(string) > 0:
        newstring = string[:-1]
        clear_all()
        display.insert(0, newstring)
    else:
        clear_all()
        display.insert(0, "Error")


# adding input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# adding buttons
Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2)

# adding operators
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)


Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="X", command=lambda: get_operation("X")).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3)


Button(root, text="π", command=lambda: get_operation("*3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: get_operation("**2")).grid(row=5, column=4)


Button(root, text="del", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="00", command=lambda: get_operation("00")).grid(row=3, column=5)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5)
Button(root, text="x²", command=lambda: get_operation("**2")).grid(row=5, column=5)


root.mainloop()
