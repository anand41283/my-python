
# 1. Write a python pgm to create a class representing a circle. Include methods to find area and perimeter
class circle:
    # r=int
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r   
    def perimeter(self):
        return 2*3.14*self.r 
c=circle(5)
# print(c.area())
# print(c.perimeter())   

# 2.W.p to create a calculator class. include methods for arithematic operations

class calculator:
    num1:int
    num2:int
    def enter(self,num1=0,num2=0):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2    
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    def rem(self):
        return self.num1%self.num2
cal=calculator()
cal.enter(10) 
print(cal.add()) 

# 3. Write a Python program to create a class that represents a shape. Include methods to calculate its area 
# and perimeter. Implement subclasses for different shapes like circle, triangle, and square.




