# ----------------Data Hiding-----------------------
# Data hiding is one of the important feature of OOP.
# It hides which we we want to protect and not want to show it to external users.
# Syntax __variable name= Value

class Object:
    __num = 0 # this variable is hidden you can't access it

    def add(self,number):
        self.__num = +number
        print(self.__num)

obj1= Object()
obj1.add(5)
#trying to access hidden variable but it will not get recognized and produce error

print(obj1.__num)