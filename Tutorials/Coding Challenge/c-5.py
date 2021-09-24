# Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.

def divide(a, b):
    try:
        c = a/b
        return c
    except ZeroDivisionError:
        print('There is a divide by zero error. Please enter another number.')
        return 0


first_n = float(input('Enter the first number: '))
second_n = float(input('Enter the second number: '))

result = divide(first_n, second_n)
print(result)
