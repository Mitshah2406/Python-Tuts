# Errors and Exceptions.

# types of errors:
# 1)Syntax errors  -occurs due to invalid Syntax
# 2)Logical error  -occurs to programmer's incorrect logic.


#Exceptions:
# 1)ZeroDivisionError -a number can't be divided by zero

# Exception handling

try:  #in this, you write the code for which you think error might occur
    a = 20
    b = 0
    print(a / b)
 
except ZeroDivisionError:  #in this,you can handle the error and the program will run smoothly
    print("Any number can't be divided by zero.")

finally:
    print('This is going to be executed no matter what.')