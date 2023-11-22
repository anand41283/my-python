#1
# a=(1,2,3,4,4)
# l1=list(a)
# l1.append(5)
# b=tuple(l1)
# print(b)


#2
# a=(2,3)
# if(type(a)==tuple):
#     print("Its a tuple")
# elif    

#3

# a=('a','h','k','b')
# l1=list(a)
# l1.sort()
# x=tuple(l1)
# print(l1)

#4
# a=('a','h','k','b')
# b=input("enter the element to check: ")
# print(b in a)
# # if(b in a):
# #     print("The element is present in the tuple")
# # else:
# #     print("The element is not present in the tuple")    




tuple_1=("blue","red","green","apple","orange",23,45,67,23.5,67.8,100,"red","red")
print(tuple_1[0],tuple_1[-1]) #5
print(tuple_1[2:])#6
print(tuple_1[:6])#7
print(tuple_1[3::3])#8
print(tuple_1[::])#9
# print(max(tuple_1))#10 it will show error
# print(min(tuple_1))#11)  """"""""""""""""
print(tuple_1.index(23.5))#12
print(tuple_1.count("red"))#13
b=(67,"nami","mittu",8)#14
z=tuple_1+b
print(z)
print(len(z))#15
for i in z:#16
    print(i)
h,j,k,l,*m=z#17
print(h)   
print(j)
print(k)
print(l)
print(m)    
s=(23,)#20
print(s)
print(type(s))





