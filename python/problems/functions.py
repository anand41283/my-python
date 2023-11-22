# def area_circle(r):
#     return "Area of the circle ",3.14*r**2
# print(area_circle(3))



# def odd_number():
#     odd=[]
#     for i in range(1,51):
#         if i%2!=0:
#             odd.append(i)
#     print(odd)  
# odd_number()          



def odd_number():
    odd=[i for i in range(1,51) if i%2!=0]
    return odd
print(odd_number())


def even_number():
    even=[i for i in range(4,30) if i%2==0]
    return even
print(even_number())

# a=[1,2,3,4,5,6,7,8,9,10]
