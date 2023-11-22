a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if(b<a>c):
    first=a
    if(b>c):
        second=b
        third=c
    else:
        second=c
        third=b
elif(a<b>c):
    first=b
    if(a>c):
        second=a
        third=c
    else:
        second=c
        third=a
elif(a<c>b):
    first=c
    if(a<b):
        second=a
        third=b
    else:
        second=b
        third=a                
print(first,second,third)
      