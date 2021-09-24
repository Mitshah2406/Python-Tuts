# Generators in Python

# Generators are used to generate numbers in a list.

def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1


for x in function():
    print(x)


# printing even number
def even_numbers(x):
 
    for i in range(1, x):
        if i % 2 == 0:
            yield i
 
 
limit = int(input('num:'))
print(list(even_numbers(limit)))
