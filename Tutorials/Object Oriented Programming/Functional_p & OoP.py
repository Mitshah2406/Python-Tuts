#functional programming V/S OOP
#SIMPLE PROGRAM TO ACCEPT STUDENT NAME AND AGE

#FUNCTIONAL PROGRAMING


# def data():
#     name = input("Enter Name:")
#     age = input("Enter Age:")
#     print(name)
#     print(age)

# data()



#OOP

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

student1= Student(" "," ")
student1.getdata()
student1.putdata()