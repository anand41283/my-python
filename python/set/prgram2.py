# create blank set and add elements(12)

# s=set()
# tu={1,2,3,4,5,6,7,8,9,10,11,12}
# s.update(tu)
# print(s)

#check given elements in present or not using if 

# de={"blue","green","red","white",23,45,67}
# gi=input("Enter the element ")
# for i in de:
#     if(i==int):
#         k=gi in de
#         if (k==True):
#             print("The element is present")
#         else:
#             print("The element is not present")
#             continue
#     if(i==str):
#         g=gi in de
#         if (g==True):
#             print("The element is present")
#         else:
#             print("The element is not present")


# add list of elements  to a set

# l1=("bike","car")
# s1={"kiwi"}

# s1.update(l1)
# print(s1)


# 4.create a set(fruits) and add 8 fruits in to it

# fruits=set()
# s={'kiwi','apple','mango','banana','orange','pineapple','jackfruit','strwburry'}
# fruits.update(s)
# print(fruits)

# 5. Return a new set of identical items from 2 sets

# s1={2,3,4,5}
# s3={8,6,4,3}
# s4=s1.intersection(s3)
# print(s4)

# 6. Get only unique items from 2 sets

# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# b=set1.symmetric_difference(set2)
# print(b)

# 7.Update the first set with items that dont exist in the second set

# set2={10,20,30}
# set3={20,40,50}
# set2.difference_update(set3)
# print(set2)

# 8.Return a set of elemnt present in set a or b but not both

# set1={10,20,30,40,50}
# set3={30,40,50,60,70}
# set1.symmetric_difference_update(set3)
# print(set1)

# 9.Check if 2 sets have any elements in common ,if yes print the common element
    
# set1={10,20,30,40,50}
# set3={30,40,50,60,70}
# set4=set1.isdisjoint(set3)
# if set4==False:
#     set5=set1.intersection(set3)
#     print(set5)
# else:
#     print("There is no common elements")    


# 10.update set1 by adding items from set2 except common
# set1={10,20,30,40,50}
# set3={30,40,50,60,70}
# set1.update(set3)
# print(set1)

# 11.Remove items from set1 that are not common to both set1 and set2
# set1={10,20,30,40,50}
# set3={30,40,50,60,70}
# set4=set1.difference(set3)
# print(set4)

# 12. prgm to check if two given sets have no elements in common
# set1={1,2,3}
# set2={4,5,6}
# print(set1.isdisjoint(set2))


# 13. pgm to remove all elemnts from given set
# set2={1,2,3,4,5,7}
# set2.clear()
# print(set2)

# # 14.convert a set in to list
# li=list(set2)
# print(li)















        



            
       