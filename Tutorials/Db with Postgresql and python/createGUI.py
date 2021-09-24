from tkinter import *
import tkinter as tk
import psycopg2
# --------------------Create GUI-------------------------------


def get_data(name, age, address):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="mitadi", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''INSERT INTO student(NAME,AGE,ADDRESS) VALUES(%s,%s,%s);'''
    cur.execute(query, (name, age, address))
    conn.commit()
    conn.close()


def get_id(id_num):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="mitadi", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM student WHERE id = %s;'''
    cur.execute(query, (id_num))
    result = cur.fetchone()
    display(result)
    display_all()
    conn.commit()
    conn.close()


def display(result):
    listbox = Listbox(frame, height=1, width=20)
    listbox.grid(row=7, column=1)
    listbox.insert(END, result)

def display_all():
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="mitadi", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM student;'''
    cur.execute(query)
    result = cur.fetchall()

    listbox = Listbox(frame, height=5, width=20)
    listbox.grid(row=9, column=1)
    for x in result:
        listbox.insert(END, x)



root = Tk()
canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
# relx and rely are margin and relwidth/height are 0.8 * height or width of canvas
# place is a method for placing an object over another
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

label = Label(frame, text="Add Data")
label.grid(row=0, column=1)

# ------------------Adding Entries---------------------


label = Label(frame, text="Name: ")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

label = Label(frame, text="Age: ")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

label = Label(frame, text="Address: ")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

# adding button and saving entered data into database

btn = Button(frame, text="Add", command=lambda: get_data(
    entry_name.get(), entry_age.get(), entry_address.get()))
btn.grid(row=4, column=1)


# searching data


label = Label(frame, text="Search Data ")
label.grid(row=5, column=1)

label = Label(frame, text="Search By ID: ")
label.grid(row=6, column=0)

search_id = Entry(frame)
search_id.grid(row=6, column=1)

btn = Button(frame, text="Search", command=lambda: get_id(search_id.get()))
btn.grid(row=6, column=2)
btn = Button(frame, text="Display All Entries", command=lambda: display_all())
btn.grid(row=8, column=2)
root.mainloop()
