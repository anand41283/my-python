"""
POLYMORPHISM
------------
-> The literal meaning of the polymorphism is the condition of occurance in different forms.
->Polymorphism is a very important concept in programming.
->it refers to the use of single type enity (method,opertor or object) to represent different
 tupe in different scenarios.


 1. method overloading
 ->Two or more metheods can have the same name insdie the sam class if they accept different arguments 
 ->This feature is known as overloading
 ->metheod overloading achived by either: changing the number arguments.


 2. method overrinding

 ->in oops, is a language feature that allows a subclass or child class to provide a specific implementation of a method
  that is already provided by one of its superclass or parentclasses

  3. operator overloading

  ->same operator to have different meaning according to the context is called operator overloading

  4.
  ->duck typing

"""
#method overloading

class sum:
    def find_sum(self,a,b):
        print("Sum of two numbers is :", a+b)
    def find_sum(self,a,b,c):
        print(a+b+c)

obj=sum()
obj.find_sum(2,3)
obj.find_sum(2,3,4)

#python does not support method overloading
#the concept of method overloading is implemented using default arguments

class sum:
    def find(self,a=0,b=0,c=0):
        print(a+b+c)

        


        