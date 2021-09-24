
# List Operations
# 1)Create a list and later change a element in it by its index number with list operations.

num = [1, 2, 3, 4, 5]
num[2] = 7
print(num)

# 2)Adding two list {Concatenation}

num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
print(num1+num2)

# 3)multiplication of list{i.e, if you written a list and you want to write it three times then you multiply it.}

list1 = [1, 1, 1, 1, 1]
print(list1*2)

# 4)Checking whether an element is present in the list or not. (CASE-SENSITIVE)

fruits = ["Mango", "Apple", "Orange"]
# ans is false because this operation is case-sensitive.
print("APPLE" in fruits)
