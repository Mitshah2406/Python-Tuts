import bcrypt
from tkinter import *

root = Tk()
def check(password):
    hashed = b'$2b$12$TJHBVN7Wg7Z01Y2LXKvvBelnW9en5NtewiFKYSzpKpMJf.iiySzEe'

    password = bytes(password,encoding='utf-8')

    if bcrypt.checkpw(password, hashed):
        print("Login Success")
    else:
        print("Invalid password")



root.geometry('300x300')
root.title('Password Validator')


text = Label(root,text="Enter Your Password:")
entered_password = Entry(root)

text.grid(row=0,column=0)
entered_password.grid(row=0,column=1)

validate_btn = Button(root,text="Validate",command= lambda: check(entered_password.get()))
validate_btn.grid(row=1,column=1)
root.mainloop()



