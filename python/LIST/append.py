l1=[1,2,3,4]
print(l1)
l1.append(5)#append
print(l1)

#insert

l1.insert(2,6)
print(l1)


#remove
l1.remove(5) #it will removw the element 5 in the list
print(l1)


#pop

# l1.pop(2)
l1.pop()
print(l1)

#del

del l1[1]
print(l1)
del l1
print(l1) #it will show error because it was deleted