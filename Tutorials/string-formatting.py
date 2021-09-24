# String formatting
# It allows you to combine strings with non-strings.

# printing date using string formatting.
number = [13, 12, 2020]
string = "Date :{0}/{1}/{2}".format(number[0], number[1], number[2])
print(string)

#second method by assigning values itself in format fn.
string = "{x}/{y}".format(x = 100, y = 200)
print(string)