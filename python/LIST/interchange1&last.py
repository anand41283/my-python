l1=['bus','blue','car',52,23.1,8]
# l1.pop()
# l1.insert(5,'bus')
# l1.pop(0)
# l1.insert(0,8)
# print(l1)

# l1[0],l1[-1]=l1[-1],l1[0]
# print(l1)
print(l1)
temp=l1[1]
l1[1]=l1[-1]
l1[-1]=temp
print(l1)