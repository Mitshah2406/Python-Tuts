# Filters in Python

# Filters is a function which can be used to filter out certain values out of a list.
def even(x):
    if x%2==0:
        return x

num = [10, 1, 2, 4, 8, 6, 7, 45, 25, 28, 60, 46, 47, 86]
# print(list(filter(lambda x: x % 2 == 0, num)))
print(list(filter(even,num)))