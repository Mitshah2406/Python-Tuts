# Itertools is a module
# ways of importing module
# 1)import a specific function from module
# from itertools import accumalate
# 2)import full module and use it as eg: itertools.count()
import itertools

for x in itertools.count(5):  # count function takes a number to start and print numbers till infinity
    print(x)
    if x >= 20:
        break

numbers = list(itertools.accumulate(range(8))) #accumalate keeps on adding a number eg: 0, 0 + 1 = 1, 1  + next_num(2) = 3, 3 + 3 = 6, 6 + 4 = 10
print(numbers)

print(list(itertools.takewhile(lambda i: i <= 10, numbers))) #takewhile takes a list and function which specifies till where to print a list
