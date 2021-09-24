# String Functions

# 1)Join

# print(":".join(["Apple", "Banana", "Mango"]))
fruits = ("Mango", "Apple", "Banana")
operate = (":").join(fruits)
print(operate)

# 2)Replace

print("Hello World".replace("World", "There"))
newstring = ("Hello World")
newstring1 = newstring.replace("World", "There")
print(newstring1)

# 3)Starts with

newstring = ("This is the World")
newstring1 = newstring.startswith("This")
print(newstring1)

# 4)Ends with

newstring = ("This is the World")
newstring1 = newstring.endswith("World")
print(newstring1)

# 5)Upper Case

newstring = ("This is the World")
newstring1 = newstring.upper()
print(newstring1)

# 6)Lower Case

newstring = ("This is the World")
newstring1 = newstring.lower()
print(newstring1)