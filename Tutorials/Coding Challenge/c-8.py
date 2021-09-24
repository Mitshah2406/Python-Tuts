# List out  all the odd numbers from 1 to 100 using lists in Python.

# 1st method
numbers = [x for x in range(1, 101, 2)]
print(numbers)

# 2nd method

num = list(range(1, 101))
for x in num:
    if x % 2 != 0:
        print(x)
