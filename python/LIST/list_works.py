#create new list and add fruits
# a=int(input("Enter the limit of the list"))
l1=['apple','banana','kiwi','mango']
# for i in range(0,a):
#     l1.append(input("Enter the element"))
print(l1)

#print the first and last elements


print(l1[0],l1[-1])

#change the value apple to kiwi

l1[0]="kiwi"
print(l1)

#remove th last element

l1.remove('mango')
print(l1)

#add new element

l1.insert(0,"mango")
print(l1)

#add new element to index=4
l1.insert(4,"jackfruit")
print(l1)

# pop out element index=3