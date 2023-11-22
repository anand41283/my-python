def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mull(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
def pow(a,b):
    return a**b
def flrdiv(a,b):
    return a//b

print("Enter 2 numbers")
num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
print("OPERATORS")
print("1 = For addition \n 2 = for substraction \n 3 = for multiply \n 4 = for division \n 5 = for reminder\n 6 = for power\n 7 = for floor division")
op=int(input("Enter the operator: "))
if op not in [1,2,3,4,5,6]:
    print("Invalid input")
elif op==1:
    print(add(num1,num2))
elif op==2:
    print(sub(num1,num2))
elif op==3:
    print(mull(num1,num2))
elif op==4:
    print(div(num1,num2))
elif op==5:
    print(rem(num1,num2))
elif op==6:
    print(pow(num1,num2))
elif op==7:
    print(flrdiv(num1,num2))                        


