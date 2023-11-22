# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
#  Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints:

# To override a method in super class, we can define a method with the same name in the super class.
class shape:
    
    def area(self):
        print("Area of the shape is 0") 
class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        print("The area of the square: ",self.length**2)
        super().area()
obj=square(5)
obj.area()                     