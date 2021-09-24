class mould:
 quantity = 200

    def __init__(self, name, color):  # instance attributes are defined using init constructor. note : - self means the object that is defined. you can use any name instead of self
        self.name = name
        self.color = color


teddy1 = mould("Red", "Red")
teddy2 = mould("Rob", "Brown")
print(teddy1.name)
print(teddy1.color)
print(teddy2.name)
print(teddy2.color)
