l1=[1,2,3,4,4,3,5,6,2]
print(l1)
n=int(input("Enter the element to remove"))
for i in l1:
    if(n==i):
        l1.remove(n)
print(l1)        
