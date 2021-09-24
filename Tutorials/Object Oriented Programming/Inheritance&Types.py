#inheritance

#it means a class which can access attribute of other class
class Student:

    def __init__(self,name,age):
        self.name =name
        self.age =age

    def getdata(self):
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")

    def putdata(self):
        print(self.name)
        print(self.age)

class Sciencestudent(Student): #here, ---Sciencestudent--- is sub class ---OR----- derived class and ---Student--- is base class

    def science(self):
        print("This is a science method")

s1=Sciencestudent("","")
s1.getdata()
s1.putdata()
s1.science()


#------------Types-----------------

# --------------1)Multiple Inheritance----------------

class A:
    def a_method(self):
        print("This is Method A")
    
class B:
    def b_method(self):
        print("This is Method B")
#multiple inheritance is simple as inheritance but you just need to type comma and you can inherit as many class as you want    
class C(A,B):
    def c_method(self):
        print("This is Method C")

c1 = C()
c1.a_method()
c1.b_method()
c1.c_method()

#---------------2)Multi-level inheritance------------

class A:
    def a_method(self):
        print("This is Method A")
    
#multi-level inheritance is inheriting one class(A) to another(B). 
# So B class got attributes of both A and B, So if you want that attributes of A and B should inherit in (C class)
#You can directly write B becauseB has attribute of A also.So C is inheriting attribute of B directly And A indirectly.
class B(A):
    def b_method(self):
        print("This is Method B")
class C(B):
    def c_method(self):
        print("This is Method C")

c1 = C()
c1.a_method()
c1.b_method()
c1.c_method()
    