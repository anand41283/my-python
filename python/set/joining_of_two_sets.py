set1={1,2,3,4}
set2={1,2,3,5,6}
 
#union()

# set3=set1.union(set2)
# print(set3)

# #update

# set1.update(set2)
# print(set1) #add set to another set
#
#   # intersection

# set4=set1.intersection(set2)
# print(set4)

#intersection_update
set1.intersection_update(set2)
print(set1)

#symmetric difference

set5=set1.symmetric_difference(set2)
print(set5)