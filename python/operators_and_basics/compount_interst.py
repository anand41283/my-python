p=int(input("Enter the principal amount: "))
n=int(input("Enter the duration per year: "))
r=int(input("Enter the rate of interest: "))
compount=(p*(1+(r/100))**n-p)
print("The compount rate of interest is: ", compount),