# Operator Overloading

# it means that a operator such as + will do anything we say i.e, sub,divide,multiply,etc.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)
