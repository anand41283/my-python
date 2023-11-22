"""9. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" 
which can print "Male" for Male class and "Female" for Female class.

Hints:Use Subclass(Parentclass) to define a child class.
"""

class Person:
    
    def getgender(self):
        n=input("Enter male(M) or female(F): ")
        if (n=="M" or "m"):
            print("Male")
        elif (n=="F"or"f"):
            print("Female")
        else:
            print("invalid input")

class Male(Person):
    def getgender(self):
        print("Male")
        # super().getgender()

class Female(Person):
    def getgender(self):
        print("Female")
        super().getgender()

obj=Male()
obj1=Female()
obj.getgender()
obj1.getgender()        

