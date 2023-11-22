# for i in range(0,6):
#     for j in range(0,i+1):
#         # print(i)
#         print("*", end="   ")
#     print()    
    

# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    

# words="Let's google the pineapple photo"
# l1=list(words)
# li=[]

# for i in l1:
    
#     if i not in li:
#         li.append(i)
# print(li) 
# z="".join(li)     
# print(z)  

# whole removing

# string="lets's google the pineapple photos"
# str=string.split()
# for i in str:
#    with_out_duplicates=[]
#    for j in i:
#         if j not in with_out_duplicates:
#             with_out_duplicates.append(j)
#    print("".join(with_out_duplicates),end=' ')



#list compre.   

# string="lets's google the pineapple photos"
# result=[''.join([char for i,char in enumerate(words)])]

                                                                                                                                                                                                                                                                                                                                                                
            
       
        
string="lets's google the pineapple photos"
result=[''.join([char for i,char in enumerate(string) if string.find(char)==i]) for string in string.split()]

