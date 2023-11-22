#1. python pgm to create an empty dictionary
a={}
print(a)

#2. python pgm to create a dictionary using dict() fn

b=()
b=dict(b)
print(b)
print(type(b))

#3. python pgm to create a dictionary with integer keys and print keys ,values and key-value pair

c={1:"Anand",2:"isac",3:"abhiram"}

for i in c:
    print(i)
for i in c.values():
    print(i)  
for i in c.items():
    print(i) 

#print(c.keys())   
#       
#4. python pgm to create a dictionary of 10 numbers and their squares

num_dic={}
for i in range(1,11):
    num_dic[i]=i**2
print(num_dic)    

#5. python pgm to create a dictionary and accessing each elements using get() method
c={1:"Anand",2:"isac",3:"abhiram"}
print(c.get(1))
print(c.get(2))


#6. python pgm to create a nested dictionary and aaccessing each elemnt

nes_dic={"Child1":{'Name':'Anand','age':21,'sex':'male'}, 
"Child2":{'Name':'Sai','age':22,'sex':'male'}}
    
print(nes_dic["Child1"]['Name'])    


#7. python pgm to create a dictionary and add 5 items to the dictionary
d={}
d[1]='benz'
d[2]='BMW'
d[3]='toyota'
d[4]='kia'
d[5]='maruthi'
d[6]='vw'
print(d)
#8. python pgm to create a dictionary with 7 items and remove 2 items using pop() and del

#9. python pgm to create a dictionary(fruits) with 3 items and change the fruit name apple to grapes
#10.python pgm to create a dictionary with 10 items and copy the dic to another dic using dict() and find
    #the length of new dictionary
#11.python pgm to create a dictionary and print each keys in dictionary
#12.python pgm to create a dictionary with interger value and key and print the sum of key-value pairs
    #s={1:11,2:45,3:41,4:62}
    #op [13,47,44,66]
#13.write a pgm to swap the position of dictionary item
mydic={1:"python",2:"php",3:".net",4:"c++"}
#op={1:"python",4:"c++",3:".net",2:"php"}