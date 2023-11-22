"""5. Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.
"""
class american:
    def aa(self):
        print("america")
class newyork(american):
    def bb(self):
        print("newyork")   

obj=newyork()
obj.aa()
obj.bb()             
