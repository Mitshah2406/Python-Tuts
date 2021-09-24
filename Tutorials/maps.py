# Maps

# So what map allows us to do basically is that map actually allows us to operate on a list or perform a single operation on a given list.
# 1)using fn
# def add_two(x):
#     return x*2


# num = [10, 20, 30, 40, 50, 60, 70]
# result = list(map(add_two, num))
# print(list(map(add_two, num)))

# 2)using lambda
num = [10, 20, 30, 40, 50, 60, 70]

print(list(map(lambda x: x*2, num)))
