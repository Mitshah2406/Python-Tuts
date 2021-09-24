#Using the concept of operator overloading in Python, change the behavior of the multiplication operator in a way that multiplication operator behaves like an addition operator.

class Math:
    def __init__(self,x):
        self.x = x

    def __mul__(self,oper):
        x = self.x+ oper.x
        return (x)


number = Math(4)
num2 = Math(5)
print(number*num2)

