class rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        print("The area of the given rectangle is: ",self.l*self.w)
obj=rectangle(2,6)
obj.area()            