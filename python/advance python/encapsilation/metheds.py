"""
Static Method
-----------------
A static method is a general utility method that performs a task in isolation. Inside this method, 
we don’t use instance or class variable because this static method doesn’t take any parameters like 
self and cls.

A static method is bound to the class and not the object of the class. Therefore, we can call it using
 the class name.

A static method doesn’t have access to the class and instance variables because it does not receive an 
implicit first argument like self and cls.
Therefore it cannot modify the state of the object or class

Syntax:
class ClassName(object):
@staticmethod
def function_name():
    pass

UTILITY FUNCTIONS
-------------------
A utility function in Python is a small, self-contained piece of code that performs a specific task. 
It's called a "utility" because it's a helpful tool that makes a certain task easier to perform. 
These functions are not meant to be standalone, but rather to be used in conjunction with other code.
"""

"""
Methods are 2 two types:
1. instance methods
2. static method
"""