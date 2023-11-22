
ascii_values=65
rows=int(input("Enter the rows "))
for i in range(rows):
    for j in range(i+1):
        print(chr(ascii_values),end=" ")
    ascii_values+=1
    print("\n")    