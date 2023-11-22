# circle area
class circle:

    def __init__(self):
        self.r = int(input("Enter the radius: "))

    # def __init__(self,r):
    #     self.r=r

    def area(self):
        print("Area of the given circle of radius is: ", 3.14*(self.r**2))


obj = circle()
obj.area()
