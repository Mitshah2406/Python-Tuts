#Functional Programming

def add_ten(x):
    return x+10

def twice(func,arg):
    return func(func(arg))  #add_ten(add_ten(arg)) = add_ten(20) = 30


c = 10
print("The value is: ",twice(add_ten, c))
