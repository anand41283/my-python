"""
ACCESS MODIFIERS

- access modifiers are used to set the accessbilility (visibitity) of classes,interfaces,variable,methods
construction and data members

- There are 3 type of modifiers:
 
->There are 3 types of access modifiers
    -private: only visible within its class or interface declaration
    -public: accessible from anywhere in your code. default access modifier for all declarations
    -protected: The members of a class that are declared protected are only accessible to a class
    derived from it
    
    
Public Access Modifier
-By default the member variables and methods are public which means they can befaccessed from anyuhere
    outside or inside the class.
-No public keyword is required to make the class or methods and properties public

Private Access Modifier
-> Class properties and methods with private access modifier can only be accessed within the class where
    they are defined and cannot be accessed outside the class.
-> In Python private properties and methods are declared by adding a prefix with two underscores ('__')
before their declaration.

"""

#Example of public
class student:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def display(self):
        return self.name,self.age

s1=student("raj",20)        
s1.display()

# Example of private

class bank:
    def __init__(self,acc_num,balance):
        self.acc_num=acc_num
        self.balance=balance
    def __display(self):
        print("Balance is ",self.balance)
    
s2=bank(10000,123)
s2.__display()#error because its an private data

# example of protectd
class student:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def _display(self):
        print("Name",self.name)
        print("age",self.age)
class stu(student):
    def __init__(self, name, age,rolno):
        super().__init__(name, age)
        self.rolno=rolno
    def display(self):
        self._display()
        print("roilno",self.rolno)
b1=stu("sai",18,23,)
# b1.display()