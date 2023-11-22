#print each vowels and consonants






#create a fn accepts 2 numbers and returns its difference
# def diff(a,b):
#     if a>b:
#         return a-b
#     else:
#         return b-a
    

# print(diff(30,20))
# print(diff(20,30))    

                                                                                                                                                                                        
# def factorial(a):
#     for i in range(1,a+1):
#         fact=1
#         fact*=i
#     return fact

# num=int(input("Enter the number"))
# print("factorial is ",factorial(num))    


# check given number is prime or not
# def prime(b):
#     for i in range(2,b):
#         if b%i==0:
#             return "Not prime number"
#             break
#         else:
#             return "Prime Number"
        
# c=int(input("Enter the number"))
# print(prime(c))



# define function tha acept roll number and returns whether the student is present or not 
# [20,45,78,65,2,3,4,5]

# def present_or_not(d):
#     li=[20,45,78,65,2,3,4,5]
#     return "present" if d in li else "Not Present"#ternory method
    
# roll=int(input("Enter the roll number")) 
# print(present_or_not(roll))   



# swap using function

# def swap(n1,n2):
#     n1,n2=n2,n1
#     return n1,n2


# d=int(input("Enter 2 number to swap: "))
# f=int(input())
# print(swap(d,f))


# define a fn that convert the upper case to ,lower case
b=input("Enter the string: ")
def upper(s):
    return s.upper()

def lower(c):
    return c.lower()
print(lower(b))
print(upper(b))

# if b==lower:
#     print(upper(b))
# else:
#     print(lower(b))    