# Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.

# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.

# You can use any specifications which you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.
# Make sure that the sub classes have their own methods to get and display their special specification.

# Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class
class Computer:
    def __init__(self, ram, storage, processor):
        self.ram = ram
        self.storage = storage
        self.processor = processor

    def getspecs(self):
        print("Enter PC specs")
        self.ram = input("Enter your Pc's ram: ")
        self.storage = input("Enter your Pc's storage: ")
        self.processor = input("Enter your Pc's processor: ")

    def displayspecs(self):
        print("Here are the specs:  ")
        print("Your PC's ram is:" + self.ram + "Storage is:" +
              self.storage + "processor is: "+self.processor)


class Desktop(Computer):
    def __init__(self, case_color):
        self.case_color = case_color

    def d_getspecs(self):
        print("Enter desktop specs")
        self.case_color = input("Enter the case color: ")

    def d_displayspecs(self):
        print("Here are the specs:  ")
        print("Case color is "+self.case_color)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def l_getspecs(self):
        print("Enter Laptop specs")
        self.weight = input("Enter the weight: ")

    def l_displayspecs(self):
        print("Here are the specs:  ")
        print("Weight is "+self.weight)


mypc = Laptop("")
inpute = mypc.getspecs()
pri = mypc.displayspecs()
# print(mypc.d_getspecs)
# print(mypc.d_displayspecs)
input_a = mypc.l_getspecs()
pr_a = mypc.l_displayspecs()
print(inpute)
print(input_a)
print(pri)
print(pr_a)
