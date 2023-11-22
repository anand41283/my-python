num=int(input("Enter the number "))
fact=1
if(num<0):
    print("sorry")
elif(num==0):
    print("Fatctorial od 0 is 1")
else:    
    for i in range(1,num+1):
         fact*=i
    print(fact)