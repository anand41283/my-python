num=int(input("enter the number "))
sum=0
temp=num
while temp>0:
    digit=temp%10**3
    temp//=10
if sum==num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")        