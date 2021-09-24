class mould:
    quantity = 200

    def __init__(self,name,color):
        self.name = name
        self.color = color

    #this is a simple function but it is inside a class so it is called a class function and is also called as defining a method.
    def change_color(self,color):
         #method 1 by defining color here taking only self parameter
        # self.color = "White" 
        #method 2 by taking one more parameter as color and giving color while calling class function
        self.color=color

        
teddy1 = mould("ted", "Red")
print(teddy1.name)
print(teddy1.color)


teddy1.change_color("White")
print(teddy1.name)
print(teddy1.color)

