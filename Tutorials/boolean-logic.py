# Boolean Logic


# Boolean Operator :


# 1)and

# It combines two conditions together.If we use "and" then both conditions should be true.

Username = (input("Enter your username:"))
Password = (input("Enter Your Password:"))

# if Username =="Admin" and Password =="Admin":
#     print("Valid user")

# else:
#     print("Invalid User")

# 2)Or
# it requires only one condition should be true.

if Username == "Admin" or Password == "Admin":
    print("Valid user")

else:
    print("Invalid User")
