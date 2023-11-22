"""
3. Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later

"""

class base:
    class_prameter="class parameter"

    def __init__(self,instance_parameter):
        self.instance_parameter=instance_parameter
        

obj=base("value parameter")
print(base.class_prameter)
print(obj.instance_parameter)


        