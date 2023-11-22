"""
4. Define a class named American which has a static method called printNationality.


Hints:

Use @staticmethod decorator to define class static method.

"""

def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()