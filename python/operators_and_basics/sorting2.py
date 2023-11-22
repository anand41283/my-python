a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if(a>b and a>c):
    first=a
    if(b>c):
        second=b
        third=c
    else:
        second=c
        third=b
elif(a<b and b>c):
    first=b
    if(a>c):
        second=a
        third=c
    else:
        second=c
        third=a
elif(a<c and b<c):
    first=c
    if(a>b):
        second=a
        third=b
    else:
        second=b
        third=a              
print(first,second,third)