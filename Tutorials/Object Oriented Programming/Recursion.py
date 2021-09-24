#----------------RECURSION------------------

#function calling itself is called as recursion.

#finding factorial of number using recursion
# factorial mean 

#eg - factorial of 5
#it is found till value reaches 1
# (5)*(4)*(3)*(2)*(1)

def factorial(x):
    if x==1:
        return 1
    else:
        return (x)*(factorial(x-1))

number= int(input("Enter a integer: "))
print(factorial(number))

