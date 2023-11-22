#swap
print("swapping")
a=int(input("A = "))
b=int(input("B = "))
#method 1
# temp=a
# a=b
# b=temp
# print("After swaping")
# print("A = ",a)
# print("B = ",b)
#method 2
# a,b=b,a #tuple unpacking
# print("After swaping")
# print("A =", a)
# print("B =", b)
# method 3
a=a+b
b=a-b
a=a-b
print("After swaping")
print("A =", a)
print("B =", b)

