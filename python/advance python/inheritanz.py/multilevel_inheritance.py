#MULTILEVEL INHERITANCE
#-----------------------

# the chid class inherit the all properties and metheod from intermediate clas that allready inherit the parent class

# class base:
#     def fun1(self):
#         print("grandfather")
# class father:
#     def fun2(base):
#         print("father")
# class child:
#     def fun3(father):
#         print("child")

# object=child()
# object.fun1()
# object.fun2()
# object.fun3()      


# example

class base:
    #constructor
    def __init__(self,name):
        self.name=name

    def getname(self):
        return self.name
    
class child(base):

    def __init__(self, name,age):
        base.__init__(self,name) 
        self.age=age

    def getage(self):
        return self.age   

class grandchild(child):
    def __init__(self,name,age,address):
        child.__init__(self,name,age)
        self.address=address

    def getaddress(self):
        return self.address

object=grandchild("sai",21,"kozhikode")
print(object.getname(),object.getage(),object.getaddress())


             

