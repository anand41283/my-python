numbers=[]
square=[]
cube=[]

n=int(input("Enter the limit of the list"))

for i in range(0,n):
    numbers.append(int(input("Enter the elements")))
for x in numbers:
    square.append(x**2)
    cube.append(x**3) 

print(numbers)
print(square)
print(cube)       