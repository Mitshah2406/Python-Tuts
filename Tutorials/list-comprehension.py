#List Comprehension

# 1)printing square of numbers using list Comprehension.

list=[x**2 for x in range(11)]
print(list)

#2) printing only even square numbers

list=[x**2 for x in range(11) if x**2 % 2==0]
print(list)