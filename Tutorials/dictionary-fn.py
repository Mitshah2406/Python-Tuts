# Dictionary functions



# 1)to check whether a value is there or not.

numbers = {

    1 : "one",

    2 : "two",

    3 : "three"

}

print(3 in numbers)

#2. Get function - A function which is used to extract a particular value from the dictionary.

print(numbers.get(6,"key not found"))