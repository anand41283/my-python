# items=[1,2,3,4]
# sqr=list(map(lambda x: x**2,items))#map work like for loop
# sqr=[i**2 for i in items]#with list comprehensive metheod
# print(sqr)



#another  maping

# items=[1,2,3,4]
# items2=[1,2,3,4]
# add=list(map(lambda x,y:x+y,items,items2))
# print(add)

#filter

# numbers=[-3,-6,-5,2,5,6,-2]
# # lessthanzero=filter(lambda x: x<0,numbers)
# print(list(lessthanzero))


# numbers=[-3,-6,-5,2,8,8,5,6,-2]
# even=filter(lambda x: x%2==0,numbers)
# print(list(even))


# words=['apple','banana','grapes','cherry','pineapple']
# l=filter(lambda x: len(x)>5,words)
# print(list(l))

#using function

# words=['apple','banana','grapes','cherry','pineapple']
# def value(words):
#     return len(words)>5
# l=filter(value,words)
# print(list(l))

#removing empty 

# words=['apple','','banana','grapes','','cherry','pineapple']
# # non_empty=filter(lambda x: x!="",words)
# #using function
# def non_emp(words):
#     return words!=""
# non_empty=filter(non_emp,words)
# print(list(non_empty))



#reduce
#for reducing normally we do the print commant will give out side the loop

from functools import reduce

list=[1,2,4,6]
product=reduce((lambda x,y:x*y),list)
print(product)

list1=[for i in range(1,11)]
sum=reduce()